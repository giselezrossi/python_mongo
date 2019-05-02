from pymongo import MongoClient
#pip install pymongo

class MongoConnect():

    def save(self, json):
        try:
            cliente = MongoClient('localhost', 27017)
            banco = cliente.teste
            aluno = banco.aluno
            aluno_id = aluno.insert_one(json).inserted_id
        except Exception as e:
            print("problema ao salvar registro")
            print(json)
            print(e)
