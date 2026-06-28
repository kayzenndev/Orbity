import sys
import time

#Função limpa terminal
def clear_screen():
    from os import system
    import platform
    if platform.system() == 'Windows':
        system('cls')
    else:
        system('clear')

#Função animação de carregamento 
def loadinganm():
    AZUL = '\033[94m'                      
    ROSA_VIBRANTE = '\033[38;2;255;20;147m' 
    NEGRITO = '\033[1m'                    
    RESET = '\033[0m'                      

    animation = ["\\", "|", "/", "-"]
    msg = "Loading code..."

    for _ in range(3):
        for i in range(len(animation)):
            time.sleep(0.2)
            
            sys.stdout.write(f"\r{AZUL}{msg}{RESET} {NEGRITO}{ROSA_VIBRANTE}{animation[i % len(animation)]}{RESET}")
            sys.stdout.flush()

#Carregamento de saída
def loadinganmexit():
    AZUL = '\033[94m'                      
    ROSA_VIBRANTE = '\033[38;2;255;20;147m' 
    NEGRITO = '\033[1m'                    
    RESET = '\033[0m'                      

    animation = ["\\", "|", "/", "-"]
    msg = "Exiting..."

    for _ in range(3):
        for i in range(len(animation)):
            time.sleep(0.2)
            
            sys.stdout.write(f"\r{AZUL}{msg}{RESET} {NEGRITO}{ROSA_VIBRANTE}{animation[i % len(animation)]}{RESET}")
            sys.stdout.flush()

#Mensagem de retorno
def mensagemvoltar():
    print('\033[38;2;64;224;208mPress the Y key to return to the menu.\033[0m')
    print('\033[38;2;64;224;208mPressione a tecla Y para retornar ao menu.\033[0m')

    back = input('\033[38;5;208m>>>\033[0m').strip().lower()

    print(' ')
    return back

#Mensagem de leaving
def mensagemend():
    print('\033[38;2;64;224;208mYou chose to leave the program! Thanks for using. :)\033[0m')

    print(' ')

    loadinganmexit()

#Mensagem calculando
def loadingcalc():
    AZUL = '\033[94m'                      
    ROSA_VIBRANTE = '\033[38;2;255;20;147m' 
    NEGRITO = '\033[1m'                    
    RESET = '\033[0m'                      

    animation = ["\\", "|", "/", "-"]
    msg = "Calculating... "

    for _ in range(3):
        for i in range(len(animation)):
            time.sleep(0.2)
            
            sys.stdout.write(f"\r{AZUL}{msg}{RESET} {NEGRITO}{ROSA_VIBRANTE}{animation[i % len(animation)]}{RESET}")
            sys.stdout.flush()

#Carregamento
def loading():
    AZUL = '\033[94m'                      
    ROSA_VIBRANTE = '\033[38;2;255;20;147m' 
    NEGRITO = '\033[1m'                    
    RESET = '\033[0m'                      

    animation = ["\\", "|", "/", "-"]
    msg = "Loading ... "

    for _ in range(3):
        for i in range(len(animation)):
            time.sleep(0.2)
            
            sys.stdout.write(f"\r{AZUL}{msg}{RESET} {NEGRITO}{ROSA_VIBRANTE}{animation[i % len(animation)]}{RESET}")
            sys.stdout.flush()

#Função que retorna a asciiart
def ascii():
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

#Função para mostrar o cabeçalho do arquivo main
def header():
    asciiart = ascii()

    options1 = f"""
\033[38;5;208m[\033[97m01\033[38;5;208m]\033[0m \033[38;2;64;224;208m- Mais sobre o projeto
\033[38;5;208m[\033[97m02\033[38;5;208m]\033[0m \033[38;2;64;224;208m- Ver avisos importantes
\033[38;5;208m[\033[97m03\033[38;5;208m]\033[0m \033[38;2;64;224;208m- Manual de instruções
\033[38;5;208m[\033[97m04\033[38;5;208m]\033[0m \033[38;2;64;224;208m- Orbity Based on Classic Physis 
\033[38;5;208m[\033[97m05\033[38;5;208m]\033[0m \033[38;2;64;224;208m- Orbity with Runge-Kutta
\033[38;5;208m[\033[97m00\033[38;5;208m]\033[0m \033[38;2;64;224;208m- Sair
"""

    print(f"\033[38;5;208m{asciiart}\033[0m")  
    print(options1)  

#Função para mostrar o cabeçalho do menu
def headermenu():
    asciiart = ascii()

    options1 = f"""
\033[38;5;208m[\033[97m01\033[38;5;208m]\033[0m \033[38;2;64;224;208m- Calcular o trabalho realizado pelo gás dentro da base.
\033[38;5;208m[\033[97m02\033[38;5;208m]\033[0m \033[38;2;64;224;208m- Calcular alcance do foguete.
\033[38;5;208m[\033[97m03\033[38;5;208m]\033[0m \033[38;2;64;224;208m- Calcular a variação da energia interna do gás.
\033[38;5;208m[\033[97m04\033[38;5;208m]\033[0m \033[38;2;64;224;208m- Calcular a velocidade do foguete em função de W.
\033[38;5;208m[\033[97m05\033[38;5;208m]\033[0m \033[38;2;64;224;208m- Calcular a velocidade do foguete em função de ΔU.
\033[38;5;208m[\033[97m06\033[38;5;208m]\033[0m \033[38;2;64;224;208m- Calcular a valocidade (para facilitar o cálculo do rendimento).
\033[38;5;208m[\033[97m07\033[38;5;208m]\033[0m \033[38;2;64;224;208m- Calcular rendimento η.

\033[38;5;208m[\033[97m08\033[38;5;208m]\033[0m \033[38;2;64;224;208m- Gerar gráfico do Alcance x Pressão Final.
\033[38;5;208m[\033[97m09\033[38;5;208m]\033[0m \033[38;2;64;224;208m- Gerar gráfico do Alcance x Rendimento.
\033[38;5;208m[\033[97m10\033[38;5;208m]\033[0m \033[38;2;64;224;208m- Gerar gráfico de V0x x Tempo.
\033[38;5;208m[\033[97m11\033[38;5;208m]\033[0m \033[38;2;64;224;208m- Gerar gráfico de V0y x Tempo.
\033[38;5;208m[\033[97m00\033[38;5;208m]\033[0m \033[38;2;64;224;208m- Encerrar programa.
"""

    print(f"\033[38;5;208m{asciiart}\033[0m")
    print(options1)