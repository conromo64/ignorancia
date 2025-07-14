#10#
import random
import pymysql
from msilib.schema import ComboBox
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from conecta_bd import *

#7#
pant = Tk()
pant.resizable(1,1)
pant.geometry("1200x900")
pant.config(bg="Light sky blue")
pant.title("Juego de la ignorancia-BD")

#12#
def recupera_bd():
    #1#
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
    #5#
    cursor = conn.cursor()
    #13#
    cursor.execute('select id_categoria, descripcion from categoria ')
    #4#
    categorias = cursor.fetchall()
    print(categorias)
    #15#
    cursor.execute('select id_pregunta, opcion_1, opcion_2, opcion_3, opcion_4, correcto, id_categoria from pregunta')
    #2#
    preguntas=cursor.fetchall() 
    print(preguntas)
    #14#
    conn.close()

#11#
def avanza_jug():
    global x1,x2,x3
    if turno==1:
        x1=x1+100
        j1.place(x=x1, y=252)
    elif turno==2:
        x2=x2+100
        j2.place(x=x2, y=363)
    elif turno==3:
        x3=x3+100
        j3.place(x=x3, y=475)    


#6#     
def opc1():
    global turno, x4
    r1.config(state=DISABLED)
    r2.config(state=DISABLED)
    r3.config(state=DISABLED) 
    r4.config(state=DISABLED)  
    #8#  
    if correcto==1:
        avanza_jug()
    else:
        #9#
        x4=x4+100
        j4.place(x=x4, y=585)
    #17#
    turno=turno+1
    #25#
    if turno>3:
        turno=1
    str_sig.set('jugador '+str(turno))

#6#  
def opc2():
    global turno, x4
    r1.config(state=DISABLED)
    r2.config(state=DISABLED)
    r3.config(state=DISABLED) 
    r4.config(state=DISABLED)    
    #8#
    if correcto==2:
        avanza_jug()
    else:
        #9#
        x4=x4+100
        j4.place(x=x4, y=585)
    #17#
    turno=turno+1
    #25#
    if turno>3:
        turno=1
    str_sig.set('jugador '+str(turno))

#6#  
def opc3():
    global turno, x4
    r1.config(state=DISABLED)
    r2.config(state=DISABLED)
    r3.config(state=DISABLED) 
    r4.config(state=DISABLED)    
    #8#
    if correcto==3:
        avanza_jug()
    else:
        #9#
        x4=x4+100
        j4.place(x=x4, y=585)
    #17#
    turno=turno+1
    #25#
    if turno>3:
        turno=1
    str_sig.set('jugador '+str(turno))

#6#  
def opc4():
    global turno, x4
    r1.config(state=DISABLED)
    r2.config(state=DISABLED)
    r3.config(state=DISABLED) 
    r4.config(state=DISABLED)  
    #8#  
    if correcto==4:
        avanza_jug()
    else:
        #9#
        x4=x4+100
        j4.place(x=x4, y=585)
    #17#
    turno=turno+1
    #25#
    if turno>3:
        turno=1
    str_sig.set('jugador '+str(turno))



#18#
def sel_preg():
    global str_preg, correcto
    #21#
    tam=len(selection)
    #19#    
    if tam!=0:
        #30#
        #30#calcula un numero aleatorio entre 0 y el tamaño de la lista de preguntas
        n=random.randint(0, tam-1)
        print(n)
        #20#
        str_preg.set(selection[n][1])
        str_res1.set(selection[n][2])
        str_res2.set(selection[n][3])
        str_res3.set(selection[n][4])
        str_res4.set(selection[n][5])
        correcto=selection[n][6]
        print(correcto)
        #22#    
        r1.config(state=NORMAL)
        r2.config(state=NORMAL)
        r3.config(state=NORMAL) 
        r4.config(state=NORMAL)
    else:
        str_preg.set('categoria sin preguntas')
        str_res1.set('')   
        str_res2.set('')
        str_res3.set('')
        str_res4.set('')    
        #28#
        r1.config(state=DISABLED)
        r2.config(state=DISABLED)
        r3.config(state=DISABLED) 
        r4.config(state=DISABLED)

    pant.update()

#23#
def preguntas(event):
    global selection
    cat=event.widget.get()
    selection=recupera_preguntas(cat)
    #print(preg)
    sel_preg()

#26#
def pregunta_sig():
    global selection
    cat=categorias.get() 
    seleccion=recupera_preguntas(cat)
    #print(preg)
    sel_preg()  



#recupera_bd()
#16#
fon=PhotoImage(file=r"./imagenes/patio.png")
fond=Label(pant, image=fon, width=1200, bg="light sky blue", height=488).place(x=-2, y=210)

selection=()
#3#
str_preg=StringVar()
str_res1=StringVar()
str_res2=StringVar()
str_res3=StringVar()
str_res4=StringVar()
str_sig=StringVar()
correcto=0
x1=10
x2=10
x3=10
x4=10
turno=1

cats=recupera_categoria()
#24#
eti=Label(pant, bg="light sky blue", text="Categoria", font='helvetica 18 bold')
eti.place(x=10, y=10)
#27#
categorias=ttk.Combobox(pant, font='helvetica 18 bold')
#29#
categorias['values']=cats
categorias.place(x=150, y=10)
categorias.bind("<<ComboboxSelected>>", preguntas)

#35#
sig = Button(pant, text="siguiente", command=pregunta_sig, font='helvetica 14 bold', bg="green",)
sig.place(x=800 ,y=10)

#34#
str_sig.set('jugador 1')
sig_jug=Label(pant, bg="Light sky blue", textvariable=str_sig, font='helvetica 18 bold')
sig_jug.place(x=500, y=10)


#33#

eti=Label(pant, bg='light sky blue', text="pregunta", font='helvetica 18 bold')
eti.place(x=10, y=60)

str_preg.set("")
pre=Entry(pant,textvariable=str_preg, font='helvetica 18 bold', bg='lavender', width=100, state=DISABLED)
pre.place(x=150, y=60)

str_res1.set("")
r1=Button(pant,textvariable=str_res1, command=opc1, font='helvetica 14 bold', bg="blue", fg="white", width=20)
r1.place(x=100, y=110)

str_res2.set("")
r2=Button(pant,textvariable=str_res2, command=opc2, font='helvetica 14 bold', bg='blue', fg="white", width=20)
r2.place(x=360, y=110)

str_res3.set("")
r3=Button(pant,textvariable=str_res3, command=opc3, font='helvetica 14 bold', bg='blue', fg="white", width=20)
r3.place(x=620, y=110)

str_res4.set("")
r4=Button(pant,textvariable=str_res4, command=opc4, font='helvetica 14 bold', bg='blue', fg="white", width=20)
r4.place(x=880, y=110)

#31#

ju1=PhotoImage(file=r"./imagenes/lap.png")
j1=Label(pant, image=ju1, bg="light sky blue")
j1.place(x=10, y=252)

ju2=PhotoImage(file=r"./imagenes/gom.png")
j2=Label(pant, image=ju2, bg="light sky blue")
j2.place(x=10, y=363)

ju3=PhotoImage(file=r"./imagenes/sca.png")
j3=Label(pant, image=ju3, bg="light sky blue")
j3.place(x=10, y=475)

ju4=PhotoImage(file=r"./imagenes/bur.png")
j4=Label(pant, image=ju4, bg="light sky blue")
j4.place(x=10, y=585)


#32#
pant.mainloop()




#1#se crea un objeto de coneccion a la BD
#2#se crea una lista para contener las categorias extraidas de la base de datos
#3#definir variables para la pregunta y las respuestas
#4#se crea una lista para contener las categorias extraidas de la base de datos
#5#Se crea un cursor para ejecutar consultas a la base de datos
#6#procedimento de validacion de respuesta 
#7#Definicion de la pantalla
#8#si la respuesta es correcta avanza el jugador
#9#avanza la ignorancia
#10#Importar librerias
#11#avanza el jugador en el tablero
#12#procedimiento para conectar y extraer informacion de la BD
#13#se utiliza el cursor para ejecutar la consulta sobre la tabla de categoria
#14#cerrar la base de datos
#15#se utiliza el cursor para ejecutar la consulta sobre la tabla de preguntas
#16#recupera la imagen de fondo
#17#cambio de turno
#18#selecciona aleatoriamente la prgunta de la categoria seleccionada
#19#si hay preguntas en la categoria
#20#asigna la pregunta y las respuestas a las variables de control
#21#calcula cuantas preguntas hay en la categoria
#22#habilita los botones de respuesta
#23#procedimiento para recuperar las preguntas de la base de datos
#24#crea una etiqueta para la categoria
#25#si el turno es mayor a 3 se reinicia
#26#procedimiento para recuperar la siguiente pregunta
#27#combobox para seleccionar la categoria
#28#deshabilita los botones de respuesta
#29#se asigna la lista de categorias a la lista desplegable
#30#calcula un numero aleatorio entre 0 y el tamaño de la lista de preguntas
#31#define las imagenes de los jugadores
#32#ciclo principal de la aplicacion
#33#Define las etiquetas y botones para la pregunta y las respuestas
#34#Etiqueta para mostrar el jugador que sigue
#35#Boton para avanzar a la siguiente pregunta