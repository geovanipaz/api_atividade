from models import Pessoas, db_session


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

if __name__=='__main__':
    #insere_pessoas()
    excluir_pessoa()
    consulta_pessoas()
    #altera_pessoa()