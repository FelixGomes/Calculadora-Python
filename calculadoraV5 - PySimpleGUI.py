import PySimpleGUI as sg

# =======Funcao para computar a equacao da calculadora=======
def computa_equacao():
    try:
        global expressao
        total = str("%0.2f" % (eval(expressao)))
        janela.find_element('input').Update(total)
        expressao = total
    except:
        janela.find_element('input').Update('Erro!')
    finally:
        expressao = ""

# =======Funcao para limpar o ultimo digito do display (backspace)=======
def backspace():
    global expressao
    expressao = expressao[:-1]
    janela.find_element('input').Update(expressao)

# =======Predefinicoes de botao=======
wbt = {'size': (7, 2), 'font': ('Franklin Gothic Book', 12), 'button_color': ('black', '#F8F8F8')}
tbt = {'size': (7, 2), 'font': ('Franklin Gothic Book', 12), 'button_color': ('black', '#F1EABC')}
obt = {'size': (16, 2), 'font': ('Franklin Gothic Book', 12), 'button_color': ('black', '#ECA527'), 'focus': True}
# wbt = white button (botao brancos), tbt = tan button (botao bronze), obt = orange button (botao laranja)

# =======Layout para criacao do GUI=======
layout = [[sg.Txt ('Calculadora Simples', size=(38,1), justification='right')],
          [sg.Txt ('' * 10)],
          [sg.Txt ('', size= (15,1), font=('Helvetica', 18), key='input')],
          [sg.Txt ('' * 10)],
          [sg.ReadFormButton('C',**tbt), sg.ReadFormButton('CE',**tbt), sg.ReadFormButton('%',**tbt), sg.ReadFormButton('/',**tbt)],
          [sg.ReadFormButton('7',**wbt), sg.ReadFormButton('8',**wbt), sg.ReadFormButton('9',**wbt), sg.ReadFormButton('*',**tbt)],
          [sg.ReadFormButton('4',**wbt), sg.ReadFormButton('5',**wbt), sg.ReadFormButton('6',**wbt), sg.ReadFormButton('-',**tbt)],
          [sg.ReadFormButton('1',**wbt), sg.ReadFormButton('2',**wbt), sg.ReadFormButton('3',**wbt), sg.ReadFormButton('+',**tbt)],
          [sg.ReadFormButton('0',**wbt), sg.ReadFormButton('.',**wbt), sg.ReadFormButton('=',**obt, bind_return_key=True)]
          ]

# =======Criacao da janela=======
janela = sg.FlexForm('Calculadora', default_button_element_size=(5,2), auto_size_buttons=False, grab_anywhere=True, return_keyboard_events=True)
janela.Layout(layout)

# =======String que conterá a equacao a ser avaliada na funcao=======
expressao = ""

# =======Loop infinito para rodar o GUI (apenas python 3.10 ou superior)=======
while True:
    botao, valor = janela.Read()
    if botao is None:
        break
    if botao in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        expressao += botao
        janela.find_element('input').Update(expressao)
    match botao:
        case '+':
            expressao += '+'
            janela.find_element('input').Update(expressao)
        case '-':
            expressao += '-'
            janela.find_element('input').Update(expressao)
        case '*':
            expressao += '*'
            janela.find_element('input').Update(expressao)
        case '/':
            expressao += '/'
            janela.find_element('input').Update(expressao)
        case '.':
            expressao += '.'
            janela.find_element('input').Update(expressao)
        case '%':
            expressao += '%'
            janela.find_element('input').Update(expressao)
        case '=':
            computa_equacao() # Chama a funcao
        case 'C':
            expressao += '' # Limpa o display e esvazia o que tem na expressao (clear all)
            janela.find_element('input').Update(expressao)

    if botao == 'CE' or botao == 'BackSpace:8':
        backspace()
    if botao == sg.WIN_CLOSED or botao == 'Escape:27': # Botao e tecla para fechar a janela
        janela.close()
        break
            