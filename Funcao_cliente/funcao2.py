class Item:
    def __init__(self, codigo, valor, nomeProduto):
        self.codigo = codigo
        self.valor = valor
        self.nomeProduto = nomeProduto

def cadastrar_item():
    print("Chamando cadastrar item()")
    codigo_do_item = input("Digite o código do item: ")

    while True:
        valor_do_item = input("Digite o valor do item: ")
        try:
            valor_do_item = float(valor_do_item)
            break  # Se a conversão for bem-sucedida, sai do loop
        except ValueError:
            print("Digite apenas números, por favor.")

    nome_do_produto = input("Digite o nome do item: ")
    item = Item(codigo_do_item, valor_do_item, nome_do_produto)
    return item

def carrinho(item):
    print("Adicionando item ao carrinho:", item.nomeProduto)

import os

def limpar_prompt():
    os.system("cls")

def NotaFiscal(cliente, carrinho_itens):
    print(f"Nota Fiscal\nNome do cliente: {cliente.nome}")
    print("Lista de Produtos Comprados: ")
    for item in carrinho_itens:
        print(f"Nome do produto: {item.nomeProduto} | Valor: R${item.valor}")
    soma = sum(item.valor for item in carrinho_itens)
    print(f"Valor total da compra: {soma}")
    print("Obrigado por comprar com nosso sistema de automação de vendas\n--------Volte sempre--------")

# Exemplo de uso (adicione seu próprio código para definir a classe `Cliente` e manipular o fluxo completo)
# cliente = Cliente("Nome do Cliente")
# carrinho_itens = []
# item = cadastrar_item()
# carrinho_itens.append(item)
# NotaFiscal(cliente, carrinho_itens)
