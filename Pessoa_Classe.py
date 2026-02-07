class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}'

    @property
    def saudação(self):
        if self.profissao:
            return f'Olá, sou {self.nome}! Trabalho como {self.profissao}.'
        else:
            return f'Olá, sou {self.nome}!'
        
    def aniversario(self):
        self.idade += 1

pessoa1 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
pessoa3 = Pessoa(nome='Jaque', idade=22)

print("Informações Iniciais:")
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

pessoa1.aniversario()
pessoa2.aniversario()

print("Informações após aniversário:")
print(pessoa1)
print(pessoa3)
print()


print(pessoa1.saudação)
print(pessoa2.saudação)
print(pessoa3.saudação)
    