import pynvim
from typing import Optional, List

from aider.io import InputOutput

class NeovimIO(InputOutput):
    def __init__(self, nvim: pynvim.Nvim, buf: pynvim.Buffer, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nvim = nvim
        self.buf = buf
        self.setup_highlighting()

    def setup_highlighting(self):
        """Setup syntax highlighting for Neovim buffers"""
        self.nvim.command("set filetype=markdown")
        self.nvim.command("syntax enable")
        
    def update_status(self, status):
        """Update the status line with Aider's state"""
        self.nvim.command(f"let g:aider_status = '{status}'")
        self.nvim.command("redrawstatus")

    def tool_output(self, msg: str, log_only: bool = False):
        """Display tool output in Neovim buffer"""
        if log_only:
            return
            
        lines = msg.splitlines()
        self.buf.append(lines)
        self.nvim.command("normal G")  # Scroll to bottom

    def tool_error(self, msg: str):
        """Display error message in Neovim buffer"""
        self.nvim.err_write(msg + "\n")

    def tool_warning(self, msg: str):
        """Display warning message in Neovim buffer"""
        self.nvim.out_write(f"Warning: {msg}\n")

    def get_input(self, *args, **kwargs) -> str:
        """Get input from Neovim command line"""
        return self.nvim.call("input", "Aider> ")

    def assistant_output(self, message: str, pretty: Optional[bool] = None):
        """Display assistant output in Neovim buffer"""
        self.buf.append(message.splitlines())
        self.nvim.command("normal G")  # Scroll to bottom

    def toggle_multiline_mode(self):
        """Toggle multiline input mode"""
        super().toggle_multiline_mode()
        if self.multiline_mode:
            self.nvim.out_write("Multiline mode enabled\n")
        else:
            self.nvim.out_write("Multiline mode disabled\n")
