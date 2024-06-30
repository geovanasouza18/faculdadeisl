import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root123',
    database='consulta',
)



cursor = conexao
cursor()

# CREATE

#comando = 'INSERT INTO livro (titulo, isbn, ano, editora) VALUES ("Cidade da Lua Crescente", 9786555871708, 2020, "Editora Galera")'
#cursor.execute(comando)
#conexao.commit()
#resultado = cursor.fetchall()


# READ

#comando = 'SELECT * FROM livro'
#cursor.execute(comando)
#resultado = cursor.fetchall()
#print(resultado)


# UPDATE

#comando = 'UPDATE livro SET autor = "Sarah J. Maas" WHERE id = 1'
#cursor.execute(comando)
#conexao.commit()

# DELETE

#comando = 'DELETE FROM livro WHERE id = 6'
#cursor.execute(comando)
#conexao.commit()

cursor.close()
conexao.close()

