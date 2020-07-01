# -*- coding: utf-8 -*-
from functools import partial
from tkinter import *
from random import shuffle
from os import path
from tkinter import ttk

def janela1():
    #Imagem da tela
    janela = Tk()  
    janela.title("Sudoku da Depressão 1.0.1")
    labelima=ttk.Label(janela)
    labelima.pack()
    mi= PhotoImage(file=".\Mamona.png")
    labelima.config(image=mi)
    labelima['background']="deepskyblue4"
    labelima.place(x= 199, y = 350)
    janela["bg"]="deepskyblue4"

    #Textos
    lb3=Label(janela, text = "  Trabalho Interdisciplinar  ",
              bg = "deepskyblue4",fg = "white",
              font= ("Comic Sans MS", 13))
    lb3.place(x=145, y= 80)
    lb4=Label(janela, text = "  Sistemas de Informação  ",
              bg = "deepskyblue4",
              fg = "white",
              font= ("Comic Sans MS", 20))
    lb4.place(x=80, y= 20)
    lb=Label(janela, text = " Sudoku da Depressão",
             bg = "deepskyblue4",fg = "black",
             font= ("Chiller", 40))
    lb.place(x=80, y= 180)
    lb3=Label(janela, text = "Desenvolvedores: ",
              bg = "deepskyblue4",fg = "black",
              font= ("Verdana", 10))
    lb3.place(x=10, y= 480)
    lb3=Label(janela, text = "Bryan França",
              bg = "deepskyblue4",fg = "white", font= ("Verdana", 8))
    lb3.place(x=130, y= 482) 
    bt= Button(janela, text="INICIAR",
               fg= "black", bg="white",
               font= ("Comic Sans MS", 12))
    bt["command"] = partial (bt_click_j1, janela)
    bt.place(x = 206, y = 280)
    janela.geometry("500x500+400+100")
    janela.mainloop()
  

def janela2():
# montar a janela    
    janela= Tk()
    janela.title("Sudoku da Depressão")
    janela.geometry("700x500+250+100")
    janela["bg"]="deepskyblue4"
    fonte1=("Verdana","10")

    labelra=ttk.Label(janela)
    labelra.pack()
    mix= PhotoImage(file=".\\rank.png")
    labelra.config(image=mix)
    labelra['background']="deepskyblue4"
    labelra.place(x= 507, y = 25)

    
#Quadro
    labelim=ttk.Label(janela)
    labelim.pack()
    mi= PhotoImage(file=".\quadro.gif")
    labelim.config(image=mi)
    labelim['background']="deepskyblue4"
    labelim.place(x= 408, y = 70)

# mostrar o ranking
    # ler o arquivo se ele existir
    texto = ['']
    if path.exists('Nome e Tempo.txt'):
        text_file = open("Nome e Tempo.txt","r")
        texto = text_file.readlines()
        texto.append("\n")
        text_file.close()
    #montar a lista
    i = 0
    #cria um dicionario com o tempo e o nome
    ranking = {}
    while i < len(texto)-1:
        ranking[int(texto[i])] = str(int(texto[i])) + ' => '+texto[i+1]
        i+=2
    #monta uma lista com as chaves ordenadas
    chaves_t = sorted(ranking)
    #monta uma lista com no máximo 4 chaves - numero de nomes no ranking
    # para alterar é só mudar a condição i < 4
    i=0
    chaves = [];
    while i < len(chaves_t) and i < 5:
        chaves.append(chaves_t[i])
        i+=1
    i=0
    #mostra o ranking
    for ch in chaves:
        Label(janela,text=ranking.get(ch),bg="black",fg = "white",font=("ChalkDust","10"),width=25).place(x=420, y=85+i)
        i+=20
        


#Informar o nome
    Label(janela,text='Nome: ',font=fonte1,width=8).place(x=10, y=375)
    nome_t = Entry(janela,width=10,font=fonte1)
    nome_t.focus_force() # Para o foco começar neste campo
    nome_t.place(x=100, y=375)
    
    botao2 = Button (janela, text="Voltar")
    botao2['command'] = partial(botao2_click_j2, janela)


    
#VALOR ALEATORIOS
# Gera uma lista com os valores de 1 a 9
    lista = [1,2,3,4,5,6,7,8,9]
# Embarala o valores dentro da lista
    shuffle(lista)
    
    
#TROCAR NUMERO
    def bt4_click():
        bt4["text"] = bt4["text"] + 1
        if (bt4["text"]>9):
            bt4["text"]=0

    def bt9_click():
        bt9["text"] = bt9["text"] + 1
        if (bt9["text"]>9):
            bt9["text"]=0

    def bt12_click():
        bt12["text"] = bt12["text"] + 1
        if (bt12["text"]>9):
            bt12["text"]=0
    def bt7_click():
        bt7["text"] = bt7["text"] + 1
        if (bt7["text"]>9):
            bt7["text"]=0

    def bt15_click():
        bt15["text"] = bt15["text"] + 1
        if (bt15["text"]>9):
            bt15["text"]=0

    def bt14_click():
        bt14["text"] = bt14["text"] + 1
        if (bt14["text"]>9):
            bt14["text"]=0

    def bt18_click():
        bt18["text"] = bt18["text"] + 1
        if (bt18["text"]>9):
            bt18["text"]=0

    def bt19_click():
        bt19["text"] = bt19["text"] + 1
        if (bt19["text"]>9):
            bt19["text"]=0

    def bt23_click():
        bt23["text"] = bt23["text"] + 1
        if (bt23["text"]>9):
            bt23["text"]=0

    def bt27_click():
        bt27["text"] = bt27["text"] + 1
        if (bt27["text"]>9):
            bt27["text"]=0

    def bt21_click():
        bt21["text"] = bt21["text"] + 1
        if (bt21["text"]>9):
            bt21["text"]=0

    def bt32_click():
        bt32["text"] = bt32["text"] + 1
        if (bt32["text"]>9):
            bt32["text"]=0

    def bt33_click():
        bt33["text"] = bt33["text"] + 1
        if (bt33["text"]>9):
            bt33["text"]=0

    def bt41_click():
        bt41["text"] = bt41["text"] + 1
        if (bt41["text"]>9):
            bt41["text"]=0
    def bt50_click():
        bt50["text"] = bt50["text"] + 1
        if (bt50["text"]>9):
            bt50["text"]=0
    def bt58_click():
        bt58["text"] = bt58["text"] + 1
        if (bt58["text"]>9):
            bt58["text"]=0

    def bt60_click():
        bt60["text"] = bt60["text"] + 1
        if (bt60["text"]>9):
            bt60["text"]=0

    def bt64_click():
        bt64["text"] = bt64["text"] + 1
        if (bt64["text"]>9):
            bt64["text"]=0

    def bt70_click():
        bt70["text"] = bt70["text"] + 1
        if (bt70["text"]>9):
            bt70["text"]=0

    def bt73_click():
        bt73["text"] = bt73["text"] + 1
        if (bt73["text"]>9):
            bt73["text"]=0

    def bt81_click():
        bt81["text"] = bt81["text"] + 1
        if (bt81["text"]>9):
            bt81["text"]=0

    def time():
        janela['bg'] = 'deepskyblue4'
#(1)
        if(bt4["text"]==lista[1]):
            bt4["bg"]="green"
        else:
            bt4["bg"]="red"
            bt10 ["bg"] = "white"
            bt11 ["bg"] = "white"
            bt13 ["bg"] = "white"
            bt16 ["bg"] = "white"
            bt17 ["bg"] = "white"
            bt28 ["bg"] = "white"
            bt29 ["bg"] = "white"
            bt30 ["bg"] = "white"
            bt31 ["bg"] = "white"
            bt34 ["bg"] = "white"
            bt35 ["bg"] = "white"
            bt36 ["bg"] = "white"
            bt46 ["bg"] = "white"
            bt47 ["bg"] = "white"
            bt48 ["bg"] = "white"
            bt49 ["bg"] = "white"
            bt51 ["bg"] = "white"
            bt52 ["bg"] = "white"
            bt53 ["bg"] = "white"
            bt54 ["bg"] = "white"
            bt55 ["bg"] = "white"
            bt65 ["bg"] = "white"
            bt66 ["bg"] = "white"
            bt67 ["bg"] = "white"
            bt68 ["bg"] = "white"
            bt69 ["bg"] = "white"
            bt71 ["bg"] = "white"
            bt72 ["bg"] = "white"
        if(bt7["text"]==lista[0]):
            bt7["bg"]="green"
        else:
            bt7["bg"]="red"
        if(bt9["text"]==lista[2]):
            bt9["bg"]="green"
        else:
            bt9["bg"]="red"
#(2)
        if(bt12["text"]==lista[3]):
            bt12["bg"]="green"
        else:
            bt12["bg"]="red"
        if(bt14["text"]==lista[8]):
            bt14["bg"]="green"
        else:
            bt14["bg"]="red"
        if(bt15["text"]==lista[5]):
            bt15["bg"]="green"
        else:
            bt15["bg"]="red"
        if(bt18["text"]==lista[6]):
            bt18["bg"]="green"
        else:
            bt18["bg"]="red"
#(3)
        if(bt19["text"]==lista[2]):
            bt19["bg"]="green"
        else:
            bt19["bg"]="red"
        if(bt21["text"]==lista[8]):
            bt21["bg"]="green"
        else:
            bt21["bg"]="red"
        if(bt23["text"]==lista[4]):
           bt23["bg"]="green"
        else:
            bt23["bg"]="red"
        if(bt27["text"]==lista[7]):
            bt27["bg"]="green"
        else:
            bt27["bg"]="red"
#(4)
        if(bt32["text"]==lista[1]):
            bt32["bg"]="green"
        else:
            bt32["bg"]="red"
        if(bt33["text"]==lista[0]):
            bt33["bg"]="green"
        else:
            bt33["bg"]="red"
#(5)
        if(bt41["text"]==lista[6]):
            bt41["bg"]="green"
        else:
            bt41["bg"]="red"
#(6)
        if(bt50["text"]==lista[8]):
            bt50["bg"]="green"
        else:
            bt50["bg"]="red"
#(7)
        if(bt58["text"]==lista[3]):
            bt58["bg"]="green"
        else:
            bt58["bg"]="red"
        if(bt60["text"]==lista[6]):
            bt60["bg"]="green"
        else:
            bt60["bg"]="red"
#(8)
        if(bt64["text"]==lista[4]):
            bt64["bg"]="green"
        else:
            bt64["bg"]="red"
        if(bt70["text"]==lista[6]):
            bt70["bg"]="green"
        else:
            bt70["bg"]="red"
#(9)
        if(bt73["text"]==lista[5]):
            bt73["bg"]="green"
        else:
            bt73["bg"]="red"
        if(bt81["text"]==lista[0]):
            bt81["bg"]="green"
        else:
            bt81["bg"]="red"

# controla o tempo
        def countdown(count):
        # change text in label        
            label['width'] = 5
            label['text'] = count
            label['bg'] = "deepskyblue4"
            label['fg'] = "black"
            z = True
            
# verifica se terminou o jogo
            if(bt4['bg'] == 'green' and
               bt7["bg"]=="green" and
               bt9["bg"]=="green" and
               bt12["bg"]=="green" and
               bt14["bg"]=="green" and
               bt15["bg"]=="green" and
               bt18["bg"]=="green" and
               bt19["bg"]=="green" and
               bt21["bg"]=="green" and
               bt23["bg"]=="green" and
               bt27["bg"]=="green" and
               bt32["bg"]=="green" and
               bt33["bg"]=="green" and
               bt41["bg"]=="green" and
               bt50["bg"]=="green" and
               bt58["bg"]=="green" and
               bt60["bg"]=="green" and
               bt64["bg"]=="green" and
               bt70["bg"]=="green" and
               bt73["bg"]=="green" and
               bt81["bg"]=="green"):
                z = False
                labelim['background']="white"
                labelra['background']="white"
                
# se terminou mostra o nome e o tempo
                # monta a linha com os dados do jogador
                nome = nome_t.get()
                label['bg'] = "white"
                texto.append(str(count))
                texto.append("\n")
                texto.append(nome)
                #grava os dados no arquivo
                text_file = open("Nome e Tempo.txt","w")
                text_file.writelines(texto)
                text_file.close()

# se não terminou
            if z == True:
                janela.after(1000, countdown, count+1)
      
        label = Label(janela,font = ("Chiller", 20))
        label.place(x=25, y=3)
        time.place(x = 1000, y = 3500)

# call countdown first time    
        countdown(0)
        btsolve.place(x=224, y=280)
# root.after(0, countdown, 5)

    def btsolve_click():
        btsolve["text"]="Testar"

#MUDAR COR (21 botoes para alterar)
        if(bt4["text"]==lista[1]):
            bt4["bg"]="green"
        else:
            bt4["bg"]="red"
            bt10 ["bg"] = "white"
            bt11 ["bg"] = "white"
            bt13 ["bg"] = "white"
            bt16 ["bg"] = "white"
            bt17 ["bg"] = "white"
            bt28 ["bg"] = "white"
            bt29 ["bg"] = "white"
            bt30 ["bg"] = "white"
            bt31 ["bg"] = "white"
            bt34 ["bg"] = "white"
            bt35 ["bg"] = "white"
            bt36 ["bg"] = "white"
            bt46 ["bg"] = "white"
            bt47 ["bg"] = "white"
            bt48 ["bg"] = "white"
            bt49 ["bg"] = "white"
            bt51 ["bg"] = "white"
            bt52 ["bg"] = "white"
            bt53 ["bg"] = "white"
            bt54 ["bg"] = "white"
            bt55 ["bg"] = "white"
            bt65 ["bg"] = "white"
            bt66 ["bg"] = "white"
            bt67 ["bg"] = "white"
            bt68 ["bg"] = "white"
            bt69 ["bg"] = "white"
            bt71 ["bg"] = "white"
            bt72 ["bg"] = "white"
            
        if(bt7["text"]==lista[0]):
            bt7["bg"]="green"
        else:
            bt7["bg"]="red"
        if(bt9["text"]==lista[2]):
            bt9["bg"]="green"
        else:
            bt9["bg"]="red"
        if(bt12["text"]==lista[3]):
            bt12["bg"]="green"
        else:
            bt12["bg"]="red"
        if(bt14["text"]==lista[8]):
            bt14["bg"]="green"
        else:
            bt14["bg"]="red"
        if(bt15["text"]==lista[5]):
            bt15["bg"]="green"
        else:
            bt15["bg"]="red"
        if(bt18["text"]==lista[6]):
            bt18["bg"]="green"
        else:
            bt18["bg"]="red"
        if(bt19["text"]==lista[2]):
            bt19["bg"]="green"
        else:
            bt19["bg"]="red"
        if(bt21["text"]==lista[8]):
            bt21["bg"]="green"
        else:
            bt21["bg"]="red"
        if(bt23["text"]==lista[4]):
           bt23["bg"]="green"
        else:
            bt23["bg"]="red"
        if(bt27["text"]==lista[7]):
            bt27["bg"]="green"
        else:
            bt27["bg"]="red"
        if(bt32["text"]==lista[1]):
            bt32["bg"]="green"
        else:
            bt32["bg"]="red"
        if(bt33["text"]==lista[0]):
            bt33["bg"]="green"
        else:
            bt33["bg"]="red"
        if(bt41["text"]==lista[6]):
            bt41["bg"]="green"
        else:
            bt41["bg"]="red"
        if(bt50["text"]==lista[8]):
            bt50["bg"]="green"
        else:
            bt50["bg"]="red"
        if(bt58["text"]==lista[3]):
            bt58["bg"]="green"
        else:
            bt58["bg"]="red"
        if(bt60["text"]==lista[6]):
            bt60["bg"]="green"
        else:
            bt60["bg"]="red"
        if(bt64["text"]==lista[4]):
            bt64["bg"]="green"
        else:
            bt64["bg"]="red"
        if(bt70["text"]==lista[6]):
            bt70["bg"]="green"
        else:
            bt70["bg"]="red"
        if(bt73["text"]==lista[5]):
            bt73["bg"] = "green"
        else:
            bt73["bg"]="red"
        if(bt81["text"]==lista[0]):
            bt81["bg"]="green"
        else:
            bt81["bg"]="red"
        if(bt4['bg']== 'green' and bt7["bg"]=="green" and bt9["bg"]=="green" and bt12["bg"]=="green" and bt14["bg"]=="green" and bt15["bg"]=="green" and bt18["bg"]=="green" and bt19["bg"]=="green" and bt21["bg"]=="green" and bt23["bg"]=="green" and bt27["bg"]=="green" and bt32["bg"]=="green" and bt33["bg"]=="green" and bt41["bg"]=="green" and bt50["bg"]=="green" and bt58["bg"]=="green" and bt60["bg"]=="green" and bt64["bg"]=="green" and bt70["bg"]=="green" and bt73["bg"]=="green" and bt81["bg"]=="green"):
            janela["bg"]= "white"
            labelwin = Label(janela,width = 10, text = "PARABÉNS", fg = "forestgreen", bg = "white", font = ("Chiller",55))
            labelwin.place(x = 113, y = 400)
            botao2.place(x = 233, y = 320)
        else:
            labelwin = Label(janela,width = 10, text = "PARABÉNS", fg = "black", bg = "black", font = ("Chiller",55))
            labelwin.place(x = 10000, y = 401000)

    time = Button(janela,width = 7, text ="Jogar", command = time)
    time.place(x = 10, y = 345)

#BOTOES
#3x3 (1)        
    bt1= Button(janela,width=3, text = lista[4], bg = "white")
    bt2= Button(janela,width=3, text = lista[6], bg = "white")
    bt3= Button(janela,width=3, text = lista[5], bg = "white")
    bt4= Button(janela,width=3, text = 0, bg = "white", command = bt4_click)
    bt5= Button(janela,width=3, text = lista[3], bg = "white")
    bt6= Button(janela,width=3, text = lista[7], bg = "white")
    bt7= Button(janela,width=3, text = 0, bg = "white", command = bt7_click)
    bt8= Button(janela,width=3, text = lista[8], bg = "white")
    bt9= Button(janela,width=3, text = 0, bg = "white", command = bt9_click)
    bt1.place(x=115, y=45)
    bt2.place(x=145, y=45)
    bt3.place(x=175, y=45)
    bt4.place(x=115, y=70)
    bt5.place(x=145, y=70)
    bt6.place(x=175, y=70)
    bt7.place(x=115, y=95)
    bt8.place(x=145, y=95)
    bt9.place(x=175, y=95)
#3x3 (2)
    bt10= Button(janela,width=3, text = lista[7], bg = "gray")
    bt11= Button(janela,width=3, text = lista[0], bg = "gray")
    bt12= Button(janela,width=3, text = 0, bg = "gray", command = bt12_click)
    bt13= Button(janela,width=3, text = lista[2], bg = "gray")
    bt14= Button(janela,width=3, text = 0, bg = "gray", command = bt14_click)
    bt15= Button(janela,width=3, text = 0, bg = "gray", command = bt15_click)
    bt16= Button(janela,width=3, text = lista[1], bg = "gray")
    bt17= Button(janela,width=3, text = lista[4], bg = "gray")
    bt18= Button(janela,width=3, text = 0, bg = "gray", command = bt18_click)
    bt10.place(x=208, y=45)    
    bt11.place(x=238, y=45)
    bt12.place(x=268, y=45)
    bt13.place(x=208, y=70)
    bt14.place(x=238, y=70)
    bt15.place(x=268, y=70)
    bt16.place(x=208, y=95)
    bt17.place(x=238, y=95)
    bt18.place(x=268, y=95)
#3x3 (3)
    bt19= Button(janela,width=3, text = 0, bg = "white", command = bt19_click)
    bt20= Button(janela,width=3, text = lista[1], bg = "white")
    bt21= Button(janela,width=3, text = 0, bg = "white", command = bt21_click)
    bt22= Button(janela,width=3, text = lista[0], bg = "white")
    bt23= Button(janela,width=3, text = 0, bg = "white", command= bt23_click)
    bt24= Button(janela,width=3, text = lista[6], bg = "white")
    bt25= Button(janela,width=3, text = lista[3], bg = "white")
    bt26= Button(janela,width=3, text = lista[5], bg = "white")
    bt27= Button(janela,width=3, text = 0, bg = "white", command =bt27_click)
    bt19.place(x=301, y=45)
    bt20.place(x=331, y=45)
    bt21.place(x=361, y=45)
    bt22.place(x=301, y=70)
    bt23.place(x=331, y=70)
    bt24.place(x=361, y=70)
    bt25.place(x=301, y=95)
    bt26.place(x=331, y=95)
    bt27.place(x=361, y=95)
#3x3 (4)
    bt28= Button(janela,width=3, text = lista[7], bg = "gray")
    bt29= Button(janela,width=3, text = lista[5], bg = "gray")
    bt30= Button(janela,width=3, text = lista[8], bg = "gray")
    bt31= Button(janela,width=3, text = lista[2], bg = "gray")
    bt32= Button(janela,width=3, text = 0, bg = "gray", command =bt32_click)
    bt33= Button(janela,width=3, text = 0, bg = "gray", command =bt33_click)
    bt34= Button(janela,width=3, text = lista[6], bg = "gray")
    bt35= Button(janela,width=3, text = lista[4], bg = "gray")
    bt36= Button(janela,width=3, text = lista[3], bg = "gray")
    bt28.place(x=115, y=122)
    bt29.place(x=145, y=122)
    bt30.place(x=175, y=122)
    bt31.place(x=115, y=147)
    bt32.place(x=145, y=147)
    bt33.place(x=175, y=147)
    bt34.place(x=115, y=172)
    bt35.place(x=145, y=172)
    bt36.place(x=175, y=172)
#3x3 (5)
    bt37= Button(janela,width=3, text = lista[0], bg = "white")
    bt38= Button(janela,width=3, text = lista[2], bg = "white")
    bt39= Button(janela,width=3, text = lista[4], bg = "white")
    bt40= Button(janela,width=3, text = lista[3], bg = "white")
    bt41= Button(janela,width=3, text = 0, bg = "white", command= bt41_click)
    bt42= Button(janela,width=3, text = lista[7], bg = "white")
    bt43= Button(janela,width=3, text = lista[5], bg = "white")
    bt44= Button(janela,width=3, text = lista[1], bg = "white")
    bt45= Button(janela,width=3, text = lista[8], bg = "white")
    bt37.place(x=208, y=122)
    bt38.place(x=238, y=122)
    bt39.place(x=268, y=122)
    bt40.place(x=208, y=147)
    bt41.place(x=238, y=147)
    bt42.place(x=268, y=147)
    bt43.place(x=208, y=172)
    bt44.place(x=238, y=172)
    bt45.place(x=268, y=172)
#3x3 (6)
    bt46= Button(janela,width=3, text = lista[6], bg = "gray")
    bt47= Button(janela,width=3, text = lista[3], bg = "gray")
    bt48= Button(janela,width=3, text = lista[1], bg = "gray")
    bt49= Button(janela,width=3, text = lista[4], bg = "gray")
    bt50= Button(janela,width=3, text = 0, bg = "gray", command=bt50_click)
    bt51= Button(janela,width=3, text = lista[5], bg = "gray")
    bt52= Button(janela,width=3, text = lista[7], bg = "gray")
    bt53= Button(janela,width=3, text = lista[0], bg = "gray")
    bt54= Button(janela,width=3, text = lista[2], bg = "gray")
    bt46.place(x=301, y=122)
    bt47.place(x=331, y=122)
    bt48.place(x=361, y=122)
    bt49.place(x=301, y=147)
    bt50.place(x=331, y=147)
    bt51.place(x=361, y=147)
    bt52.place(x=301, y=172)
    bt53.place(x=331, y=172)
    bt54.place(x=361, y=172)
#3x3 (7)            
    bt55= Button(janela,width=3, text = lista[8], bg = "white")
    bt56= Button(janela,width=3, text = lista[0], bg = "white")
    bt57= Button(janela,width=3, text = lista[1], bg = "white")
    bt58= Button(janela,width=3, text = 0, bg = "white", command = bt58_click)
    bt59= Button(janela,width=3, text = lista[2], bg = "white")
    bt60= Button(janela,width=3, text = 0, bg = "white", command = bt60_click)
    bt61= Button(janela,width=3, text = lista[5], bg = "white")
    bt62= Button(janela,width=3, text = lista[7], bg = "white")
    bt63= Button(janela,width=3, text = lista[4], bg = "white")
    bt55.place(x=115, y=199)
    bt56.place(x=145, y=199)
    bt57.place(x=175, y=199)
    bt58.place(x=115, y=224)
    bt59.place(x=145, y=224)
    bt60.place(x=175, y=224)
    bt61.place(x=115, y=249)
    bt62.place(x=145, y=249)
    bt63.place(x=175, y=249)
#3x3 (8)
    bt64= Button(janela,width=3, text = 0, bg = "gray", command = bt64_click)
    bt65= Button(janela,width=3, text = lista[7], bg = "gray")
    bt66= Button(janela,width=3, text = lista[2], bg = "gray")
    bt67= Button(janela,width=3, text = lista[8], bg = "gray")
    bt68= Button(janela,width=3, text = lista[5], bg = "gray")
    bt69= Button(janela,width=3, text = lista[0], bg = "gray")
    bt70= Button(janela,width=3, text = 0, bg = "gray", command = bt70_click)
    bt71= Button(janela,width=3, text = lista[3], bg = "gray")
    bt72= Button(janela,width=3, text = lista[1], bg = "gray")
    bt64.place(x=208, y=199)
    bt65.place(x=238, y=199)
    bt66.place(x=268, y=199)
    bt67.place(x=208, y=224)
    bt68.place(x=238, y=224)
    bt69.place(x=268, y=224)
    bt70.place(x=208, y=249)
    bt71.place(x=238, y=249)
    bt72.place(x=268, y=249)
#3x3 (9)
    bt73= Button(janela,width=3, text = 0, bg = "white", command = bt73_click)
    bt74= Button(janela,width=3, text = lista[6], bg = "white")
    bt75= Button(janela,width=3, text = lista[3], bg = "white")
    bt76= Button(janela,width=3, text = lista[1], bg = "white")
    bt77= Button(janela,width=3, text = lista[7], bg = "white")
    bt78= Button(janela,width=3, text = lista[4], bg = "white")
    bt79= Button(janela,width=3, text = lista[8], bg = "white")
    bt80= Button(janela,width=3, text = lista[2], bg = "white")
    bt81= Button(janela,width=3, text = 0, bg = "white", command = bt81_click)
    bt73.place(x=301, y=199)
    bt74.place(x=331, y=199)
    bt75.place(x=361, y=199)
    bt76.place(x=301, y=224)
    bt77.place(x=331, y=224)
    bt78.place(x=361, y=224)
    bt79.place(x=301, y=249)
    bt80.place(x=331, y=249)
    bt81.place(x=361, y=249)

    btsolve= Button(janela,width=7, text="Testar", command= btsolve_click)
    btsolve.place(x=4000, y=4000)
    botao2.place(x = 2303, y = 3020)
    
    janela.mainloop()

def bt_click_j1(janela):
    janela.destroy()
    janela2()

def botao2_click_j2(janela):
    janela.destroy()
    janela1()    
janela1()
