from tkinter import *


def CalcMedia():
    media = (float(caixa.get()) + float(caixa2.get())) / 2
    numeroResultado['text'] = media

# ======================================================= #
tela = Tk()
tela.title('Média')
tela.geometry('400x375')
tela.resizable(False, False)
corFundo = "light grey"
tela.config(background=corFundo)
# ======================================================= #
numero1 = Label(tela, text='Digite o 1° numero:', font='arial 15 bold', background=corFundo)
caixa = Entry(tela, font='arial 15')

numero2 = Label(tela, text='Digite o 2° numero:', font='arial 15 bold', background=corFundo)
caixa2 = Entry(tela, font='arial 15')

botao = Button(tela, text='Calcular Média', font='arial 15', command=CalcMedia)

resultado = Label(tela, text='RESULTADO', font='arial 15 bold', background=corFundo)
numeroResultado = Label(tela, text='', font='arial 15 bold', background=corFundo)
# ======================================================= #
numero1.pack(pady=5), caixa.pack(pady=5)
numero2.pack(pady=5), caixa2.pack(pady=5)
botao.pack(pady=5)

resultado.pack()
numeroResultado.pack()

tela.mainloop()
