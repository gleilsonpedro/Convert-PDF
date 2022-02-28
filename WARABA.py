from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from turtle import left 
from pdf2image import convert_from_path
import os
from pathlib import Path
import shutil

from pyparsing import ParseSyntaxException


def linha():
    lb_espaco = Label(app, text="_______________________________________________", font=("Arial 14"))
    lb_espaco.pack()

def espaco():
    lb_espaco = Label(app, text="", font=("Arial 8"))
    lb_espaco.pack()

def logica():
      
    pasta_principal = os.path.exists("data")
    if pasta_principal == False:
        os.mkdir("data")
   
    saidadpi = cb_dpi.get()
    saidaformato = cb_formato.get()
    filename = filedialog.askdirectory()
    lista_arquivos = os.listdir(filename)
    local= os.getcwd()
                       
    for arquivo in lista_arquivos:
        if ".pdf" in arquivo:
            
            shutil.move(f"{filename}/{arquivo}", local)
            
            img = convert_from_path(arquivo, dpi=(saidadpi), poppler_path=r"C:\Program Files\poppler-0.68.0\bin")
            for imgs in img:
                imgs.save(f"data/{arquivo}{saidaformato}")
            os.remove(arquivo)
            
       
    messagebox.showinfo("WARABA - by Gleilson Pedro", "Seus arquivos estão convertidos dentro da pasta data...com DPI:"+saidadpi+" No formato:"+saidaformato)
      
    app.destroy()

    
app=Tk()
app.title("WARABA - by Gleilson Pedro")
app.iconbitmap("waraba.ico")
# configura janela para abrir centralizada em qualquer tela
largura = 600
altura = 400
#seta a largura e altura da tela
largura_tela = app.winfo_screenwidth()
altura_tela = app.winfo_screenheight()
# faz o calculo pra centralizar a janela no meio da tela
pos_x = largura_tela/2 - largura/2
pos_y = altura_tela/2 - altura/2
#define as variáveis pra centralizar a tela
app.geometry("%dx%d+%d+%d" % (largura, altura, pos_x, pos_y))

listDpi = ["20", "40", "60", "80", "100", "120", "150", "200"]
listFormato = [".gif", ".jpg", ".png", ".bmp"]

lb_topo = Label(app, text="Este software converte os arquivos pdf em imagens", font="Arial 14", width=600,
               height=2, bg="gray", fg="white")
lb_topo.pack()

linha()
lb_dpi = Label(app, text="Escolha o DPI de saída.", font=("Arial 12"), anchor="w")
lb_dpi.pack()

cb_dpi = ttk.Combobox(app, values= listDpi, font="Arial 12", justify="center")
cb_dpi.set("100")
cb_dpi.pack()

lb_formato = Label(app, text="Escolha o Formato de saída", font=("Arial 12"))
lb_formato.pack()

cb_formato = ttk.Combobox(app, values= listFormato, font="Arial 12", justify="center")
cb_formato.set(".gif")
cb_formato.pack()
linha()

linha()
lb_informa = Label(app, text="Ao clicar em inciar conversão escolha a pasta dos PDF'S", font=("Arial 12"))
lb_informa.pack()

linha()
bt_converter = Button(app, text= "Inicia Conversão", comman=logica, 
                 width=15, height=1, 
                 font="Arial 12", bg= "gray",
                 fg="white")
bt_converter.pack()

app.mainloop()
