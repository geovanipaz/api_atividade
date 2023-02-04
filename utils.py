from models import Pessoas, db_session, Usuarios


def insere_pessoas():
    pessoa = Pessoas(nome="geo", idade=29)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome="geo").first()
    #print(pessoa)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome="geo").first()
    pessoa.idade = 21
    pessoa.save()

def excluir_pessoa():
    pessoa = Pessoas.query.filter_by(nome="geo").first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__=='__main__':
    insere_usuario('rafael','123')
    insere_usuario('galleani','321')
    consulta_todos_usuarios()
    #insere_pessoas()
    #excluir_pessoa()
    consulta_pessoas()
    #altera_pessoa()