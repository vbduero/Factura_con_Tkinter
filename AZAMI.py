
#from tkinter import ttk
#from cProfile import label
#from cgitb import text
#from logging.config import valid_ident
from tkinter import *

from PIL import Image, ImageTk

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter


print ("        AZAMI S.A.S    "   )
print ("       NIT 32435465    "   )
print ("      TEL: 3142769220  "   )
print (" - " * 30)
print ("     TERMINAL NEIVA HUILA  "  )
print ("  CAJERO: Bermeo Duero Valentina  ")

#LIBRERIA tiempo
import datetime
tiempo =datetime.datetime.now()
print(tiempo)
print("{}/{}/{}".format(tiempo.day,tiempo.month,tiempo.year))
print("{}:{}:{}".format(tiempo.hour,tiempo.minute,tiempo.second))


class Cliente:

    #def __init__(self, root):
        #self.wind = root
        #self.wind.title("   RECIBO   ")
        #self.wind.geometry("850x600")
        #self.wind.config(bg="teal")
        

    def __init__(self):
        self.nombrecli = " "
        self.cedulacli = " "


    def datos(self):
        print('--------------------------')
        print('          CLIENTE   ')
        print('---------------------------')
        self.nombrecli = input( 'Digite el nombre del cliente: ')
        self.cedulacli = input( 'Digite la cedula del cliente: ')

class Producto:

    def _init_(self):
        self.cantidad = 0
        self.precio = 0
        self.nombre = " "
        self.costo_total = 0
        self.itbis_total = 0 

    def calcular_costo_total(self):
        self.costo_total = self.cantidad * self.precio
    def calcular_itbis_total(self):
        self.itbis_total = self.costo_total * 0.19

    def so_datos(self):
        print('-------------------------')
        print( '         PRODUCTO  ')
        print('--------------------------')
        self.nombre = input( 'Digite el nombre del producto: ')
        self.precio = float(input('Digite el precio del producto:$ '))
        self.cantidad = int(input( 'Digite la cantidad del producto: '))

class Factura:
    def __init__(self, cliente, lista_productos):
        self.lista_productos = lista_productos
        self.cliente = cliente
        self.monto = 0
       
    
    def re_productos(self):
        while True:
            print('Facturar un producto?')
            print('1 = SI')
            print('2 = NO')
            va = int(input('Digite la opcion deseada: '))
            if va == 2:
                print("Inicia de nuevo")
                break
            else:
                producto = Producto()
                producto.so_datos()
                producto.calcular_costo_total()
                self.lista_productos.append(producto)
        
        while True:
            print (" - " * 35)
            print('Pagar con tarjeta')
            print('1 - SI')
            print('2 - NO')
            va = int(input( 'Digite la opcion deseada: '))
            if va == 1:
               print("No es permitido, estamos trabajando en ello")
            else:
                print("okay")
                break

    def procesar_fac(self):

        for producto in self.lista_productos:
            self.monto += producto.costo_total

        print ("=" * 35)
        print (f' NOMBRE : {self.cliente.nombre}')
        print (f' CEDULA : {self.cliente.cedulacli}') 
        #print (f' NOMBRE : {self.cliente.nombrecli}')   
        print(f'SUBTOTAL : {self.monto}')
        print('-' * 35)
        print(f'CANTIDAD PRODUCTO FACTURADOS: {len(self.lista_productos)}')
        print( 'LISTADO PRODUCTOS: ')
        print('-' * 30)
        for producto in self.lista_productos:
            print(f'NOMBRE: {producto.nombre} - PRECIO: {producto.precio} - CANTIDAD: {producto.cantidad} - TOTAL: {producto.costo_total} ')
        print(f'IVA FINAL : {self.monto  *  0.19}')
        print(f'TOTAL : {self.monto  + (self.monto*  0.19)}')
        print( '-' * 30)

    def juan(self):
        w, h = letter
        c = canvas.Canvas("mio.pdf", pagesize=letter)
        c.setFont("Helvetica",9)
        c.drawString(160,h-50,"hola mundo")
        #c.drawString(160, h-70,f"FECHA:  {datetime.datetime.now().day} / {datetime.datetime.now().month} / {datetime.datetime.now().year}       Hora:{hora}:{minu}:{seg}")

        c.drawString(160, h-85, f"TOTAL{self.monto}")
        c.drawImage("py_code.png",160, h-300, width=100, height=100)

        c.save()




        root = Tk()
        root.title("        RECIBO ")
        #Contenedor=Frame(root,width=500,height=500,bg="green")
        #Contenedor.pack()

        root.config(width=500,height=500,bg="white")
        Qr = Image.open("./py_code.png")
        Qr_redimensionada = Qr.resize((150,150),Image.ANTIALIAS)
        Qr_procesada = ImageTk.PhotoImage(Qr_redimensionada)
        este=Label(root,text=" AZAMI S.A.S    ",bg="white",font=("Avenir Next Condensed",15))
        este.place(x=190,y=10)
        esta=Label(root,text="  NIT: 3243546-5    ",bg="white",font=("Avenir Next Condensed",15))
        esta.place(x=187,y=32)
        esto=Label(root,text="RESPONSABLE DE IVA. EEU 1081 ",bg="white",font=("Avenir Next Condensed",15))
        esto.place(x=147,y=52)
        valenti=Label(root,text="  Agente Retenedor de ICA   ",bg="white",font=("Avenir Next Condensed",15))
        valenti.place(x=167,y=72)
        valen=Label(root,text="   TEL: 3142769220  ",bg="white",font=("Avenir Next Condensed",15))
        valen.place(x=180,y=92)
        val=Label(root,text="Servicios_Exito.com.co  ",bg="white",font=("Avenir Next Condensed",15))
        val.place(x=180,y=112)
        es=Label(root,text="  TERMINAL EXITO HUILA    ",bg="white",font=("Avenir Next Condensed",15))
        es.place(x=157,y=132)
        est=Label(root,text="     DG 23 65 73 LC 123  ",bg="white",font=("Avenir Next Condensed",15))
        est.place(x=158,y=152)
        NATA=Label(root,text="Aut. DIAN 78654345678  FEC 03/03/2022  ",bg="white",font=("Avenir Next Condensed",15))
        NATA.place(x=120,y=182)
        RAFA=Label(root,text="DESDE JK-33668     HASTA JK - 2000000   ",bg="white",font=("Avenir Next Condensed",15))
        RAFA.place(x=120,y=202)
        GINA=Label(root,text="DCTO/EQUIVALENTE POS:  JK - 52341  ",bg="white",font=("Avenir Next Condensed",15))
        GINA.place(x=120,y=222)
        WILLI=Label(root,text="VIGENCIA HASTA: 13/12/2023  ",bg="white",font=("Avenir Next Condensed Demi Bold",15))
        WILLI.place(x=120,y=242)
        GIN=Label(root,text=f"FECHA:{tiempo.day,tiempo.month,tiempo.year}   HORA:{tiempo.hour,tiempo.minute,tiempo.second}  ",bg="white",font=("Avenir Next Condensed",15))
        GIN.place(x=120,y=262)
        WIL=Label(root,text="CAJERO: BERMEO DUERO VALENTINA  ",bg="white",font=("Avenir Next Condensed",15))
        WIL.place(x=120,y=282)
        e=Label(root,text="====================================== ",bg="white",font=("Arial",15))
        e.place(x=100,y=302)
        WIl=Label(root,text="Uds DESCRIPCION       PRECIO         TOTAL  ",bg="white",font=("Avenir Next Condensed",15))
        WIl.place(x=125,y=322)
        ew=Label(root,text="====================================== ",bg="white",font=("Arial",15))
        ew.place(x=100,y=342)
        
        W=Label(root,text=f"                                                   {self.monto}  ",bg="white",font=("Avenir Next Condensed",15))
        W.place(x=125,y=362)
        ewS=Label(root,text="====================================== ",bg="white",font=("Arial",15))
        ewS.place(x=100,y=382)
        Wo=Label(root,text=f"  SUBTOTAL    {self.lista_productos}  ",bg="white",font=("Avenir Next Condensed",15))
        Wo.place(x=185,y=402)
        Wx=Label(root,text=f"  DTO     {self.lista_productos}  ",bg="white",font=("Avenir Next Condensed",15))
        Wx.place(x=185,y=422)
        WQQ=Label(root,text=f"   TOTAL       {self.monto}  ",bg="white",font=("Avenir Next Condensed",15))
        WQQ.place(x=185,y=442)
        mu=Label(root,text="====================================== ",bg="white",font=("Arial",15))
        mu.place(x=100,y=462)
        ma=Label(root,text="DISCRIMINACION DE IMPUESTOS ",bg="white",font=("Avenir Next Condensed",15))
        ma.place(x=170,y=482)
        me=Label(root,text=f"  I BASE  19%          {self.monto}  IVA      {self.monto  *  0.19}  ",bg="white",font=("Avenir Next Condensed",15))
        me.place(x=153,y=502)
        mi=Label(root,text=f"    TOTAL                      {self.monto}              {self.monto  *  0.19}  ",bg="white",font=("Avenir Next Condensed",15))
        mi.place(x=152,y=522)
        mo=Label(root,text="====================================== ",bg="white",font=("Arial",15))
        mo.place(x=100,y=542)
        ka=Label(root,text=" FORMA DE PAGO ",bg="white",font=("Avenir Next Condensed",15))
        ka.place(x=180,y=562)
        ke=Label(root,text=f"    EFECTIVO                 {self.monto * 0.19 + self.monto}    ",bg="white",font=("Avenir Next Condensed",15))
        ke.place(x=157,y=582)
        ki=Label(root,text="====================================== ",bg="white",font=("Arial",15))
        ki.place(x=100,y=602)
        ko=Label(root,text="!GRACIAS POR TU COMPRA!  ",bg="white",font=("Avenir Next Condensed",15))
        ko.place(x=180,y=622)
        ku=Label(root,text="  !Unete a nuestro programa de    ",bg="white",font=("Avenir Next Condensed",15))
        ku.place(x=157,y=642)
        pa=Label(root,text="            fidelizacion Exito SS!  ",bg="white",font=("Avenir Next Condensed",15))
        pa.place(x=158,y=662)

        Q = Label(root, image= Qr_procesada, bg="white",border=10,pady=10)
        Q.place(x=150,y=685)

        pe=Label(root,text=" www.Exito.com.co  ",bg="white",font=("Avenir Next Condensed",15))
        pe.place(x=180,y=842)
        pi=Label(root,text="  Registrate con el codigo: 13   ",bg="white",font=("Avenir Next Condensed",15))
        pi.place(x=157,y=862)
        pu=Label(root,text="====================================== ",bg="white",font=("Arial",15))
        pu.place(x=100,y=882)
        po=Label(root,text="Tiquete POS impuesto por software ServiSoft  ",bg="white",font=("Avenir Next Condensed",15))
        po.place(x=135,y=902)
        xa=Label(root,text="   Desarrollado por ING  NIT:600098764-0  ",bg="white",font=("Avenir Next Condensed",15))
        xa.place(x=135,y=922)
        xe=Label(root,text="====================================== ",bg="white",font=("Arial",15))
        xe.place(x=100,y=942)


        root.mainloop()

    def fin (self):
        print('=' * 30)
        print( "          EL EXITO.COM     ")
        print('=' * 30)
        #self.datos()
        self.re_productos()
        self.procesar_fac()
        self.juan()
        print('-' * 30)

factura=Cliente()
factura.datos()
factura = Factura( cliente=Cliente(), lista_productos=[])
#factura.datos()
#factura.registrar_productos()
#factura.procesar_factura()
factura.fin()



