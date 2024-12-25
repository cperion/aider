import pynvim
from neovim_io import NeovimIO

@pynvim.plugin
class AiderPlugin:
    def __init__(self, nvim):
        self.nvim = nvim
        self.io = None
        self.coder = None

    @pynvim.command('Aider', nargs='*', range='')
    def start_aider(self, args, range):
        """Start an Aider session in Neovim"""
        if self.io:
            self.nvim.err_write("Aider is already running\n")
            return

        # Create a new buffer for the chat
        buf = self.nvim.api.create_buf(False, True)
        self.nvim.api.set_current_buf(buf)
        
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
        
        self.io = None
        self.coder = None
        self.nvim.out_write("Aider session stopped\n")

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
