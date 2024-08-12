import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk
from datetime import datetime

class Item:
    def __init__(self, codigo, valor, nomeProduto):
        self.codigo = codigo
        self.valor = valor
        self.nomeProduto = nomeProduto

class Cliente:
    def __init__(self, nome):
        self.nome = nome

# Funções auxiliares
def cadastrar_item():
    codigo_do_item = codigo_var.get()
    valor_do_item = valor_var.get()
    nome_do_produto = nome_var.get()

    if not codigo_do_item or not valor_do_item or not nome_do_produto:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return

    try:
        valor_do_item = float(valor_do_item)
    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números no campo de valor.")
        return

    item = Item(codigo_do_item, valor_do_item, nome_do_produto)
    carrinho_itens.append(item)
    atualizar_lista()

def atualizar_lista():
    carrinho_listbox.delete(0, tk.END)
    for item in carrinho_itens:
        carrinho_listbox.insert(tk.END, f"Nome: {item.nomeProduto} | Valor: R${item.valor:.2f}")

def remover_item():
    selecionado = carrinho_listbox.curselection()
    if selecionado:
        carrinho_itens.pop(selecionado[0])
        atualizar_lista()
    else:
        messagebox.showwarning("Atenção", "Selecione um item para remover.")

def finalizar_compra():
    nome_cliente = cliente_nome.get()  # Recupera o nome do cliente da entrada
    if not nome_cliente:
        messagebox.showwarning("Atenção", "O nome do cliente não foi preenchido!")
        return

    if not carrinho_itens:
        messagebox.showwarning("Atenção", "O carrinho está vazio!")
        return

    soma = sum(item.valor for item in carrinho_itens)
    mensagem = f"Nome do cliente: {nome_cliente}\n"
    mensagem += "Lista de Produtos Comprados:\n"
    for item in carrinho_itens:
        mensagem += f"{item.nomeProduto} - R${item.valor:.2f}\n"
    mensagem += f"\nValor total da compra: R${soma:.2f}"

    # Criar e salvar a imagem da nota fiscal
    criar_nota_fiscal(nome_cliente, carrinho_itens, soma)

    # Exibir mensagem
    messagebox.showinfo("Nota Fiscal", mensagem)
    carrinho_itens.clear()
    atualizar_lista()

def criar_nota_fiscal(nome_cliente, itens, valor_total):
    # Criar uma imagem em branco
    img = Image.new('RGB', (600, 800), color=(255, 255, 255))

    # Criar objeto de desenho
    d = ImageDraw.Draw(img)

    # Definir fonte
    try:
        title_font = ImageFont.truetype("arial.ttf", 24)
        item_font = ImageFont.truetype("arial.ttf", 16)
    except IOError:
        title_font = ImageFont.load_default()
        item_font = ImageFont.load_default()

    # Adicionar logo
    try:
        logo = Image.open("images/logo.png")  # Substitua "logo.png" pelo caminho da sua imagem de logo
        logo = logo.resize((200, 100))  # Redimensionar se necessário
        img.paste(logo, (200, 20), logo)
    except FileNotFoundError:
        print("Arquivo da logo não encontrado")

    # Desenhar texto na imagem
    d.text((10, 140), f"Nome do Cliente: {nome_cliente}", fill=(0,0,0), font=item_font)
    y = 180
    for item in itens:
        d.text((10, y), f"{item.nomeProduto} - R${item.valor:.2f}", fill=(0,0,0), font=item_font)
        y += 20
    d.text((10, y), f"Valor Total: R${valor_total:.2f}", fill=(0,0,0), font=item_font)

    # Salvar imagem com o nome do cliente e data
    data_atual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo = f"{nome_cliente}_{data_atual}_Nota.png"
    img.save(nome_arquivo)

def toggle_mode():
    if dark_mode.get():
        # Configurar tema escuro
        app.config(bg="#212529")
        style.configure("TFrame", background="#212529")
        style.configure("TLabel", background="#212529", foreground="#ffffff")
        style.configure("TButton", background="#343a40", foreground="#000070")
        style.configure("TEntry", fieldbackground="#495057", foreground="#000070")
        toggle_btn.config(image=moon_image, style="Dark.TButton")  # Atualizar imagem e estilo do botão
        dark_mode.set(False)
    else:
        # Configurar tema claro
        app.config(bg="#f8f9fa")
        style.configure("TFrame", background="#f8f9fa")
        style.configure("TLabel", background="#f8f9fa", foreground="#000069")
        style.configure("TButton", background="#ffffff", foreground="#000069")
        style.configure("TEntry", fieldbackground="#ffffff", foreground="#000069")
        toggle_btn.config(image=sun_image, style="Light.TButton")  # Atualizar imagem e estilo do botão
        dark_mode.set(True)

# Interface Gráfica
app = tk.Tk()
app.title("Sistema de Vendas")
app.geometry("600x600")

# Centralizar a janela
app.update_idletasks()
window_width = app.winfo_width()
window_height = app.winfo_height()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
app.geometry(f'{window_width}x{window_height}+{x}+{y}')

dark_mode = tk.BooleanVar(value=True)  # Modo escuro por padrão

# Estilo ttk
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12), background="#f8f9fa")
style.configure("TButton", font=("Arial", 10), padding=4)
style.configure("TEntry", font=("Arial", 12))
style.configure("TFrame", background="#ffffff")

# Adicionar estilos personalizados
style.configure("Dark.TFrame", background="#212529")
style.configure("Dark.TLabel", background="#212529", foreground="#ffffff")
style.configure("Dark.TButton", background="#343a40", foreground="#ffffff")
style.configure("Dark.TEntry", fieldbackground="#495057", foreground="#ffffff")

style.configure("Light.TFrame", background="#f8f9fa")
style.configure("Light.TLabel", background="#f8f9fa", foreground="#000069")
style.configure("Light.TButton", background="#ffffff", foreground="#000069")
style.configure("Light.TEntry", fieldbackground="#ffffff", foreground="#000069")

# Frames para organização
frame_cliente = ttk.Frame(app, padding="10")
frame_cliente.grid(row=0, column=0, sticky="ew")

frame_itens = ttk.Frame(app, padding="10")
frame_itens.grid(row=1, column=0, sticky="ew")

frame_carrinho = ttk.Frame(app, padding="10")
frame_carrinho.grid(row=2, column=0, sticky="ew")

frame_acoes = ttk.Frame(app, padding="10")
frame_acoes.grid(row=3, column=0, sticky="ew")

# Cliente
cliente_nome = tk.StringVar()
ttk.Label(frame_cliente, text="Nome do Cliente:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
ttk.Entry(frame_cliente, textvariable=cliente_nome).grid(row=0, column=1, sticky="ew", padx=5, pady=5)

# Itens
codigo_var = tk.StringVar()
valor_var = tk.StringVar()
nome_var = tk.StringVar()

ttk.Label(frame_itens, text="Código do Item:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
ttk.Entry(frame_itens, textvariable=codigo_var).grid(row=1, column=1, sticky="ew", padx=5, pady=5)

ttk.Label(frame_itens, text="Valor do Item:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
ttk.Entry(frame_itens, textvariable=valor_var).grid(row=2, column=1, sticky="ew", padx=5, pady=5)

ttk.Label(frame_itens, text="Nome do Produto:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
ttk.Entry(frame_itens, textvariable=nome_var).grid(row=3, column=1, sticky="ew", padx=5, pady=5)

ttk.Button(frame_itens, text="Cadastrar Item", command=cadastrar_item).grid(row=4, column=0, columnspan=2, pady=10)

# Carrinho
carrinho_itens = []
carrinho_listbox = tk.Listbox(frame_carrinho, width=50, height=10)
carrinho_listbox.grid(row=0, column=0, columnspan=2, pady=10)

ttk.Button(frame_carrinho, text="Remover Item", command=remover_item).grid(row=1, column=0, pady=10)
ttk.Button(frame_carrinho, text="Finalizar Compra", command=finalizar_compra).grid(row=1, column=1, pady=10)

# Alternar tema
toggle_frame = ttk.Frame(app)
toggle_frame.grid(row=0, column=1, padx=10, pady=10, sticky="ne")

# Carregar e redimensionar imagens para o botão de alternância
try:
    sun_image = ImageTk.PhotoImage(Image.open("images/sol.png").resize((24, 24)))  # Imagem do sol para modo claro
    moon_image = ImageTk.PhotoImage(Image.open("images/lua.png").resize((24, 24)))  # Imagem da lua para modo escuro
except FileNotFoundError as e:
    print(f"Arquivo de imagem não encontrado: {e}")
    sun_image = moon_image = None

toggle_btn = ttk.Button(toggle_frame, text="Alternar Tema", command=toggle_mode, image=sun_image, style="Light.TButton")
toggle_btn.grid(row=0, column=0)

app.mainloop()
