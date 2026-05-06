from tkinter import *
from tkinter import ttk
from tkinter import messagebox

janela = Tk()
janela.title("FORMULÁRIO DE CADASTRO DE CLIENTE")
janela.geometry("800x600")


abas = ttk.Notebook(janela)
abas.pack(fill="both", expand=True)

aba1 = Frame(abas)
abas.add(aba1, text="Cadastro do Paciente")

aba2 = Frame(abas)
abas.add(aba2, text="Pacientes Cadastrados")

def cadastrar():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    data = entry_data.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    convenio = entry_convenio.get()
    contato = entry_contato.get()

    if nome == "" or cpf == "" or data == "" or telefone == "" or email == "" or convenio == "" or contato == "":
        messagebox.showwarning("Erro", "Preencha todos os campos!")
    else:
        tabela.insert("",END, values=(nome,cpf,data,telefone,email,convenio,contato))
    entry_nome.delete(0,END)
    entry_cpf.delete(0,END)
    entry_data.delete(0,END)
    entry_telefone.delete(0,END)
    entry_email.delete(0,END)
    entry_convenio.delete(0,END)
    entry_contato.delete(0,END)

messagebox.showinfo("Sucesso", "Paciente Cadastrado")

Label(aba1, text="Nome Completo").pack(pady=5)
entry_nome= Entry(aba1, width=40)
entry_nome.pack()

Label(aba1, text="CPF").pack(pady=5)
entry_cpf= Entry(aba1, width=40)
entry_cpf.pack()

Label(aba1, text="Data de Nascimeto").pack(pady=5)
entry_data= Entry(aba1, width=40)
entry_data.pack()

Label(aba1, text="Telefone").pack(pady=5)
entry_telefone= Entry(aba1, width=40)
entry_telefone.pack()

Label(aba1, text="Email").pack(pady=5)
entry_email= Entry(aba1, width=40)
entry_email.pack()

Label(aba1, text="Convênio/sus").pack(pady=5)
entry_convenio= Entry(aba1, width=40)
entry_convenio.pack()

Label(aba1, text="contato de emergência").pack(pady=5)
entry_contato= Entry(aba1, width=40)
entry_contato.pack()

Button(
    aba1,
    text="cadastrar",
    bg="green",
    fg="white",
    width=20,
    command=cadastrar
    ).pack(pady=20)

colunas=("nome","cpf","data","telefone","email","convenio","contato")

tabela=ttk.Treeview(
    aba2,
    columns=colunas,
    show="headings"
)

for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, width=151)

tabela.pack(fill="both", expand=True, pady=20)

janela.mainloop()