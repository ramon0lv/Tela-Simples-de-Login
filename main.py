## MINHA PRIMEIRA TELA DE LOGIN by Ramon
## Inspiração do canal Usando Python

from tkinter import *
from tkinter import messagebox

# CORES
co0 = "#f0f3f5"  # Preto / Black
co1 = "#feffff"  # Branco / White
co2 = "#033333"  # Verde escuro / Dark green
co3 = "#38576b"  # Valor / Value
co4 = "#403d3d"  # Letras / Letters

# Função para reiniciar o programa
def reiniciar_programa():
    janela.destroy()
    main()

def main():
    global janela, frame_cima, frame_baixo, e_nome, e_pass

    # Minha Janela
    janela = Tk()
    janela.title('Login')
    janela.geometry('310x300')
    janela.configure(background=co1)
    janela.resizable(width=FALSE, height=FALSE)

    # Divisão da Janela
    frame_cima = Frame(janela, width=310, height=50, bg=co1, relief='flat')
    frame_cima.grid(row=0, column=0, padx=0, pady=1, sticky=NSEW)

    frame_baixo = Frame(janela, width=310, height=250, bg=co1, relief='flat')
    frame_baixo.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)

    # Config Frame de cima
    l_nome = Label(frame_cima, text='LOGIN', anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
    l_nome.place(x=105, y=5)

    l_linha = Label(frame_cima, text='', width=275, anchor=NE, font=('Ivy 1'), bg=co2, fg=co4)
    l_linha.place(x=10, y=45)

    credenciais = ['test', '123']

    # Função de verificação de senha
    def verificar_senha():
        nome = e_nome.get()
        senha = e_pass.get()

        if nome == 'admin' and senha == 'admin':
            messagebox.showinfo('Login', 'Seja Bem Vindo!')
        elif credenciais[0] == nome and credenciais[1] == senha:
            messagebox.showinfo('Login', 'Seja Bem Vindo, ' + credenciais[0] + '!')
            # Mudança do Frame
            for Widget in frame_baixo.winfo_children():
                Widget.destroy()
            for Widget in frame_cima.winfo_children():
                Widget.destroy()
            nova_janela()
        else:
            messagebox.showwarning('Falha', 'Verifique Login ou Senha!')

    # Função após verificação
    def nova_janela():
        # Limpar os widgets do frame_baixo
        for widget in frame_baixo.winfo_children():
            widget.destroy()

        # Configurar novo rótulo no frame_cima
        l_nome_cima = Label(frame_cima, text='Usuário: ' + credenciais[0], anchor=NE, font=('Ivy 8'), bg=co1, fg=co4)
        l_nome_cima.place(x=5, y=5)

        # Configurar novo rótulo e entrada no frame_baixo
        l_nome_nova = Label(frame_baixo, text='Aproveite ' + credenciais[0] + '!', anchor=NW, font=('Ivy 15'), bg=co1, fg=co4)
        l_nome_nova.place(x=10, y=10)

        # Botão de Logout
        b_logout = Button(frame_baixo, command=reiniciar_programa, text='LOGOUT', width=7, height=1, font=('Ivy 8 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge', borderwidth=5)
        b_logout.place(x=215, y=200)

    # Config Frame de baixo
    l_nome_baixo = Label(frame_baixo, text='Nome', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome_baixo.place(x=135, y=20)
    e_nome = Entry(frame_baixo, width=25, justify='left', font=('', 15), highlightthickness=1, relief='solid')
    e_nome.place(x=14, y=50)

    l_pass = Label(frame_baixo, text='Senha', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_pass.place(x=135, y=95)
    e_pass = Entry(frame_baixo, width=25, justify='left', show='*', font=('', 15), highlightthickness=1, relief='solid')
    e_pass.place(x=14, y=130)

    # Botão
    b_confirmar = Button(frame_baixo, command=verificar_senha, text='ENTRAR', width=39, height=2, font=('Ivy 8 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge', borderwidth=5)
    b_confirmar.place(x=15, y=180)

    janela.mainloop()

main()
