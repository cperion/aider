from .main import main
import sys

def neovim_main():
    """Entry point for Neovim plugin"""
    from neovim_plugin import AiderPlugin
    return AiderPlugin

if __name__ == "__main__":
    if '--neovim' in sys.argv:
        # When running as a Neovim plugin, return the plugin class
        neovim_main()
    else:
        # Normal CLI mode
        main()
