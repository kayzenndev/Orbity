import time
import importlib
import sys
from functions import clear_screen, loadinganm, mensagemend, mensagemvoltar

def asciiart():
    asciiart = r"""
         
 ██████╗ ██████╗ ██████╗ ██╗████████╗██╗   ██╗
██╔═══██╗██╔══██╗██╔══██╗██║╚══██╔══╝╚██╗ ██╔╝
██║   ██║██████╔╝██████╔╝██║   ██║    ╚████╔╝ 
██║   ██║██╔══██╗██╔══██╗██║   ██║     ╚██╔╝  
╚██████╔╝██║  ██║██████╔╝██║   ██║      ██║   
 ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝   ╚═╝      ╚═╝   
                                              
    ORBITY - v1.0.0.1
    Author: kayzenndev        
""" 
    return asciiart

#Função para mostrar o cabeçalho do menu
def header():

    asciiart = ascii()

    options1 = f"""
\033[38;5;208m[\033[97m01\033[38;5;208m]\033[0m \033[38;2;64;224;208m- Mais sobre o projeto
\033[38;5;208m[\033[97m02\033[38;5;208m]\033[0m \033[38;2;64;224;208m- Ver avisos importantes
\033[38;5;208m[\033[97m03\033[38;5;208m]\033[0m \033[38;2;64;224;208m- Manual de instruções
\033[38;5;208m[\033[97m04\033[38;5;208m]\033[0m \033[38;2;64;224;208m- Inciar programa
\033[38;5;208m[\033[97m00\033[38;5;208m]\033[0m \033[38;2;64;224;208m- Sair
"""

    print(f"\033[38;5;208m{asciiart}\033[0m")  
    print(options1)  

#Counter
keyback = [0]
key = 1
index = 0

#Loop
while key > keyback[index]:
    clear_screen()

    header()

    try:
        pergunta = int(input('\033[38;2;64;224;208mPor favor, selecione uma opção: \033[0m').strip())
        print(' ')

        loadinganm()
        clear_screen()

        if pergunta == 1:
            with open('docs/aboutproject.txt', 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()
                print(conteudo)
            
            mensagemvoltar()
            loadinganm()
            clear_screen()


        elif pergunta == 2:
            with open('docs/notices.txt', 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()
                print(conteudo)

            mensagemvoltar()
            loadinganm()
            clear_screen()

        elif pergunta == 3:
            with open('docs/manual.txt', 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()
                print(conteudo)

            mensagemvoltar()
            loadinganm()
            clear_screen()

        elif pergunta == 4:
            if 'src.menu' in sys.modules:
                importlib.reload(menu)
            else:
                from src import menu


        elif pergunta == 0:
            mensagemend()
            clear_screen()
            keyback.append(key)
            index += 1

        else:
            print('')
            print('\033[38;2;255;20;147mValor inválido, tente novamente.\033[0m')
            print('')
            loadinganm()
            clear_screen()
            continue

    except ValueError:
        print('')
        print('\033[38;2;255;20;147mValor inválido, tente novamente.\033[0m')
        print('')
        loadinganm()
        clear_screen()