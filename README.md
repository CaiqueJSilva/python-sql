Conexão com Banco de Dados SQL Server em Python
Este código demonstra como conectar e inserir dados em um banco de dados SQL Server usando Python com a biblioteca pyodbc.

Funcionalidades principais:
Estabelece conexão com o banco de dados SQL Server

Especifica driver, servidor (DESKTOP-U1525UN) e banco de dados (PythonSQL)

Exibe mensagem de confirmação quando a conexão é bem-sucedida

Insere dados na tabela Vendas:

Cria um registro com:

ID da venda

Nome do cliente ('Caique')

Produto vendido ('PC')

Data da venda ('15/02/2021')

Preço (8000)

Quantidade (1)

Tecnologias utilizadas:
Python

Biblioteca pyodbc (para conexão com SQL Server)

Microsoft SQL Server como SGBD

O código executa um commit para confirmar a transação no banco de dados após a inserção.

