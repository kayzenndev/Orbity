from functions import clear_screen, loadinganm, mensagemend, mensagemvoltar, header

try:
    import importlib
    import sys
    from functions import clear_screen, loadinganm, mensagemend, mensagemvoltar, header

    keyback = [0]
    key = 1
    index = 0

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
    
except ModuleNotFoundError, ImportError:
    print('')
    print('\033[38;2;255;20;147mOpa... Tem algo de errado com os módulos. Verifique a instalação correta dos requisitos ou abra um issue ná página do projeto.\033[0m')
    print('')
    loadinganm()
    clear_screen()