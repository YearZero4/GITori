import os, requests, sys, time, pyfiglet
from colorama import Fore, Style, init
from bs4 import BeautifulSoup as b
init(autoreset=True)
green=f'{Fore.GREEN}{Style.BRIGHT}'
white=f'{Fore.WHITE}{Style.BRIGHT}'
red=f'{Fore.RED}{Style.BRIGHT}'
reset=f'{Style.RESET_ALL}'
folders=['datos', 'datos/usuarios', 'datos/repositorios_clonados']
root='https://github.com'
zip1='archive/refs/heads/'
div='=======' ; n=1

def clear():
 so=os.name
 if so == 'nt':
  os.system('cls')
 else:
  os.system('clear')

clear()

for i in folders:
  if not os.path.exists(i):
   os.makedirs(i)
def sn():
 yn=input("\nDESEAS SALIR [S/N]? -> ")
 if yn == 'S' or yn == 's':
  print(f"\n{white}Hasta Luego{green}...")
  time.sleep(2)
  sys.exit()
 elif yn == 'N' or yn == 'n':
  print("REINICIAR PROGRAMA")
  input()

users=os.listdir('datos/usuarios')
usk=[]
for i in users:
 usk.append(i)
e='           '
print('''
     ____ ___ _____
    / ___|_ _|_   _|__  _ __ _   _
   | |  _ | |  | |/ _ /| '__| | | |
   | |_| || |  | | (_) | |  | |_| |
    /____|___| |_|/___/|_|   /__, |
                             |___/''')

print(f'''
{green}[1]{white} Descargar repositorio copiando URL
{green}[2]{white} Especificar {green}USUARIO{white} del REPOSITORIO
{green}[3]{white} Ver USUARIOS buscados anteriormente
{green}[0]{white} Salir del Script
''')
nn=1
opc=int(input('----> '))
print("")

def descargar_repositorio(url):
 ruta=f'datos/repositorios_clonados/{user}'
 if not os.path.exists(ruta):
  os.makedirs(ruta)
 nrepo=ruta + '/' + url.split('/')[-1] + '.zip'
 name0=url.split('/')[-1]
 p=requests.get(url)
 soup=b(p.content, 'html.parser')
 buscar = soup.find_all('span', class_='Text__StyledText-sc-17v1xeu-0 eMMFM')
 for i in buscar:
  result = i.get_text(strip=True)
  zipx=f'{url}/{zip1}{result}.zip'
  r=requests.get(zipx)
  with open(nrepo, 'wb') as f:
   f.write(r.content)
   f.close()
  if os.path.exists(nrepo):
   print(f"{green}REPOSITORIO -> {name0}{white} DESCARGADO" )
  else:
   print(f"{red}Error en {white}{name0}")


def drxurl(url):
 user=url.split('/')[3]
 ruta=f'datos/repositorios_clonados/{user}'
 if not os.path.exists(ruta):
  os.makedirs(ruta)
 repo=url.split('/')[-1]
 nsave=f"{ruta}/{repo}.zip"
 zip1='archive/refs/heads/'
 p=requests.get(url)
 soup=b(p.content, 'html.parser')
 buscar = soup.find_all('span', class_='Text__StyledText-sc-17v1xeu-0 eMMFM')
 for i in buscar:
  result = i.get_text(strip=True)
  zipx=f'{url}/{zip1}{result}.zip'
  r=requests.get(zipx)
  with open(nsave, 'wb') as f:
   f.write(r.content)
   f.close()
  if os.path.exists(nsave):
   print(f"{green}REPOSITORIO -> {repo}{white} DESCARGADO" )
  else:
   print(f"{red}Error en {white}{repo}")


if opc == 1:
 print(f'{white}EJEMPLO : {reset}https://github.com/soydalto/Google-Maps-API')
 url_rpp=input("\nIntroduzca la URL del Repositorio -> ")
 drxurl(url_rpp)
 sn()

elif opc == 2:
 print(f'{white}EJEMPLO : {reset}YearZero4')
 user=input("Nombre de usuario -> ")
 rx=f'datos/usuarios/{user}'
 if not os.path.exists(rx):
  with open(rx, 'w') as f:
   f.write('')
   f.close()

elif opc == 3:
 for i in users:
  print(f"{white}[{nn}] {green}{i}")
  nn=nn+1
 sn()

elif opc == 0:
 clear()
 sys.exit()

else:
 print('Opcion Invalida...')
 sys.exit()

repositorios=f'https://github.com/{user}?tab=repositories'
r=requests.get(repositorios)
soup=b(r.content, 'html.parser')
buscar=soup.find_all('a', itemprop="name codeRepository")
url_repository=[]
for i in buscar:
 url=root + i['href']
 url_repository.append(url)
nrepos=len(url_repository)

print(f"\n{green}USUARIO DEL REPOSITORIO -> {white}{user}\n{green}Cantidad de repositorios -> {white}{nrepos}\n")
print(f"\nREPOSITORIOS MAS RECIENTE\n")


for i in url_repository:
 if n <= 3:
  print(f"{green}[{n}] {white}{i}")
  n=n+1
n=1
print("\nREPOSITORIOS MAS ANTIGUOS\n")
for i in url_repository:
 if n > 3:
  print(f"{green}[{n}] {white}{i}")
 n=n+1
print(f"""
{white}[1]{green} Descargar un repositorio
{white}[2]{green} Descargar todos los repositorios
{white}[0]{green} Salir Del Script
""")
opcion=int(input("Opcion Numero -> "))

if opcion == 1:
 numero=int(input("\nIntroduzca el Numero del repositorio -> "))
 numero=numero-1
 repositorio=url_repository[numero]
 descargar_repositorio(repositorio)
elif opcion == 2:
 for i in url_repository:
  descargar_repositorio(i)
elif opcion == 0:
 clear()
 sys.exit()
input("\nACABA DE FINALIZAR EL SCRIPT")
