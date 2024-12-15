set clipboard=unnamedplus

call plug#begin()
"Plug 'tpope/vim-surround'
Plug 'tmsvg/pear-tree'                             " For easy pairs of quotation marks, parens, etc

Plug 'wellle/context.vim', {'on': []}

Plug 'morhetz/gruvbox'

Plug 'sirver/ultisnips'
    let g:UltiSnipsExpandTrigger       = '<tab>'   " Tab to expand snippets
    let g:UltiSnipsJumpForwardTrigger  = '<tab>'   " Tab to move fwd thru tabstops
    let g:UltiSnipsJumpBackwardTrigger = '<s-tab>' " Shift-Tab to move back thru tabstops
    let g:UltiSnipsUseSystemSnippets = 0
    let g:UltiSnipsEnablePseudoSnippets = 1
    let g:UltiSnipsOptions = 'i'
    let g:UltiSnipsSnippetDirectories=[$HOME.'/.config/nvim/UltiSnips']


Plug 'lervag/vimtex', {'on': []}
    "let g:tex_flavor='latex'
    "let g:vimtex_view_method='zathura'
    "let g:vimtex_quickfix_mode=0

Plug 'KeitaNakamura/tex-conceal.vim', {'on': []}
"    set conceallevel=1
"    let g:tex_conceal='abdmg'
"    hi Conceal ctermbg=none

call plug#end()

setlocal spell
set spelllang=en_us
set cursorline
colo gruvbox

function! Toggle_Light_Dark_Colorscheme()
  if &background == 'light'
    set background=dark
    echo "Background -> dark"
  else
    set background=light
    echo "Background -> light"
  endif
endfunction

" Toggle dark/light mode
nnoremap <F6> :call Toggle_Light_Dark_Colorscheme() " no workie ?? :((

" Refresh snippets
inoremap <F2> :call UltiSnips#RefreshSnippets() 

nnoremap <F9> :latexmk -pdf %

" Custom commands per filetype
autocmd FileType tex setlocal nowrap
