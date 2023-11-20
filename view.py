import sqlite3 as lite

con = lite.connect('dados.db')

#CRUD

# inserir dados (CREATE) 
def inserir_form(i):
    with con:
        cur = con.cursor()
        # não precisa inserir o id, pois insere altomaticamente no banco
        query = "INSERT INTO inventorio(nome,local, descricao, marca, data_da_compra, valor_da_compra, serie, imagem) VALUES(?,?,?,?,?,?,?,?)"
        cur.execute(query,i)


# ver todos os dados(READ)
def ver_form():
    ver_dados = []
    with con:
        cur = con.cursor()
        # não precisa inserir o id, pois insere altomaticamente no banco
        query = "SELECT * FROM inventorio"
        cur.execute(query)


        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados


# ver todos os dados(READ)
def ver_item(id): 
    ver_dados_individual = []
    with con:
        cur = con.cursor()
        # não precisa inserir o id, pois insere altomaticamente no banco
        query = "SELECT * FROM inventorio WHERE  id=?"
        cur.execute(query,id)


        rows = cur.fetchall()
        for row in rows:
            ver_dados_individual.append(row)

    return ver_dados_individual

print(ver_item([1]))


# atualizar dados (UPDATE) 
def atulizar_form(i):
    with con:
        cur = con.cursor()
        # não precisa inserir o id, pois insere altomaticamente no banco
        query = "UPDATE inventorio SET nome=?,local=?, descricao=?, marca=?, data_da_compra=?, valor_da_compra=?, serie=?, imagem=? WHERE id=?"
        cur.execute(query,i)


# deletar dados(DELETE)
def deletar_form(i):
    deletar_dados = str(1)
    with con:
        cur = con.cursor()
        # não precisa inserir o id, pois insere altomaticamente no banco
        query = "DELETE FROM inventorio WHERE id=?"
        cur.execute(query,i)
