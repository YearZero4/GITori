RED="\033[1;31m"
GREEN="\033[1;32m"
WHITE="\033[1;37m"
clear
find datos/repositorios_clonados/ -maxdepth 2 -name '*.zip' | grep '.zip$' | while read z;do
dir="${z%/*}"
nzip="${z##*/}"
unzip "$z" -d "$dir" 2>/dev/null >/dev/null
if [[ "$?" == 0 ]];then
echo -e "${WHITE}[*] ${GREEN}DESCOMPRIMIDO EXITOSAMENTE -> ${WHITE}(${nzip})"
rm "$z"
else
echo -e "${WHITE}[*] ${RED}ERROR AL DESCOMPRIMIR -> ${WHITE}(${nzip})"
fi
done
