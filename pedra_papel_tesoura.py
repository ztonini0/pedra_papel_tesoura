from tkinter import *
import random

janela = Tk()

#CRIAÇÃO DAS JANELAS, TITULO E PARA NÃO AUMENTAR A DIMENSÃO DA JANELA

janela.title('Pedra papel tesoura')
janela.iconbitmap('Ipapper.ico')
janela.resizable(False, False)

click = True

#ADICIONAR AS VARIVEIS PARA CARREGAR AS IMAGENS
#Principais imagens
papelPHoto = PhotoImage (file =  'papel.png')
pedraPhoto = PhotoImage(file =   'pedra.png')
tesouraphoto = PhotoImage(file = 'tesoura.png')

#Imagens segundarias
PM = PhotoImage(file = 'Pmao.png')
PDM = PhotoImage(file = 'PDmao.png')
TM = PhotoImage(file = 'Tmao.png')

#Imagens vitoria, derrota, empate
youwinPhoto = PhotoImage(file = 'youwin.png')
youlosePhoto = PhotoImage (file = 'gameover.png')
empate = PhotoImage(file = 'empate.png')

papelButton = ''
pedraButton = ''
tesouraButton = ''

#CRIANDO UMA FUNÇÃO PARA OS BOTOES E ARRUMAR AS COLUNAS DE CADA IMG QUE IRA APARECER NA INTERFACE

def game():
    global pedraButton,papelButton,tesouraButton

    pedraButton = Button(janela,image = pedraPhoto,command = lambda:Escolha('pedra'))
    papelButton = Button(janela,image = papelPHoto,
                         command = lambda:Escolha('papel'))
    tesouraButton = Button(janela,image = tesouraphoto,command = lambda:Escolha('tesoura'))


    pedraButton.grid(row = 0,column = 0)
    papelButton.grid(row = 0,column = 1)
    tesouraButton.grid(row = 0,column = 2)

#PARA A CPU JOGAR, ASSIM USANDO USANDO A BIBLIOTECA RANDOM PARA SER ALEATORIO

def computerPick():
    chave = random.choice(['pedra', 'papel', 'tesoura'])
    return chave

#A DEF CRIADA PARA RODAR O GAME, ASSIM QUE O USER DER UM CLICK NA IMAGEM VAI APARECER O RESULTADO SE ELE GANHOU, PERDEU OU EMPATOU.


def Escolha(Suachave):
    global click

    compPick = computerPick()

    if click == True:
        #PEDRA
        if Suachave == 'pedra':
            pedraButton.configure(image = pedraPhoto)
            #vitoria
            if compPick == 'tesoura':
                papelButton.configure(image = TM)
                tesouraButton.configure(image = youwinPhoto)
                click = False
            #derrota
            elif compPick == 'papel':
                papelButton.configure(image = PM)
                tesouraButton.configure(image = youlosePhoto)
                click = False
            #empate
            else:
                papelButton.configure(image = PDM)
                tesouraButton.configure(image = empate)
                click = False

        #PAPEL
        elif Suachave == 'papel':
            papelButton.configure(image = PM)
            if compPick == 'pedra':
                pedraButton.configure(image = PDM)
                tesouraButton.configure(image = youwinPhoto)
                click = False
            elif compPick == 'papel':
                pedraButton.configure(image = PM)
                tesouraButton.configure(image = empate)
                click = False
            else:
                pedraButton.configure(image = TM)
                tesouraButton.configure(image =youlosePhoto)
                click = False

         #tesoura
        elif Suachave == 'tesoura':
            tesouraButton.configure(image = TM)
            if compPick == 'pedra':
                papelButton.configure(image = PDM)
                pedraButton.configure(image = youlosePhoto)
                click = False
            elif compPick == 'papel':
                papelButton.configure(image = PM)
                pedraButton.configure(image = youwinPhoto)
                click = False
            else:
                papelButton.configure(image = TM)
                pedraButton.configure(image = empate)
                click = False

    else:
        #Para clicar na imagem e voltar para o começo do game
        if Suachave == 'pedra' or Suachave == 'papel' or Suachave == 'tesoura':
            pedraButton.configure(image = pedraPhoto)
            papelButton.configure(image = papelPHoto)
            tesouraButton.configure(image = tesouraphoto)
            click = True



game()

janela.mainloop()
