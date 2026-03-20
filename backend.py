import db
from tkinter import messagebox

class BackEnd():
    def __init__(self):

        self.db = db.DataBase()

    def logar_usuario(self, frontend):
        email_login = frontend.email_login_entry.get()
        password_login = frontend.password_login_entry.get()

        if email_login == "" or password_login == "":
            messagebox.showwarning("Sistema de login", "Preencha todos os campos!")
            return

        self.db.cursor.execute("""SELECT * FROM usuarios WHERE email = %s AND senha = %s""", (email_login, password_login))

        resultado = self.db.cursor.fetchone()

        if resultado:
                messagebox.showinfo ("Login", "Bem-vindo ao sistema!")
                frontend.after(1000, frontend.destroy)
                
        else:
                messagebox.showerror ("Erro", "Email ou senha incorretos!")
                return
    

    def cadastrar_usuario(self, frontend):
        username_register = frontend.username_register_entry.get()
        email_register = frontend.email_register_entry.get()
        password_register = frontend.password_register_entry.get()
        confirm_password_register = frontend.confirm_password_register_entry.get()

        if username_register == "" or email_register == "" or password_register == "" or confirm_password_register == "" :
            messagebox.showwarning("Sistema de Login", "Atenção: Todos os campos são obrigatórios!")
            return
        
        if password_register != confirm_password_register :
            messagebox.showerror("Erro", "Erro: A senha e sua confirmação não coincidem.")
            return
        
        self.db.cursor.execute("""
            SELECT * FROM usuarios WHERE email = %s""", (email_register,))
        
        resultado = self.db.cursor.fetchone()

        if resultado:
            messagebox.showerror("Erro", "Endereço de email ja está em uso!")
            return

        self.db.cursor.execute("""
                               
            INSERT INTO usuarios (username, email, senha)
            VALUES (%s, %s, %s)""", (username_register, email_register, password_register))
        
        self.db.conn.commit()
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        self.limpar_campos_registro(frontend)

    def limpar_campos_registro(self, frontend):
        frontend.username_register_entry.delete(0, 'end')
        frontend.email_register_entry.delete(0, 'end')
        frontend.password_register_entry.delete(0, 'end')
        frontend.confirm_password_register_entry.delete(0, 'end')
