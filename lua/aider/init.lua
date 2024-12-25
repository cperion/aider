local M = {}

local function setup(config)
  config = config or {}
  
  -- Ensure required dependencies
  local ok, core = pcall(require, 'aider.core')
  if not ok then
    vim.notify('Failed to load aider.core: ' .. core, vim.log.levels.ERROR)
    return
  end
  
  -- Set up keybindings
  vim.api.nvim_set_keymap('n', '<leader>aa', ':Aider<CR>', {noremap = true, silent = true})
  vim.api.nvim_set_keymap('n', '<leader>ac', ':AiderChat<CR>', {noremap = true, silent = true})
  vim.api.nvim_set_keymap('n', '<leader>ad', ':AiderDiff<CR>', {noremap = true, silent = true})
  vim.api.nvim_set_keymap('n', '<leader>au', ':AiderUndo<CR>', {noremap = true, silent = true})
  vim.api.nvim_set_keymap('n', '<leader>am', ':AiderMap<CR>', {noremap = true, silent = true})
  vim.api.nvim_set_keymap('n', '<leader>as', ':AiderSettings<CR>', {noremap = true, silent = true})
  vim.api.nvim_set_keymap('n', '<leader>ah', ':AiderHelp<CR>', {noremap = true, silent = true})
  vim.api.nvim_set_keymap('n', '<leader>at', ':AiderToggleMultiline<CR>', {noremap = true, silent = true})

  -- Set up commands
  vim.cmd([[command! Aider lua require('aider').start()]])
  vim.cmd([[command! AiderChat lua require('aider').focus_chat()]])
  vim.cmd([[command! AiderDiff lua require('aider').show_diff()]])
  vim.cmd([[command! AiderUndo lua require('aider').undo_last_change()]])
  vim.cmd([[command! AiderMap lua require('aider').show_repo_map()]])
  vim.cmd([[command! AiderSettings lua require('aider').show_settings()]])
  vim.cmd([[command! AiderHelp lua require('aider').show_help()]])
  vim.cmd([[command! AiderToggleMultiline lua require('aider').toggle_multiline()]])

  -- Set up autocommands
  vim.cmd([[
    augroup Aider
      autocmd!
      autocmd VimLeave * lua require('aider').stop()
    augroup END
  ]])
end

function M.start()
  require('aider.core').start()
end

function M.stop()
  require('aider.core').stop()
end

function M.focus_chat()
  require('aider.core').focus_chat()
end

function M.show_diff()
  require('aider.core').show_diff()
end

function M.undo_last_change()
  require('aider.core').undo_last_change()
end

function M.show_repo_map()
  require('aider.core').show_repo_map()
end

function M.show_settings()
  require('aider.core').show_settings()
end

function M.show_help()
  require('aider.core').show_help()
end

function M.toggle_multiline()
  require('aider.core').toggle_multiline()
end

M.setup = setup

return M
