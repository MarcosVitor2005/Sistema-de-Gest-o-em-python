#importando sqlite3
import  sqlite3 as lite

#criando e fazendo conexão com banco de dados
con = lite.connect('dados.db')


# criando tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE inventorio( id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, local TEXT, descricao TEXT, marca TEXT, data_da_compra DATA, valor_da_compra DECIMAL, serie TEXT, imagem TEXT)")