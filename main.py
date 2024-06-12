import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

# Função para gerar o QR Code
def generate_qr_code():
    # Obtém o texto inserido pelo usuário
    text = entry.get()
    
    # Verifica se o campo de texto não está vazio
    if text:
        # Cria um objeto QRCode com algumas configurações
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        # Adiciona o texto ao QRCode e gera a imagem
        qr.add_data(text)
        qr.make(fit=True)

        # Converte a imagem do QRCode para um formato adequado para o Tkinter
        img = qr.make_image(fill='black', back_color='white')
        img = img.resize((200, 200), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)

        # Exibe a imagem do QRCode na interface
        qr_label.config(image=img)
        qr_label.image = img
    else:
        # Mostra uma mensagem de aviso se o campo de texto estiver vazio
        messagebox.showwarning("Entrada vazia", "Por favor, insira algum texto para gerar o QR Code.")

# Configurações da janela principal
root = tk.Tk()
root.title("Gerador de QR Code")  # Define o título da janela
root.geometry("400x500")  # Define o tamanho da janela
root.configure(bg="#121212")  # Define a cor de fundo para um tom mais escuro

# Título da aplicação
title_label = tk.Label(root, text="Gerador de QR Code", font=("Helvetica Neue", 24, "bold"), bg="#121212", fg="#ffffff")
title_label.pack(pady=20)

# Frame para a entrada de texto
input_frame = tk.Frame(root, bg="#121212")
input_frame.pack(pady=10)

# Rótulo para a entrada de texto
entry_label = tk.Label(input_frame, text="Insira o texto:", font=("Helvetica Neue", 16, "italic"), bg="#121212", fg="#ffffff")
entry_label.grid(row=0, column=0, padx=10)

# Campo de entrada de texto
entry = tk.Entry(input_frame, width=30, font=("Helvetica Neue", 14), bg="#333333", fg="#ffffff", insertbackground="#ffffff", relief="flat")
entry.grid(row=0, column=1, padx=10)

# Frame para os botões
button_frame = tk.Frame(root, bg="#121212")
button_frame.pack(pady=20)

# Botão para gerar o QR Code
generate_button = tk.Button(button_frame, text="Gerar QR Code", command=generate_qr_code, font=("Helvetica Neue", 14, "bold"), bg="#4CAF50", fg="white", relief="flat", padx=10, pady=5, activebackground="#45a049", borderwidth=0, highlightthickness=0)
generate_button.grid(row=0, column=0, padx=10)

# Adicionando efeitos de mouse ao botão
generate_button.configure(highlightbackground="#4CAF50", highlightcolor="#4CAF50", highlightthickness=2)
generate_button.bind("<Enter>", lambda e: e.widget.configure(bg="#45a049"))  # Muda a cor ao passar o mouse
generate_button.bind("<Leave>", lambda e: e.widget.configure(bg="#4CAF50"))  # Restaura a cor original ao tirar o mouse

# Label para exibir o QR Code gerado
qr_label = tk.Label(root, bg="#121212")
qr_label.pack(pady=20)

# Rodapé da aplicação
footer_label = tk.Label(root, text="Feito por Alisson Giovane", font=("Helvetica Neue", 12), bg="#121212", fg="#888888")
footer_label.pack(pady=10)

# Inicia a aplicação
root.mainloop()
