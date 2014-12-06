let s:scriptFolderPath = escape(expand('<sfile>:p:h'), '\')
py import sys
execute 'python sys.path += ["' . s:scriptFolderPath . '/../pythonx"]'
let s:parsePath = resolve(s:scriptFolderPath . "/../pythonx/parse.py")

function! swift#Go()
  execute 'pyfile ' . s:parsePath
endfunction
