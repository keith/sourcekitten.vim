# sourcekitten.vim

This is an experimental vim plugin which uses
[sourcekitten](https://github.com/jpsim/sourcekitten) to live highlight
swift code.

## Issues

- It's horribly slow. This could possible be resolved by moving from
  byte movements to calculating line number and positions in python
- `matchaddpos()` conflicts with `cursorline` in vim. I can't find
  anything on this but I believe it's a bug in vim.
- It will never be fast with a single process. Using
  [neovim](https://github.com/neovim/neovim) makes this better.
- It doesn't currently highlight until you make changes
- It doesn't handle indentation
