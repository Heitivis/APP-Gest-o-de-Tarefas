import customtkinter as ctk
import tkinter
from tkinter import *
from tkinter import messagebox

#função
def add ():
    tarefa= add_tarefa.get()
    if tarefa: 
        lista_tarefas.insert(0,tarefa)
        add_tarefa.delete(0,END)
        salvar_tarefas()
    else :
        messagebox.showerror('Erro', 'Digite um Tarefa!')
def deleta ():
    selecionada  = lista_tarefas.curselection()
    if selecionada:
        lista_tarefas.delete(selecionada)
        salvar_tarefas()
    else:
        messagebox.showerror('erro', 'Selecione uma tarefa ')
def salvar_tarefas():
    with open('tarefas.txt','w') as t:
        terefas = lista_tarefas.get(0,END) 
        for x in terefas: 
            t.write(x+"\n")

def carreagar_tarefas():
   try:
    with open('tarefas.txt','r') as t:
        tarefas = t.readlines()
        for x in tarefas:
            lista_tarefas.insert(0,x.strip())        
   except: 
       messagebox.showinfo("APP","Bem vindo ao APP Tarefas.")    
#---


ctk.set_appearance_mode('dark')
janela= ctk.CTk()
janela.minsize(350,500)
janela.maxsize(350,500)
janela.title('app tarefas v1.0')

ctk.CTkLabel(janela, text='App Tarefas V1.0 ', text_color='green', font=('arial',30,'bold')).pack(pady=10)

bt_adicionar=ctk.CTkButton(janela,text='Adicionar Tarefa',fg_color='green', text_color='white',font=('arial',16,'bold'),hover_color='darkgreen',
                           command=add)
bt_adicionar.place(x=20,y=70)

bt_remover=ctk.CTkButton(janela,text='Remover Tarefa',fg_color='red', text_color='white',font=('arial',16,'bold'), hover_color='darkred',
                         command=deleta)
bt_remover.place(x=185,y=70)
 
add_tarefa=ctk.CTkEntry(janela, width=300, height=30, placeholder_text='Digite uma Nova Tarefa')
add_tarefa.place(x=25,y=130)

lista_tarefas = Listbox(janela,width=27,height=12,bg='#363636',fg='white', font=('arial',15))
lista_tarefas.place(x=28,y=200)




carreagar_tarefas()

janela.mainloop()
