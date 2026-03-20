import customtkinter as ctk
import backend
from PIL import Image


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.back = backend.BackEnd()
        self.frame_register = None
        self.frame_login = None
        self.config_login_screen()
        self.loginscreen()
        self.protocol("WM_DELETE_WINDOW", self.ao_fechar)

        


    #config da janela principal

    def config_login_screen(self):
        self.geometry("700x400")
        self.title("Sistema de Login")
        self.resizable(False, False)
        self.configure(fg_color="#1a1823") 

    def ao_fechar(self):
        self.back.db.desconecta_db()
        self.destroy() 

    def loginscreen(self):

        if self.frame_register != None:
            self.frame_register.place_forget()


        if self.frame_login == None:


            #imagem da janela principal
            img_pillow = Image.open("loginimg.png")
            self.img = ctk.CTkImage(light_image=img_pillow, dark_image=img_pillow, size=(350, 400))
            self.label_img = ctk.CTkLabel(self, text=None, image=self.img)
            self.label_img.grid(row=0, column=0, padx=0)

        


            #frame do formulario de login
            self.frame_login = ctk.CTkFrame(self, width=300, height=350, fg_color="#1e1b2e")
            self.frame_login.place(x=365, y=50)



            #widgets dentro da frame - informações do formulario
            self.login_label_title = ctk.CTkLabel(self.frame_login, text="Faça seu login ou cadastre-se na\nplataforma", font=("Century Gothic Negrito", 18))
            self.login_label_title.grid(row=0, column=0, padx=10, pady=10)



            self.email_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Entre com seu usuário...", corner_radius=15, border_color="#3d405b", fg_color="#161b22", border_width=2)
            self.email_login_entry.grid (row=1, column=0, padx=10, pady=10)
            # Quando clica no campo, a borda fica Azul Vibrante
            self.email_login_entry.bind("<FocusIn>", lambda e: self.email_login_entry.configure(border_color="#3a86ff"))
            # Quando clica fora, a borda volta para o Azul Acinzentado
            self.email_login_entry.bind("<FocusOut>", lambda e: self.email_login_entry.configure(border_color="#3d405b"))




            self.password_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Entre com sua senha...", corner_radius=15, border_color="#3d405b", fg_color="#161b22", border_width=2, show="*")
            self.password_login_entry.grid (row=2, column=0, padx=10, pady=10)
            # Quando clica no campo, a borda fica Azul Vibrante
            self.password_login_entry.bind("<FocusIn>", lambda e: self.password_login_entry.configure(border_color="#3a86ff"))
            # Quando clica fora, a borda volta para o Azul Acinzentado
            self.password_login_entry.bind("<FocusOut>", lambda e: self.password_login_entry.configure(border_color="#3d405b"))




            self.login_button = ctk.CTkButton(self.frame_login, text="Fazer Login".upper(), width=300, corner_radius=20, command=lambda: self.back.logar_usuario(self))
            self.login_button.grid (row=3, column=0, padx=10, pady=10)


            # "OU" entre o login e o registro


            self.bridge_for_register = ctk.CTkLabel(self.frame_login, text="ou".upper(), font=("Century Gothic Negrito", 16), width=300)
            self.bridge_for_register.grid (row=4, column=0, padx=10, pady=10)


            #botão de registro


            self.login_register_button = ctk.CTkButton(self.frame_login, text="registre-se".upper(), width=300, corner_radius=20, command=self.registerscreen)
            self.login_register_button.grid (row=5, column=0, padx=10, pady=10)

        self.frame_login.place(x=365, y=50)

    def registerscreen(self):

        if self.frame_login != None:
            self.frame_login.place_forget()


        if self.frame_register is None:

            #frame do formulario de registro
            self.frame_register = ctk.CTkFrame(self, width=300, height=380, fg_color="#1e1b2e")
            



            self.register_label_title = ctk.CTkLabel(self.frame_register, text="Por favor, insira as informações\nsolicitadas.", font=("Century Gothic Negrito", 15))
            self.register_label_title.grid(row=0, column=0, padx=10, pady=10)



            #widget de usuario

            self.username_register_entry = ctk.CTkEntry(self.frame_register, width=300, placeholder_text="Seu nome de usuário", corner_radius=15, border_color="#3d405b", fg_color="#161b22", border_width=2)
            self.username_register_entry.grid (row=1, column=0, padx=10, pady=10)
            # Quando clica no campo, a borda fica Azul Vibrante
            self.username_register_entry.bind("<FocusIn>", lambda e: self.username_register_entry.configure(border_color="#3a86ff"))
            # Quando clica fora, a borda volta para o Azul Acinzentado
            self.username_register_entry.bind("<FocusOut>", lambda e: self.username_register_entry.configure(border_color="#3d405b"))


            #widget de email

            self.email_register_entry = ctk.CTkEntry(self.frame_register, width=300, placeholder_text="E-Mail", corner_radius=15, border_color="#3d405b", fg_color="#161b22", border_width=2)
            self.email_register_entry.grid (row=2, column=0, padx=10, pady=10)
            # Quando clica no campo, a borda fica Azul Vibrante
            self.email_register_entry.bind("<FocusIn>", lambda e: self.email_register_entry.configure(border_color="#3a86ff"))
            # Quando clica fora, a borda volta para o Azul Acinzentado
            self.email_register_entry.bind("<FocusOut>", lambda e: self.email_register_entry.configure(border_color="#3d405b"))


            #widget de senha


            self.password_register_entry = ctk.CTkEntry(self.frame_register, width=300, placeholder_text="Senha", corner_radius=15, border_color="#3d405b", fg_color="#161b22", border_width=2, show="*")
            self.password_register_entry.grid (row=3, column=0, padx=10, pady=10)
            # Quando clica no campo, a borda fica Azul Vibrante
            self.password_register_entry.bind("<FocusIn>", lambda e: self.password_register_entry.configure(border_color="#3a86ff"))
            # Quando clica fora, a borda volta para o Azul Acinzentado
            self.password_register_entry.bind("<FocusOut>", lambda e: self.password_register_entry.configure(border_color="#3d405b"))


            #confirma senha


            self.confirm_password_register_entry = ctk.CTkEntry(self.frame_register, width=300, placeholder_text="Confirme sua senha", corner_radius=15, border_color="#3d405b", fg_color="#161b22", border_width=2, show="*")
            self.confirm_password_register_entry.grid (row=4, column=0, padx=10, pady=10)
            # Quando clica no campo, a borda fica Azul Vibrante
            self.confirm_password_register_entry.bind("<FocusIn>", lambda e: self.confirm_password_register_entry.configure(border_color="#3a86ff"))
            # Quando clica fora, a borda volta para o Azul Acinzentado
            self.confirm_password_register_entry.bind("<FocusOut>", lambda e: self.confirm_password_register_entry.configure(border_color="#3d405b"))


            #botao de registro


            self.register_registrarse_button = ctk.CTkButton(self.frame_register, text="registre-se".upper(), width=300, corner_radius=20, command=lambda: self.back.cadastrar_usuario(self))
            self.register_registrarse_button.grid (row=5, column=0, padx=10, pady=10)


            # "OU" entre o registro e login


            self.bridge_for_login = ctk.CTkLabel(self.frame_register, text="ou".upper(), font=("Century Gothic Negrito", 15), width=300)
            self.bridge_for_login.grid (row=6, column=0, padx=10, pady=0)



            #botão de voltar para login


            self.register_login_button = ctk.CTkButton(self.frame_register, text="voltar para login".upper(), width=300, corner_radius=20, command=self.loginscreen)
            self.register_login_button.grid (row=7, column=0, padx=10, pady=10)

        self.frame_register.place(x=365, y=14)


    
if __name__ == "__main__":
    app = App()
    app.mainloop()