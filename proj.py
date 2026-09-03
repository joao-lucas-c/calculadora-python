from tkinter import *
from tkinter import ttk

# Cores
cor1 = "#292827" 
cor2 = "#feffff"
cor3 = "#38576b"
cor4 = "#ECEFF1"
cor5 = "#FFAB40"

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=cor1)

# Frames
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=260, bg=cor1)
frame_corpo.grid(row=1, column=0)

todos_valores = ''

def entrada_valores(valor):
    global todos_valores
    todos_valores += str(valor)
    valor_texto.set(todos_valores)
    
def calcular_resultado():
    global todos_valores
    try:
        # Substitui a porcentagem para divisão por 100
        expressao = todos_valores.replace('%', '/100')
        resultado = eval(expressao)
        
        valor_texto.set(resultado)
        todos_valores = str(resultado)
    except ZeroDivisionError:
        valor_texto.set("Erro: Div/0")
        todos_valores = ''
    except Exception:
        valor_texto.set("Erro")
        todos_valores = ''

def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

# Label
valor_texto = StringVar()
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

# Botões - Primeira linha
Button(frame_corpo, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=limpar_tela).place(x=0, y=0)
Button(frame_corpo, text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valores('%')).place(x=118, y=0)
Button(frame_corpo, text="/", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valores('/')).place(x=177, y=0)

# Segunda linha
Button(frame_corpo, text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valores('7')).place(x=0, y=52)
Button(frame_corpo, text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valores('8')).place(x=59, y=52)
Button(frame_corpo, text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valores('9')).place(x=118, y=52)
Button(frame_corpo, text="*", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valores('*')).place(x=177, y=52)

# Terceira linha
Button(frame_corpo, text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valores('4')).place(x=0, y=104)
Button(frame_corpo, text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valores('5')).place(x=59, y=104)
Button(frame_corpo, text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valores('6')).place(x=118, y=104)
Button(frame_corpo, text="-", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valores('-')).place(x=177, y=104)

# Quarta linha
Button(frame_corpo, text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valores('1')).place(x=0, y=156)
Button(frame_corpo, text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valores('2')).place(x=59, y=156)
Button(frame_corpo, text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valores('3')).place(x=118, y=156)
Button(frame_corpo, text="+", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valores('+')).place(x=177, y=156)

# Quinta linha
Button(frame_corpo, text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valores('0')).place(x=0, y=208)
Button(frame_corpo, text=".", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valores('.')).place(x=118, y=208)
Button(frame_corpo, text="=", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=calcular_resultado).place(x=177, y=208)

janela.mainloop()