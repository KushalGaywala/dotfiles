vim.keymap.set("n", "<A-H>", require("smart-splits").resize_left)
vim.keymap.set("n", "<A-J>", require("smart-splits").resize_down)
vim.keymap.set("n", "<A-K>", require("smart-splits").resize_up)
vim.keymap.set("n", "<A-L>", require("smart-splits").resize_right)
vim.keymap.set("n", "<A-h>", require("smart-splits").move_cursor_left)
vim.keymap.set("n", "<A-j>", require("smart-splits").move_cursor_down)
vim.keymap.set("n", "<A-k>", require("smart-splits").move_cursor_up)
vim.keymap.set("n", "<A-l>", require("smart-splits").move_cursor_right)
vim.keymap.set("n", "<A-\\>", require("smart-splits").move_cursor_previous)

vim.keymap.set("n", "<C-left>", "")
vim.keymap.set("n", "<C-down>", "")
vim.keymap.set("n", "<C-up>", "")
vim.keymap.set("n", "<C-right>", "")
vim.keymap.set("n", "<C-h>", "")
vim.keymap.set("n", "<C-j>", "")
vim.keymap.set("n", "<C-k>", "")
vim.keymap.set("n", "<C-l>", "")
vim.keymap.set("n", "<C-\\>", "")

local config = require "smart-splits.config"
config.default_amount = 1
