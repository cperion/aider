import pynvim
from neovim_io import NeovimIO

@pynvim.plugin
class AiderPlugin:
    def __init__(self, nvim):
        self.nvim = nvim
        self.io = None
        self.coder = None
        
        try:
            # Register plugin with Neovim
            self.nvim.command("let g:aider_plugin = v:lua.require('aider.core')")
            self.setup_keybindings()
        except Exception as e:
            self.nvim.err_write(f"Error initializing Aider plugin: {e}\n")
        
    def setup_keybindings(self):
        """Setup default keybindings for Aider operations"""
        self.nvim.command("nnoremap <silent> <leader>aa :Aider<CR>")
        self.nvim.command("nnoremap <silent> <leader>ac :AiderChat<CR>")
        self.nvim.command("nnoremap <silent> <leader>ad :AiderDiff<CR>")
        self.nvim.command("nnoremap <silent> <leader>au :AiderUndo<CR>")
        self.nvim.command("nnoremap <silent> <leader>am :AiderMap<CR>")
        self.nvim.command("nnoremap <silent> <leader>as :AiderSettings<CR>")
        self.nvim.command("nnoremap <silent> <leader>ah :AiderHelp<CR>")
        self.nvim.command("nnoremap <silent> <leader>at :AiderToggleMultiline<CR>")

    @pynvim.command('Aider', nargs='*', range='')
    def start_aider(self, args, range):
        """Start an Aider session in Neovim"""
        if self.io:
            self.nvim.err_write("Aider is already running\n")
            return

        # Try to restore previous session
        if self.restore_session():
            return

        # Create a new buffer for the chat
        buf = self.nvim.api.create_buf(False, True)
        self.nvim.api.set_current_buf(buf)
        
    def restore_session(self):
        """Restore a previous Aider session if it exists"""
        try:
            import json
            from pathlib import Path
            from aider.main import main
            
            session_file = self.get_session_file()
            if not session_file.exists():
                return False
                
            with open(session_file, "r") as f:
                session_data = json.load(f)
                
            # Restore chat buffer
            buf = self.nvim.api.create_buf(False, True)
            self.nvim.api.set_current_buf(buf)
            self.nvim.api.buf_set_lines(buf, 0, -1, True, session_data["chat_history"])
            
            # Initialize IO and Coder
            self.io = NeovimIO(self.nvim, buf)
            self.coder = main(return_coder=True, input=self.io, output=self.io)
            
            # Restore files
            for fname in session_data["files"]:
                self.coder.abs_fnames.add(fname)
                
            self.io.update_status("Restored")
            return True
            
        except Exception as e:
            self.nvim.err_write(f"Error restoring session: {e}\n")
            return False
            
    def save_session(self):
        """Save the current Aider session"""
        if not self.coder:
            return
            
        session_data = {
            "chat_history": self.nvim.api.buf_get_lines(self.io.buf, 0, -1, True),
            "files": list(self.coder.abs_fnames)
        }
        
        session_file = self.get_session_file()
        try:
            with open(session_file, "w") as f:
                json.dump(session_data, f)
        except Exception as e:
            self.nvim.err_write(f"Error saving session: {e}\n")
            
    def get_session_file(self):
        """Get the path to the session file"""
        return Path(self.nvim.funcs.stdpath("data")) / "aider_session.json"
        
        # Initialize NeovimIO
        self.io = NeovimIO(self.nvim, buf)
        
        # Start Aider
        from aider.main import main
        self.coder = main(return_coder=True, input=self.io, output=self.io)

    @pynvim.command('AiderStop')
    def stop_aider(self):
        """Stop the Aider session"""
        if not self.io:
            self.nvim.err_write("No Aider session is running\n")
            return
            
        try:
            self.save_session()
            
            # Clean up buffers
            if self.io and self.io.buf:
                try:
                    buf_num = self.io.buf.number
                    if buf_num and self.nvim.buffers[buf_num] is self.io.buf:
                        self.nvim.command(f"bwipeout! {buf_num}")
                except:
                    try:
                        self.nvim.command("bdelete!")
                    except:
                        pass
                    
            self.io = None
            self.coder = None
            self.nvim.out_write("Aider session stopped and saved\n")
        except Exception as e:
            self.nvim.err_write(f"Error stopping session: {e}\n")

    @pynvim.command('AiderChat')
    def focus_chat(self):
        """Focus the Aider chat buffer"""
        if not self.io:
            self.nvim.err_write("No Aider session is running\n")
            return
        
        self.nvim.api.set_current_buf(self.io.buf)

    @pynvim.command('AiderCommit', nargs='*')
    def commit_changes(self, args):
        """Commit changes made by Aider"""
        if not self.coder:
            self.nvim.err_write("No Aider session is running\n")
            return
        
        message = " ".join(args) if args else None
        self.coder.commands.cmd_commit(message)

    @pynvim.command('AiderUndo')
    def undo_last_change(self):
        """Undo the last Aider change"""
        if not self.coder:
            self.nvim.err_write("No Aider session is running\n")
            return
        
        self.coder.commands.cmd_undo("")

    @pynvim.command('AiderAdd', nargs='+')
    def add_files(self, args):
        """Add files to the Aider session"""
        if not self.coder:
            self.nvim.err_write("No Aider session is running\n")
            return
        
        self.coder.commands.cmd_add(" ".join(args))

    @pynvim.command('AiderDrop', nargs='*')
    def drop_files(self, args):
        """Remove files from the Aider session"""
        if not self.coder:
            self.nvim.err_write("No Aider session is running\n")
            return
        
        self.coder.commands.cmd_drop(" ".join(args) if args else "")

    @pynvim.command('AiderDiff')
    def show_diff(self):
        """Show diff of changes since last message"""
        if not self.coder:
            self.nvim.err_write("No Aider session is running\n")
            return
        
        self.coder.commands.cmd_diff("")

    @pynvim.command('AiderMap')
    def show_repo_map(self):
        """Show repository map"""
        if not self.coder:
            self.nvim.err_write("No Aider session is running\n")
            return
        
        self.coder.commands.cmd_map("")

    @pynvim.command('AiderMapRefresh')
    def refresh_repo_map(self):
        """Refresh repository map"""
        if not self.coder:
            self.nvim.err_write("No Aider session is running\n")
            return
        
        self.coder.commands.cmd_map_refresh("")

    @pynvim.command('AiderSettings')
    def show_settings(self):
        """Show current Aider settings"""
        if not self.coder:
            self.nvim.err_write("No Aider session is running\n")
            return
        
        self.coder.commands.cmd_settings("")

    @pynvim.command('AiderHelp')
    def show_help(self):
        """Show Aider help"""
        if not self.coder:
            self.nvim.err_write("No Aider session is running\n")
            return
        
        self.coder.commands.cmd_help("")

    @pynvim.command('AiderAsk', nargs='*')
    def ask_question(self, args):
        """Ask a question without editing files"""
        if not self.coder:
            self.nvim.err_write("No Aider session is running\n")
            return
        
        self.coder.commands.cmd_ask(" ".join(args))

    @pynvim.command('AiderCode', nargs='*')
    def request_code(self, args):
        """Request code changes"""
        if not self.coder:
            self.nvim.err_write("No Aider session is running\n")
            return
        
        self.coder.commands.cmd_code(" ".join(args))

    @pynvim.command('AiderArchitect', nargs='*')
    def architect_mode(self, args):
        """Enter architect mode for high-level design"""
        if not self.coder:
            self.nvim.err_write("No Aider session is running\n")
            return
        
        self.coder.commands.cmd_architect(" ".join(args))

    @pynvim.command('AiderTokens')
    def show_tokens(self):
        """Show token usage"""
        if not self.coder:
            self.nvim.err_write("No Aider session is running\n")
            return
        
        self.coder.commands.cmd_tokens("")

    @pynvim.command('AiderClear')
    def clear_chat(self):
        """Clear chat history"""
        if not self.coder:
            self.nvim.err_write("No Aider session is running\n")
            return
        
        self.coder.commands.cmd_clear("")

    @pynvim.command('AiderReset')
    def reset_session(self):
        """Reset the Aider session"""
        if not self.coder:
            self.nvim.err_write("No Aider session is running\n")
            return
        
        self.coder.commands.cmd_reset("")

    @pynvim.command('AiderCopyContext')
    def copy_context(self):
        """Copy chat context to clipboard"""
        if not self.coder:
            self.nvim.err_write("No Aider session is running\n")
            return
        
        self.coder.commands.cmd_copy_context("")

    @pynvim.command('AiderToggleMultiline')
    def toggle_multiline(self):
        """Toggle multiline input mode"""
        if not self.io:
            self.nvim.err_write("No Aider session is running\n")
            return
        
        self.io.toggle_multiline_mode()
