import tkinter as tk
from tkinter import messagebox, ttk
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

# Função para pesquisar os dados no banco de dados
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

# Função para listar todos os dados cadastrados
def listar_dados():
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM livro")
        resultados = cursor.fetchall()
        if resultados:
            # Criando uma nova janela para listar os dados
            lista_janela = tk.Toplevel(janela)
            lista_janela.title("Lista de Livros Cadastrados")
            lista_janela.geometry("800x400")

            # Cabeçalhos das colunas
            headers = ["Título", "ISBN", "Ano", "Editora", "Autor"]

            # Treeview para exibir os dados como tabela
            tree = ttk.Treeview(lista_janela, columns=headers, show="headings")
            tree.pack(fill=tk.BOTH, expand=True)

            # Configurando os cabeçalhos das colunas
            for header in headers:
                tree.heading(header, text=header)
                tree.column(header, width=150, anchor=tk.CENTER)

            # Inserindo os dados na tabela
            for resultado in resultados:
                tree.insert("", tk.END, values=resultado[1:])

        else:
            messagebox.showinfo("Informação", "Não há livros cadastrados.")

        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {err}")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Cadastre o livro")
janela.geometry("600x600")


# Label e Entry para o titulo
label_titulo = tk.Label(janela, text="Título:")
label_titulo.pack()
entry_titulo = tk.Entry(janela)
entry_titulo.pack()

# Label e Entry para o isbn
label_isbn = tk.Label(janela, text="ISBN:")
label_isbn.pack()
entry_isbn = tk.Entry(janela)
entry_isbn.pack()

# Label e Entry para o ano
label_ano = tk.Label(janela, text="Ano:")
label_ano.pack()
entry_ano = tk.Entry(janela)
entry_ano.pack()

# Label e Entry para a editora
label_editora = tk.Label(janela, text="Editora:")
label_editora.pack()
entry_editora = tk.Entry(janela)
entry_editora.pack()

# Label e Entry para o autor
label_autor = tk.Label(janela, text="Autor(a):")
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
tk.Label(janela, text="Título:").pack()
entry_pesquisa = tk.Entry(janela)
entry_pesquisa.pack()

# Botão para pesquisar os dados
tk.Button(janela, text="Pesquisar", command=pesquisar_dados).pack(pady=10)

# Área para exibir o resultado da pesquisa
resultado_var = tk.StringVar()
resultado_label = tk.Label(janela, textvariable=resultado_var, wraplength=300)
resultado_label.pack(pady=10)

# Linha de separação
tk.Frame(janela, height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=5, pady=10)

# Botão para listar todos os dados
tk.Button(janela, text="Listar Todos", command=listar_dados).pack(pady=10, padx=30)

# Botão para sair
tk.Button(janela, text="Sair", command=janela.destroy).pack(pady=10)

# Executa a aplicação
janela.mainloop()
