" to load json generate from : istabul report

if !has('python')
    echohl WarningMsg|echomsg "python interface to vim not found."
    finish
endif

if !exists('g:coverage_json_path')
    let json_path=getcwd().'/coverage/coverage.json'
    if filereadable(json_path)
        let g:coverage_json_path=json_path
    else
        echohl WarningMsg|echomsg "coverage.json file not found."
        finish
    end
end

let s:plugin_path = escape(expand('<sfile>:p:h'), '\')

function! s:ClearSigns() abort
    exe ":sign unplace *"
endfunction

function! s:SetHighlight()
    hi clear SignColumn
    hi link SignColumn Normal
    hi uncovered guifg=#fc8c84 guibg=#fc8c84 ctermfg=196 ctermbg=196
    hi fstatno guifg=#ffc520 guibg=#ffc520  ctermfg=208 ctermbg=208
    hi covered guifg=#004400 guibg=green ctermfg=40 ctermbg=40
    hi branch_true guifg=black guibg=yellow ctermfg=16 ctermbg=226
    hi branch_false guifg=black guibg=yellow ctermfg=16 ctermbg=226
    sign define uncovered text=XX texthl=uncovered
    sign define fstatno text=XX texthl=fstatno
    sign define covered text=XX texthl=covered
    sign define branch_true text=IF texthl=branch_true
    sign define branch_false text=EL texthl=branch_false
endfunction

fun! s:istanbulShow() "{{{
    call s:SetHighlight()
    " if report not exists : istabul report
    exe 'py g_coverage_json_path = "' . g:coverage_json_path . '"'
    exe 'pyfile ' . s:plugin_path . '/istanbul.py'
    python sign_covered_lines()
endf "}}}

fun! istanbul#IstanbulShow() "{{{
    call s:istanbulShow()
endf "}}}

fun! istanbul#IstanbulHide() "{{{
    call s:ClearSigns()
endf "}}}
