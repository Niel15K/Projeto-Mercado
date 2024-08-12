
# Menu funcional que guarde os valores dos itens.
# Importações
import os

from Funcao_cliente import Cliente
from Funcao_cliente.funcao2 import cadastrar_item, limpar_prompt, NotaFiscal
print("----------Bem Vindo!-----------")

nomeCliente = input("Digite o seu nome para começar: ")
cliente = Cliente(nomeCliente)

if cliente.nome != '':
    print(f'Olá {cliente.nome}! Obrigado por comprar conosco.')

opção = 0
carrinho_itens = []

while opção != 5:
    limpar_prompt()
    print('''    [ 1 ] Registrar Item no carrinho
    [ 2 ] Visualizar Itens No Carrinho
    [ 3 ] Excluir Itens do Carrinho
    [ 4 ] Finalizar Compra
    [ 5 ] Sair''')
    opção = int(input('>>>>>>>> Qual é a sua opção? '))

    if opção == 1:
        limpar_prompt()
        num_itens = int(input("Digite o numero de itens que deseja registrar: "))
        for i in range(num_itens):
            item = cadastrar_item()
            carrinho_itens.append(item)
            print("--------Item adicionado com sucesso---------")

    elif opção == 2:
        limpar_prompt()
        if carrinho_itens == []:
            print("--------- Você ainda não registrou nenhum item. ---------")
        for item in carrinho_itens:
            print(f"Nome do produto: {item.nomeProduto} | Valor: R${item.valor}")


    elif opção == 3:
        limpar_prompt()
        if len(carrinho_itens ) > 0:
            item_a_remover = input(">>>>> Digite o nome do item a remover: ")
            carrinho_itens = [item for item in carrinho_itens if item.nomeProduto != item_a_remover]
            print(f"O item {item_a_remover} foi removido do carrinho.")
        else:
            print("-------- O carrinho está vazio. -------")

    elif opção == 4:
        limpar_prompt()
        Continuar = input("Digite o 'S' para confirmar e 'N' Para interromper a finalização da compra: ").upper()
        if Continuar == "S":
            nota = NotaFiscal(cliente, carrinho_itens)
            break

        else:
            print("---Você cancelou a finalização de compra.---")

    elif opção == 5:
        limpar_prompt()
        print("Você saiu do programa.")

