import math
import matplotlib.pyplot as plt
from functions import loadingcalc, clear_screen, loading

def asciiart ():
    asciarty = r"""                                                   
▄████▄ ▄▄▄▄  ▄▄▄▄  ▄▄ ▄▄▄▄▄▄ ▄▄ ▄▄     █████▄  ██ ▄█▀ ██  ██ 
██  ██ ██▄█▄ ██▄██ ██   ██   ▀███▀     ██▄▄██▄ ████   ▀█████ 
▀████▀ ██ ██ ██▄█▀ ██   ██     █       ██   ██ ██ ▀█▄     ██ 
                                                             
    By KAYZENDEV
    V 1.0.0.1

"""
    return asciarty

def header():
    asciarty = asciiart()

    print(f"\033[38;5;208m{asciarty}\033[0m")
    print(f"\033[94m[!] - Bem-vindo ao Orbity RK4! \033[0m")
    print('\n')


chave = 1
counter = 0

while chave > counter:

    try:
        # ! Calculo do arrasto

        def calc_arrasto(rho, cd, area, velocidade):
            return 0.5 * rho * cd * area * velocidade**2

        # ! Equações do Movimento

        def derivadas(estado, massa, cd, area):
            x, y, vx, vy = estado

            velocidade = math.sqrt(vx**2 + vy**2)

            rho = 1.225

            fd = calc_arrasto(
                rho,
                cd,
                area,
                velocidade
            )

            if velocidade != 0:
                fx_arrasto = -fd * (vx / velocidade)
                fy_arrasto = -fd * (vy / velocidade)
            else:
                fx_arrasto = 0
                fy_arrasto = 0

            fx = fx_arrasto
            fy = fy_arrasto - massa * 9.81

            ax = fx / massa
            ay = fy / massa

            return [
                vx,
                vy,
                ax,
                ay
            ]

        # ! Runge-Kutta 4ª Ordem

        def rk4(estado, dt, massa, cd, area):

            k1 = derivadas(
                estado,
                massa,
                cd,
                area
            )

            estado2 = [
                estado[i] + k1[i] * dt/2
                for i in range(4)
            ]

            k2 = derivadas(
                estado2,
                massa,
                cd,
                area
            )

            estado3 = [
                estado[i] + k2[i] * dt/2
                for i in range(4)
            ]

            k3 = derivadas(
                estado3,
                massa,
                cd,
                area
            )

            estado4 = [
                estado[i] + k3[i] * dt
                for i in range(4)
            ]

            k4 = derivadas(
                estado4,
                massa,
                cd,
                area
            )

            novo_estado = []

            for i in range(4):
                valor = estado[i] + (dt/6) * (
                    k1[i]
                    + 2*k2[i]
                    + 2*k3[i]
                    + k4[i]
                )

                novo_estado.append(valor)

            return novo_estado

        massa = float(input('\033[38;5;208mDigite a massa do foguete em kilogramas (kg) >>> \033[0m'))
        diametro = float(input('\033[38;5;208mDigite o diâmetro do foguete em metros (m) >>> \033[0m'))
        cd = float(input('\033[38;5;208mDigite o coeficiente de arrasto CD >>> \033[0m'))
        velocidade_inicial = float(input('\033[38;5;208mDigite a velocidade inicial do foguete em metros por segundo (m/s) >>> \033[0m'))
        angulo = float(input('\033[38;5;208mDigite o ângulo de lancamento do foguete (graus) >>> \033[0m'))

        # ! Calculos iniciais

        raio = diametro / 2
        area = math.pi * raio**2

        vx = velocidade_inicial * math.cos(
            math.radians(angulo)
        )

        vy = velocidade_inicial * math.sin(
            math.radians(angulo)
        )

        estado = [
            0,
            0,
            vx,
            vy
        ]


        dt = 0.01
        tempo = 0

        altura_maxima = 0

        x_lista = []
        y_lista = []

        while estado[1] >= 0:
            
            estado = rk4(
                estado,
                dt,
                massa,
                cd,
                area
            )

            tempo += dt

            x_lista.append(estado[0])
            y_lista.append(estado[1])

            if estado[1] > altura_maxima:
                altura_maxima = estado[1]

        print('\n')
        loadingcalc()

        print(f'\033[38;5;208mTempo de voo do foguete (s) >>> {tempo:.2f} segundos.\033[0m')
        print(f'\033[38;5;208mAlcance horizontal (m) >>> {estado[0]:.2f} metros.\033[0m')
        print(f'\033[38;5;208mAltura máxima (m) >>> {altura_maxima:.2f} metros.\033[0m')

        print('\n')

        x = input(f'\033[38;5;208mAperte enter para ver o gráfico >>> \033[0m')

        plt.figure(figsize=(10,5))


        plt.plot(
            x_lista,
            y_lista,
            label="Trajetória"
        )


        plt.scatter(
            [0],
            [0],
            label="Lançamento"
        )


        plt.scatter(
            [estado[0]],
            [0],
            label="Impacto"
        )



        plt.title(
            "Trajetória do foguete usando RK4"
        )


        plt.xlabel(
            "Distância horizontal (m)"
        )


        plt.ylabel(
            "Altura (m)"
        )


        plt.grid()

        plt.legend()


        plt.axis("equal")


        plt.show()

        print(' ')
        
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