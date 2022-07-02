from tkinter import *
from tkinter.font import BOLD
from PIL import Image, ImageTk

v_b=True
op=''
r=0
num=''
def call_image(direccion_img, x, y):
    img_v=Image.open(direccion_img)
    img_v=img_v.resize((x,y), Image.LANCZOS )  #Image.ANTIALIAS
    img_v=ImageTk.PhotoImage(img_v)
    return img_v

class Calculator():
    def __init__(self):     #<-- constructor
        self.root=Tk()
        self.root.title('Calculadora - v2.5')
        self.root.iconbitmap('Tkinter\calculator.ico')
        self.root.attributes('-alpha', 0.9)     #<-- con este metodo se establece transparencia a la aplicacion, los valores van de 1 al 0
        self.mainf=Frame(bg='#2d2d2d')
        self.mainf.pack()
    
    def window(self):   #<-- pantalla principal para los numeros y resultados
        self.window_sup()
        p=Entry(
            self.mainf,
            bg='#2d2d2d',
            fg='white',
            font=('Arial Rounded MT Negrita', 32, BOLD),
            width=10,
            justify='right',
            textvariable=num_w,
            bd=0,
            state='readonly',
            readonlybackground='#2d2d2d'
        )
        p.grid(row=1,
        column=0,
        columnspan=3,       #<-- hace que ocupe varias columnas el objeto
        padx=10, pady=5,    #<-- establece la separacion desde dentro
        ipadx=2, ipady=5    #<-- establece la separacion desde fuera
        )
        p.focus()   #<-- hace que el cursor de inicie dentro del entry para poder escribir directamente
    
    def window_sup(self):   #<-- pantalla superior donde se van escribiendo las operaciones e icono de calculadora
        Label(
            self.mainf,
            bg='#161616',
            image=calculador_logo,
            bd=0
        ).grid(row=0,
            column=3,
            ipadx=5,
            ipady=5,
            sticky=NSEW
            )
        Label(
            self.mainf,
            bg='#2d2d2d',
            fg='#8a8a8a',
            font=('Arial Rounded MT Negrita', 20, BOLD),
            justify='right',
            textvariable=num_wsup,
            bd=0
        ).grid(row=0,
            column=0,
            columnspan=3,
            sticky=E,
            ipadx=5,
            ipady=5
            )
    
    def buttom_del(self, v):    #<-- crea el botom borrar
        boton_del=Button(
            self.mainf,
            bg='#053061',
            activebackground='#7e7e7e',
            activeforeground='white',
            fg='white',
            image=v,
            #textvariable=v,
            command=lambda: self.delete(),
            font=('Arial Rounded MT Negrita', 24, BOLD),
            bd=0,
        )
        boton_del.grid(row=1,column=3,
            padx=1, pady=1,
            #ipadx=10, ipady=2,
            sticky=NSEW
        )
        boton_del.bind('<Enter>', func=lambda e: boton_del.config(background='#1961b5'))
        boton_del.bind('<Leave>', func=lambda e: boton_del.config(background='#053061'))
    
    def delete(self):   #<-- funcionalidad del boton borrar
        global r
        global num
        try:
            w=num_w.get()
            p=w[(len(w)-1)]
            b=(w.removesuffix(p))
            num_w.set(b)
        except IndexError:
            num_wsup.set(num_w.get())
            r=0
            num=''
    
    def buttom(self,r,c,v, c_base, c_selec):    #<-- crea todos los demas botones
        boton=Button(
            self.mainf,
            bg=c_base,
            activebackground='#7e7e7e',     #<-- color al dar el click del fondo
            activeforeground='white',       #<-- color al dar el click del contenido
            fg='white',
            text=v,
            textvariable=v,
            command=lambda: self.click(v),
            font=('Arial Rounded MT Negrita', 24, BOLD),
            bd=0
        )
        boton.grid(row=r,column=c,
            padx=1, pady=1,
            ipadx=18, ipady=2,
            sticky=NSEW         #<-- hace que el contenido de la grilla se expanda en todas direcciones
        )
        boton.bind('<Enter>', func=lambda e: boton.config(background=c_selec))  #<-- funciones para cambiar color al
        boton.bind('<Leave>', func=lambda e: boton.config(background=c_base))   #posicionar el mouse enter al ponerlo y leave al quitarlo para devolverlo a su color anterior
    
    def buttoms(self):  #<-- agrupacion de las llamadas de los botones
        
        self.buttom_del(del_boton)
        
        self.buttom(2,0, 7, 'black', '#6f6f6f')    #llamadas a la construccion de todos los bonotes
        self.buttom(2, 1, 8, 'black', '#5d5d5d')
        self.buttom(2, 2, 9, 'black', '#5d5d5d')
        self.buttom(2, 3, '/', '#161616', '#6f6f6f')
        
        self.buttom(3, 0, 4, 'black', '#5d5d5d')
        self.buttom(3, 1, 5, 'black', '#5d5d5d')
        self.buttom(3, 2, 6, 'black', '#5d5d5d')
        self.buttom(3, 3, 'X', '#161616', '#6f6f6f')
        
        self.buttom(4, 0, 1, 'black', '#5d5d5d')
        self.buttom(4, 1, 2, 'black', '#5d5d5d')
        self.buttom(4, 2, 3, 'black', '#5d5d5d')
        self.buttom(4, 3, '-', '#161616', '#6f6f6f')
        
        self.buttom(5, 0, ',', '#161616', '#6f6f6f')
        self.buttom(5, 1, 0, 'black', '#5d5d5d')
        self.buttom(5, 2, '=', '#053061', '#1961b5')
        self.buttom(5, 3, '+', '#161616', '#6f6f6f')
    
    def write_window(self, v):  #<-- funcion que escribe en la pantalla principal
        global v_b
        
        if v_b:
            num_w.set(num_w.get() + str(v))

        else:
            num_w.set(str(v))
            v_b=True
    
    def write_windowsup(self, v):   #<-- funcion que escribe en la pantalla superior
        global v_b
        global op
        global num
        v_b=False

        if v != '=':
            num_wsup.set(num_wsup.get() + str(num) + str(v))
            num=''
            
        else:
            num_wsup.set('')
    
    def click(self, v):     #<-- funcion que tienen todos los botones (excepto el de borrar) y evalua si se pulso un numero u operacion
        global op
        global num
        if isinstance(v, int):
            num=num.__add__(str(v))
            self.write_window(v)

        else:
            op=v
            self.operation()

            if v_b:
                self.write_windowsup(v)
    
    def operation(self):    #<-- evalua el tipo de operacion
        global op
        if op == '+':
            self.suma()
        
        elif op == '-':
            self.resta()
            
        elif op == 'X':
            self.multiplica()
            
        elif op == '/':
            self.divide()
            
        elif op =='=':
            pass
            self.resultado()
    
    #------ FUNCIONES DE OPERACION ------
    def suma(self):
        global r
        global num

        r+=int(num)
        num_w.set(r)

    def resta(self):
        global r
        global num

        if r != 0:
            r-=int(num)
            
        else:
            r=int(num)
            
        num_w.set(r)
        
    def multiplica(self):
        global r
        global num

        if r != 0:
            r*=int(num)
            
        else:
            r=int(num)
            
        num_w.set(r)
        
    def divide(self):
        global r
        global num

        if r != 0:
            r/=int(num)
        else:
            r=int(num)
            
        num_w.set(r)
        
    def resultado(self):
        global op
        global r
        global num
        
        try:
            op=num_wsup.get()[len(num_wsup.get())-1]
            self.operation()
            r=0
            num=''
        except IndexError:
            pass
    

calculadora=Calculator()
num_w=StringVar()   #<-- Variable designada a la pantalla principal
num_wsup=StringVar()    #<-- Variable designada a la pantalla superior

#llamadas a la funcion que redimensiona el tamaño de las imagenes
calculador_logo=call_image('Tkinter\calculator.png', 30, 30)    #<-- imagen del logo que se añade a un lado de la pantalla superior
del_boton=call_image('Tkinter\del.png', 30, 30)     #<-- imagen del boton borrar

#llamadas a metodos obligatorios para que funcione la calculadora
calculadora.window()
calculadora.buttoms()
calculadora.root.mainloop()