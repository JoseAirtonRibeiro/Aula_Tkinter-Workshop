from tkinter import *
from tkinter import messagebox

def CalcMedia():
    text = caixa.get()
    text2= caixa2.get()
    if text == '':
        messagebox.showerror('Atenção', '1° Numero inválido, Verifique tente novamente')
    else:
        pass

    if text2 == '':
        messagebox.showerror('Atenção', '2° Numero inválido, Verifique tente novamente')
    else:
        pass

    media = (float(text) + float(text2)) / 2
    if media <= 29:
        numeroResultado['text'] = (f'Reprovado   Média:{media}')
    else:
        numeroResultado['text'] = (f'Aprovado!   Média:{media}')


def Format(event = None):
    text = caixa.get()
    text2 = caixa2.get()
    novo_text  = ''
    novo_text2 = ''

    if event.keysym.lower() == 'backspace':
        return
    if not text.isnumeric():
        pass
    else:
        novo_text += text

    if not text2.isnumeric():
        pass
    else:
        novo_text2 += text2
        pass
    
    caixa.delete(0, 'end')
    caixa2.delete(0, 'end')
    
    caixa.insert(0, novo_text)
    caixa2.insert(0, novo_text2)


#=======================================================#
tela = Tk()
tela.title('Média')
tela.geometry('400x375')
tela.resizable(False, False)
tela.bind('<KeyRelease>', Format)
corFundo = "#5C78C6"
fonteTitulo = "Verdana 20 bold"
tela.config(background=corFundo)

#=======================================================#
numero1 = Label(tela, text='Digite o 1° numero:', font=fonteTitulo, background=corFundo)
caixa = Entry(tela, font='arial 15', border=0, background=corFundo)
linhaCaixa = Label(tela, font=fonteTitulo, background='black')

numero2 = Label(tela, text='Digite o 2° numero:', font=fonteTitulo, background=corFundo)
caixa2 = Entry(tela, font='arial 15', border=0, background=corFundo)
linhaCaixa2 = Label(tela, font=fonteTitulo, background='black')

botao = Button(tela, text='Calcular', font=fonteTitulo, background='light green',activebackground='red', activeforeground='white',border=0, command=CalcMedia)

resultado = Label(tela, text='RESULTADO', font=fonteTitulo, background=corFundo)
numeroResultado = Label(tela, text='', font=fonteTitulo, background=corFundo)
linha_resul = Label(tela, text='______________________', font=fonteTitulo, background=corFundo)
#=======================================================#

numero1.pack(pady=5)
linhaCaixa.place(width=223, height=3, x=88, y=75)
caixa.pack(pady=5)

numero2.pack(pady=5)
linhaCaixa2.place(width=223, height=3, x=88, y=158)
caixa2.pack(pady=5)

botao.pack(pady=5)

numeroResultado.pack(side=BOTTOM)
resultado.pack(side=BOTTOM)
linha_resul.pack(side=BOTTOM)

tela.mainloop()
