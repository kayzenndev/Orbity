import time
from os import system
import importlib
import sys
from functions import clear_screen, mensagemend, loadinganmexit, loading, headermenurk

chaveanterior = [0]
chave = 1
index = 0

while chave > chaveanterior[index]:
    headermenurk()

    try:
        pergunta = int(input('\033[38;2;64;224;208mPor favor, selecione uma opção: \033[0m').strip())
        print(' ')

        clear_screen()

        if pergunta == 1:
            if 'src.runge_kutta.runge_kutta_method' in sys.modules:
                importlib.reload(runge_kutta_method)
            else:
                from src.runge_kutta import runge_kutta_method

        elif pergunta == 0:
            loadinganmexit()
            print('')
            clear_screen()
            break

        else:
            print('Número inválido, tente novamente.')
            print('Carregando...')
            time.sleep(1)
            system('cls')
            continue


        #Falta arrumar aqui---
        inicializar = input('\033[38;5;208mDeseja retornar ao menu principal? [Y/N] >>> \033[0m').upper().strip()

        if inicializar[0] == 'Y':
            chaveanterior.append(chave)
            chave += 1
            index += 1
            print('')
            loading()
            clear_screen()
        
        elif inicializar[0] == 'N':
            print('')
            mensagemend()
            clear_screen()
            break

    except ValueError:
        print('')
        print('\033[38;2;255;20;147mValor inválido, tente novamente.\033[0m')
        print('')
        loading()
        chaveanterior.append(chave)
        chave += 1
        index += 1
        clear_screen()


