import numpy as np
import matplotlib.pyplot as plt
import math

from functions import loading, loadingcalc, clear_screen, ascii

def header():
    asciiart = ascii()

    options1 = r"""
[!] - Bem-vindo ao módulo 12: Gŕafico da equação geral do lançamento.
"""

    print(f"\033[38;5;208m{asciiart}\033[0m")
    print(f"\033[94m{options1}\033[0m")

chave = 1
counter = 0

while chave > counter:
    try:
        print(' ')
        header()

        v = float(input('\033[38;5;208mDigite o volume em metros cúbicos (m³) >>> \033[0m'))
        m = float(input('\033[38;5;208mDigite a massa do foguete em kilogramas (kg) >>> \033[0m'))
        n = float(input('\033[38;5;208mDigite o rendimento (Ex: 0.10) >>> \033[0m'))
        tet = float(input('\033[38;5;208mDigite o ângulo da base de lançamento (graus) >>> \033[0m'))
        p1 = float(input('\033[38;5;208mDigite a pressão inicial (Pa) >>> \033[0m'))

        g = 9.81
        p2 = 101325

        v0 = math.sqrt((5 * v * n * (p1 - p2)) / m)

        theta = math.radians(tet)
        alcance = (v0**2 * math.sin(2 * theta)) / g

        theta = np.radians(tet)

        x = np.linspace(0, alcance, 200)

        y = (x * np.tan(theta) - (g * x**2) / (2 * v0**2 * np.cos(theta)**2))


        plt.plot(x, y, label='Trajetória do Lançamento', linewidth=2, color='black')
        plt.title('Gráfico do lançamento oblíquo.')
        plt.legend()
        plt.xlabel('Distância Horizontal (m)')
        plt.ylabel('Altura (m)')
        plt.grid(True, linestyle='-.')
        plt.tight_layout()
        plt.show()

        print(''' 
''')

        inicializar = input('\033[94mDeseja utilizar o programa novamente ? [Y/N] >>> \033[0m').strip().upper()
        print(' ')
        if inicializar[0] == 'Y':
            counter = 0
            clear_screen()
                    
        elif inicializar[0] == 'N':
            loading()
            counter += 1
            clear_screen()

        else: 
            print('')
            print('\033[38;2;255;20;147mValor inválido, tente novamente.\033[0m')
            print('')
            loading()
            counter = 0
            clear_screen()
    

    except ValueError:
        print('')
        print('\033[38;2;255;20;147mValor inválido, tente novamente.\033[0m')
        print('')
        loading()
        counter = 0
        clear_screen()
    
    except ZeroDivisionError:
        print('')
        print('\033[38;2;255;20;147mNão é possível dividir por zero, tente novamente.\033[0m')
        print('')
        loading()
        counter = 0
        clear_screen()