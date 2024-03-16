PYENV="$(cat ~/.config/.currpyenv)"

PROMPT='%{$FG[027]%}env:(%{$FG[226]%}$PYENV%{$FG[027]%})'
PROMPT+=' %{$FG[213]%}cwd:(%{$FG[225]%}%c%{$FG[213]%})'
PROMPT+=' $(git_prompt_info)'
PROMPT+='
%(?:%{$FG[046]%}%1{➜%}:%{$FG[196]%}%1{➜%})'
PROMPT+='%{$reset_color%} '

ZSH_THEME_GIT_PROMPT_PREFIX="%{$FG[202]%}git:(%{$FG[216]%}"
ZSH_THEME_GIT_PROMPT_SUFFIX="%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_DIRTY="%{$FG[202]%}) %{$FG[20]%}%1{✗%}"
ZSH_THEME_GIT_PROMPT_CLEAN="%{$FG[202]%})"

