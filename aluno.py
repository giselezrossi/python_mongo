from conexao import MongoConnect

class Aluno():

    def save(self, name, sobrenome, profissao):
        conexao = MongoConnect()
        aluno = {'name': name, 'sobrenome': sobrenome, 'profissao': profissao}
        conexao.save(aluno)
