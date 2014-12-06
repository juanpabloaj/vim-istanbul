" File: istanbul.vim
" Author: Juanpabloaj <jpabloaj@gmail.com>
" Description: Get info from coverage istanbul json file.
" Last Modified: diciembre 05, 2014
"
if exists('g:loaded_istanbul')
    finish
endif

let loaded_istanbul = 1

command! -nargs=0 IstanbulShow call istanbul#IstanbulShow()
command! -nargs=0 IstanbulHide call istanbul#IstanbulHide()
