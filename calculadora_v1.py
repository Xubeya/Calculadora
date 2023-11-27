"""
Calculadora con Tkinter

"""

from tkinter import*
import os

ruta_ppal = os.path.dirname(__file__)
ruta_img = os.path.join(ruta_ppal, "img")
ruta_favicon = os.path.join(ruta_img, "calcu.ico")



ventana = Tk()

ventana.iconbitmap(ruta_favicon)

TIPOGRAFIA = "Helvetica"
DIM_TIPO_PRINCIPAL = 31
DIM_TIPO_SECUNDARIO = 20
BG_COLOR_PRINCIPAL = "#fc71e8"
BG_COLOR_SECUNDARIO = "#f94dd0"
FG_COLOR_PRINCIPAL = "Black"
FG_COLOR_SECUNDARIO = "Black"
BG_COLOR_TERCIARIO = "#f528b9"


ventana.title("Calculadora")
ventana.configure(bg="#f204a1")
ventana.resizable(0,0)


entrada = Entry(ventana,
                font = (TIPOGRAFIA, DIM_TIPO_PRINCIPAL),
                width=15,
                justify=RIGHT,
                bg="#ff95ff",
                fg="Black",
                )

entrada.grid(row=0, 
             column=0,
             columnspan=4,
             padx=5,
             pady=5)
# Botones numeros
boton1 = Button(ventana, text="1", width=6, height=1, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), bg=BG_COLOR_PRINCIPAL, fg=FG_COLOR_SECUNDARIO, command= lambda : digitar(1))
boton2 = Button(ventana, text="2", width=6, height=1, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), bg=BG_COLOR_PRINCIPAL, fg=FG_COLOR_SECUNDARIO, command= lambda : digitar(2))
boton3 = Button(ventana, text="3", width=6, height=1, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), bg=BG_COLOR_PRINCIPAL, fg=FG_COLOR_SECUNDARIO, command= lambda : digitar(3))
boton0 = Button(ventana, text="0", width=6, height=1, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), bg=BG_COLOR_PRINCIPAL, fg=FG_COLOR_SECUNDARIO, command=lambda : digitar(0))
boton4 = Button(ventana, text="4", width=6, height=1, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), bg=BG_COLOR_PRINCIPAL, fg=FG_COLOR_SECUNDARIO, command= lambda : digitar(4))
boton5 = Button(ventana, text="5", width=6, height=1, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), bg=BG_COLOR_PRINCIPAL, fg=FG_COLOR_SECUNDARIO, command= lambda : digitar(5))
boton6 = Button(ventana, text="6", width=6, height=1, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), bg=BG_COLOR_PRINCIPAL, fg=FG_COLOR_SECUNDARIO, command= lambda : digitar(6))
boton7 = Button(ventana, text="7", width=6, height=1, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), bg=BG_COLOR_PRINCIPAL, fg=FG_COLOR_SECUNDARIO, command= lambda : digitar(7))
boton8 = Button(ventana, text="8", width=6, height=1, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), bg=BG_COLOR_PRINCIPAL, fg=FG_COLOR_SECUNDARIO, command= lambda : digitar(8))
boton9 = Button(ventana, text="9", width=6, height=1, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), bg=BG_COLOR_PRINCIPAL, fg=FG_COLOR_SECUNDARIO, command= lambda : digitar(9))
# Botones operaciones
boton_sum = Button(ventana, text="+", width=6, height=1, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), bg=BG_COLOR_SECUNDARIO, fg=FG_COLOR_SECUNDARIO, command= lambda : digitar("+"))
boton_res = Button(ventana, text="-", width=6, height=1, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), bg=BG_COLOR_SECUNDARIO, fg=FG_COLOR_SECUNDARIO, command= lambda : digitar("-"))
boton_mul = Button(ventana, text="x", width=6, height=1, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), bg=BG_COLOR_SECUNDARIO, fg=FG_COLOR_SECUNDARIO, command= lambda : digitar("*"))
boton_div = Button(ventana, text="/", width=6, height=1, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), bg=BG_COLOR_SECUNDARIO, fg=FG_COLOR_SECUNDARIO, command= lambda : digitar("/"))
boton_pun = Button(ventana, text=".", width=6, height=1, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), bg=BG_COLOR_SECUNDARIO, fg=FG_COLOR_SECUNDARIO, command= lambda : digitar("."))
boton_igu = Button(ventana, text="=", width=6, height=1, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), bg=BG_COLOR_TERCIARIO, fg=FG_COLOR_PRINCIPAL, command= lambda : calcular())
boton_par_ab = Button(ventana, text="(", width=6, height=1, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), bg=BG_COLOR_SECUNDARIO, fg=FG_COLOR_SECUNDARIO, command= lambda : digitar("("))
boton_par_cer = Button(ventana, text=")", width=6, height=1, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), bg=BG_COLOR_SECUNDARIO, fg=FG_COLOR_SECUNDARIO, command= lambda : digitar(")"))
boton_bor = Button(ventana, text="C", width=6, height=1, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), bg=BG_COLOR_TERCIARIO, fg=FG_COLOR_PRINCIPAL, command= lambda : borrar())
boton_bor_uno = Button(ventana, text="⬅", width=6, height=1, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), bg=BG_COLOR_SECUNDARIO, fg=FG_COLOR_SECUNDARIO, command= lambda : borrar_uno())

# situamos los botones
boton_bor.grid(row=1, column=0)
boton_par_ab.grid(row=1, column=1)
boton_par_cer.grid(row=1, column=2)
boton_bor_uno.grid(row=1,column=3)


boton7.grid(row=2, column=0)
boton8.grid(row=2, column=1)
boton9.grid(row=2, column=2)
boton_div.grid(row=2, column=3)


boton4.grid(row=3, column=0)
boton5.grid(row=3, column=1)
boton6.grid(row=3, column=2)
boton_mul.grid(row=3, column=3)


boton1.grid(row=4, column=0)
boton2.grid(row=4, column=1)
boton3.grid(row=4, column=2)
boton_res.grid(row=4, column=3)


boton0.grid(row=5, column=1)
boton_pun.grid(row=5,column=0)
boton_igu.grid(row=5,column=2)
boton_sum.grid(row=5, column=3)

indice = 0
def digitar(valor):
    global indice
    entrada.insert(indice,valor)
    indice += 1

def borrar():
    global indice
    entrada.delete(0, END)
    indice = 0

def calcular():
    
    global indice
    formula = entrada.get()
    borrar()
    try:
        resultado = eval(formula)
        entrada.insert(0, resultado)
    except SyntaxError:
        entrada.insert(0, "SyntaxError")
    except ZeroDivisionError:
        entrada.insert(0, "MathError")
    except:
        entrada.insert(0, "Felicidades, no se que has hecho")

    
    indice += len(entrada.get())
def borrar_uno():
    global indice
    entrada.delete(indice-1, indice)
    indice -= 1

ventana.mainloop()