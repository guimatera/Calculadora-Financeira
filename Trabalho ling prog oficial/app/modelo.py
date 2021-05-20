class usuario():
    def __init__ (self, user, senha):
        self.user = user
        self.senha = senha

    def set_password(self, senha):
        self.senha = senha

    def set_user(self, user):
        self.user = user

    def get_password(self):
        return self.senha

    def get_user(self):
        return self.user

        
    def save(self):
        registro = self.user + '-'+ self.senha +'\n'
        arquivo = open('cadastro.txt','a')
        arquivo.writelines(registro)

