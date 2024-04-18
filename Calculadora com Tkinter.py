from tkinter import *
from tkinter import ttk

#Função mostrar valor no display
def Valor_display(valor):
    global todos_valores
    todos_valores = todos_valores + str(valor)
    valor_texto.set(todos_valores)


#Função para calcular
def Calcular():
    global todos_valores
    resultado = eval(todos_valores)
    Limpar_display()
    valor_texto.set(str(resultado))


#Função para limpar a tela
def Limpar_display():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')


#Cores 
cor1 = "#3b3b3b" #Prtro
cor2 = "#feffff" #Branco
cor3 = "#38576b" #Azul
cor4 = "#ECEFF1" #Cinza
cor5 = "#FFAB40" #Laranja


janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=cor1)

#Criando Frames
frame_display = Frame(janela, width=235, height=50, bg=cor3)
frame_display.grid(row=0, column=0)
frame_botoes = Frame(janela, width=235, height=268)
frame_botoes.grid(row=1, column=0)


#Criando Label
todos_valores = ''
valor_texto = StringVar()

display_label = Label(frame_display, textvariable=valor_texto, width=16, height=2, padx=7,relief="flat",anchor=E, justify="right", font="ivy 18", fg=cor2, bg=cor3)
display_label.place(x=0, y=3)



#Criando Botoes

b_1 = Button(frame_botoes, command=Limpar_display,text="C", width=11, height=2, bg=cor4, font="ivy 13 bold", relief="raised", overrelief="ridge")
b_1.place(x=0, y=0)
b_2 = Button(frame_botoes, command=lambda: Valor_display('%'), text="%", width=5, height=2, bg=cor4, font="ivy 13 bold", overrelief="ridge")
b_2.place(x=118, y=0)
b_3 = Button(frame_botoes, command=lambda: Valor_display('/'), text="/", width=5, height=2, bg=cor5, fg=cor2, font="ivy 13 bold", relief="raised", overrelief="ridge")
b_3.place(x=177, y=0)

b_4 = Button(frame_botoes, command=lambda: Valor_display('7'), text="7", width=5, height=2, bg=cor4, font="ivy 13 bold", overrelief="ridge")
b_4.place(x=0, y=52)
b_5 = Button(frame_botoes, command=lambda: Valor_display('8'), text="8", width=5, height=2, bg=cor4, font="ivy 13 bold", overrelief="ridge")
b_5.place(x=59, y=52)
b_6 = Button(frame_botoes, command=lambda: Valor_display('9'), text="9", width=5, height=2, bg=cor4, font="ivy 13 bold", overrelief="ridge")
b_6.place(x=118, y=52)
b_7 = Button(frame_botoes, command=lambda: Valor_display('*'), text="*", width=5, height=2, bg=cor5, fg=cor2, font="ivy 13 bold", overrelief="ridge")
b_7.place(x=177, y=52)

b_8 = Button(frame_botoes, command=lambda: Valor_display('4'), text="4", width=5, height=2, bg=cor4, font="ivy 13 bold", overrelief="ridge")
b_8.place(x=0, y=104)
b_9 = Button(frame_botoes, command=lambda: Valor_display('5'), text="5", width=5, height=2, bg=cor4, font="ivy 13 bold", overrelief="ridge")
b_9.place(x=59, y=104)
b_10 = Button(frame_botoes, command=lambda: Valor_display('6'), text="6", width=5, height=2, bg=cor4, font="ivy 13 bold", overrelief="ridge")
b_10.place(x=118, y=104)
b_11 = Button(frame_botoes, command=lambda: Valor_display('-'), text="-", width=5, height=2, bg=cor5, fg=cor2, font="ivy 13 bold", overrelief="ridge")
b_11.place(x=177, y=104)

b_12 = Button(frame_botoes, command=lambda: Valor_display('1'), text="1", width=5, height=2, bg=cor4, font="ivy 13 bold", overrelief="ridge")
b_12.place(x=0, y=156)
b_13 = Button(frame_botoes, command=lambda: Valor_display('2'), text="2", width=5, height=2, bg=cor4, font="ivy 13 bold", overrelief="ridge")
b_13.place(x=59, y=156)
b_14 = Button(frame_botoes, command=lambda: Valor_display('3'), text="3", width=5, height=2, bg=cor4, font="ivy 13 bold", overrelief="ridge")
b_14.place(x=118, y=156)
b_15 = Button(frame_botoes, command=lambda: Valor_display('+'), text="+", width=5, height=2, bg=cor5, fg=cor2, font="ivy 13 bold", overrelief="ridge")
b_15.place(x=177, y=156)

b_1 = Button(frame_botoes, command=lambda: Valor_display('0'), text="0", width=11, height=2, bg=cor4, font="ivy 13 bold", relief="raised", overrelief="ridge")
b_1.place(x=0, y=208)
b_2 = Button(frame_botoes, command=lambda: Valor_display('.'), text=".", width=5, height=2, bg=cor4, font="ivy 13 bold", overrelief="ridge")
b_2.place(x=118, y=208)
b_3 = Button(frame_botoes, command= Calcular, text="=", width=5, height=2, bg=cor5, fg=cor2, font="ivy 13 bold", relief="raised", overrelief="ridge")
b_3.place(x=177, y=208)
janela.mainloop()