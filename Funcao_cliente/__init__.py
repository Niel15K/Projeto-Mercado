
class Cliente:
    def __init__(self, nome):
        self.nome = nome

if __name__ == "__main__":
    print('-----------BEM VINDO!-------------')
    cliente = input("Digite o seu nome para começar: ")
    clienteNovo = Cliente(cliente)
    if clienteNovo.nome != 0:
        print(f'Olá {clienteNovo.nome} Obrigado por comprar conosco.')

