import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Função para conectar ao banco de dados
def conectar_bd():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root123',
        database='consulta',
)

# Função para enviar os dados para o banco de dados
def enviar_dados():
    titulo = entry_titulo.get()
    isbn = entry_isbn.get()
    ano = entry_ano.get()
    editora = entry_editora.get()
    autor = entry_autor.get()

    if titulo and isbn and ano and editora and autor:
        try:
            conn = conectar_bd()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO livro (titulo, isbn, ano, editora, autor) VALUES (%s, %s, %s, %s, %s)", (titulo, isbn, ano, editora, autor))
            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo("Sucesso", "Dados enviados com sucesso!")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {err}")
    else:
        messagebox.showwarning("Atenção", "Todos os campos são obrigatórios!")

def pesquisar_dados():
    titulo_pesquisa = entry_pesquisa.get()
    if titulo_pesquisa:
        try:
            conn = conectar_bd()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM livro WHERE titulo = %s", (titulo_pesquisa,))
            resultado = cursor.fetchone()
            if resultado:
                resultado_var.set(f"Titulo: {resultado[1]}\nISBN: {resultado[2]}\nAno: {resultado[3]}\nEditora: {resultado[4]}\nAutor(a): {resultado[5]}")
            else:
                resultado_var.set("Livro não encontrado.")
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {err}")
    else:
        messagebox.showwarning("Atenção", "Por favor, insira o título do livro para a pesquisa.")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Cadastre o livro")
janela.geometry("300x500")

# Label e Entry para o titulo
label_titulo = tk.Label(janela, text="titulo:")
label_titulo.pack()
entry_titulo = tk.Entry(janela)
entry_titulo.pack()

# Label e Entry para o isbn
label_isbn = tk.Label(janela, text="isbn:")
label_isbn.pack()
entry_isbn = tk.Entry(janela)
entry_isbn.pack()

# Label e Entry para o ano
label_ano = tk.Label(janela, text="ano:")
label_ano.pack()
entry_ano = tk.Entry(janela)
entry_ano.pack()

# Label e Entry para a editora
label_editora = tk.Label(janela, text="editora:")
label_editora.pack()
entry_editora = tk.Entry(janela)
entry_editora.pack()

# Label e Entry para o autor
label_autor = tk.Label(janela, text="autor(a):")
label_autor.pack()
entry_autor = tk.Entry(janela)
entry_autor.pack()


# Botão para enviar os dados
botao_enviar = tk.Button(janela, text="Enviar", command=enviar_dados)
botao_enviar.pack(pady=10)

# Linha de separação
tk.Frame(janela, height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=5, pady=10)

# Seção de pesquisa
tk.Label(janela, text="Pesquisar Livro", font=("Helvetica", 14)).pack(pady=10)

# Label e Entry para a pesquisa
tk.Label(janela, text="Titulo:").pack()
entry_pesquisa = tk.Entry(janela)
entry_pesquisa.pack()

# Botão para pesquisar os dados
tk.Button(janela, text="Pesquisar", command=pesquisar_dados).pack(pady=10)

# Área para exibir o resultado
resultado_var = tk.StringVar()
tk.Label(janela, textvariable=resultado_var, wraplength=250).pack(pady=10)

tk.Button(janela, text="sair", command= janela.destroy).pack(pady= 10)

# Executa a aplicação
janela.mainloop()
