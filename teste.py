from comunidadeimpressionadora import app, database
# Utilizando o contexto da aplicação Flask
with app.app_context():
    # Dropa todas as tabelas (apaga os dados)
    database.drop_all()  
    # Cria as tabelas novamente
    database.create_all()
    print("Base de Dados criada")
