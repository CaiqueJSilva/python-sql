import pyodbc 

dados_conexao = (
    "Driver={Sql Server};"
    "Server=DESKTOP-U1525UN;"
    "Database=PythonSQL;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexao bem sucedida")
                    
cursor = conexao.cursor()

comando = """INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    (1, 'Caique', 'PC', '15/02/2021', 8000, 1)"""

cursor.execute(comando)
cursor.commit ()
