import tkinter as tk
from tkinter import messagebox

def calcular_media():
    try:
        # Pega os valores e converte para float (substitui vírgula por ponto caso o usuário digite)
        n1 = float(nota1.get().replace(',', '.'))
        n2 = float(nota2.get().replace(',', '.'))
        n3 = float(nota3.get().replace(',', '.'))
        
        media = (n1 + n2 + n3) / 3
        resultado.config(text=f"Média: {media:.2f}")

        nome_ = nome.get().strip()
        if not nome_:
            nome_ = "Aluno(a)"

        if media >= 7:
            situacao.config(text=f'{nome_} PASSOU DIRETO', fg='#2e7d32') # Verde
        elif media >= 5:
            situacao.config(text=f'{nome_} ESTÁ EM RECUPERAÇÃO', fg='#ef6c00') # Laranja
        else:
            situacao.config(text=f'{nome_} NÃO PASSOU...', fg='#c62828') # Vermelho
            
    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor, preencha todas as notas com números válidos!")

# Configuração da Janela Principal
janela = tk.Tk()
janela.title("Sistema Escolar XYZ")
janela.geometry('380x450')
janela.config(bg='#f4f4f9')
janela.resizable(False, False)

# Cores e fontes padrão
FONTE_TITULO = ("Arial", 14, "bold")
FONTE_TEXTO = ("Arial", 10)
COR_BG = '#f4f4f9'

# Título
titulo = tk.Label(janela, text='SISTEMA ESCOLA XYZ', font=FONTE_TITULO, bg=COR_BG, fg='#333')
titulo.pack(pady=15)

# Frame para o formulário (organização)
frame_form = tk.Frame(janela, bg=COR_BG)
frame_form.pack(pady=5)

# Nome
tk.Label(frame_form, text='Nome do Aluno:', font=FONTE_TEXTO, bg=COR_BG).pack(anchor='w')
nome = tk.Entry(frame_form, font=FONTE_TEXTO, width=30)
nome.pack(pady=(0, 10))

# Nota 1
tk.Label(frame_form, text='Nota 1:', font=FONTE_TEXTO, bg=COR_BG).pack(anchor='w')
nota1 = tk.Entry(frame_form, font=FONTE_TEXTO, width=30)
nota1.pack(pady=(0, 10))

# Nota 2
tk.Label(frame_form, text='Nota 2:', font=FONTE_TEXTO, bg=COR_BG).pack(anchor='w')
nota2 = tk.Entry(frame_form, font=FONTE_TEXTO, width=30)
nota2.pack(pady=(0, 10))

# Nota 3
tk.Label(frame_form, text='Nota 3:', font=FONTE_TEXTO, bg=COR_BG).pack(anchor='w')
nota3 = tk.Entry(frame_form, font=FONTE_TEXTO, width=30)
nota3.pack(pady=(0, 15))

# Botão Calcular
botao = tk.Button(janela, text='Calcular Média', font=("Arial", 10, "bold"), bg='#1976d2', fg='white', width=20, command=calcular_media)
botao.pack(pady=5)

# Resultados
resultado = tk.Label(janela, text='', font=("Arial", 11, "bold"), bg=COR_BG, fg='#333')
resultado.pack(pady=10)

situacao = tk.Label(janela, text='', font=("Arial", 11, "bold"), bg=COR_BG)
situacao.pack(pady=5)

janela.mainloop()