local M = {}

local function get_aider_plugin()
  local ok, plugin = pcall(vim.fn.pyeval, "vim.eval('g:aider_plugin')")
  if not ok or not plugin then
    vim.api.nvim_err_writeln("Aider plugin not initialized")
    return nil
  end
  return plugin
end

function M.start()
  local plugin = get_aider_plugin()
  if not plugin then return end
  
  plugin:start_aider()
end

function M.stop()
  local plugin = get_aider_plugin()
  if not plugin then return end
  
  -- Clean up any resources
  vim.schedule(function()
    -- Stop any running processes
    pcall(function() plugin:stop_aider() end)
    
    -- Clear any global state
    vim.g.aider_plugin = nil
    vim.g.aider_status = nil
    
    -- Force garbage collection
    collectgarbage("collect")
  end)
end

function M.focus_chat()
  local plugin = get_aider_plugin()
  if not plugin then return end
  
  plugin:focus_chat()
end

function M.show_diff()
  local plugin = get_aider_plugin()
  if not plugin then return end
  
  plugin:show_diff()
end

function M.undo_last_change()
  local plugin = get_aider_plugin()
  if not plugin then return end
  
  plugin:undo_last_change()
end

function M.show_repo_map()
  local plugin = get_aider_plugin()
  if not plugin then return end
  
  plugin:show_repo_map()
end

function M.show_settings()
  local plugin = get_aider_plugin()
  if not plugin then return end
  
  plugin:show_settings()
end

function M.show_help()
  local plugin = get_aider_plugin()
  if not plugin then return end
  
  plugin:show_help()
end

function M.toggle_multiline()
  local plugin = get_aider_plugin()
  if not plugin then return end
  
  plugin:toggle_multiline()
end

return M
