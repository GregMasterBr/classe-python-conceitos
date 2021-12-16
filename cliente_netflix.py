class Cliente():
    def __init__(self,nome,email,plano,ativo=True):
        self.nome = nome
        self.email = email
        self.lista_planos = ["basic","premium"]

        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception("Plano inválido")
        self.ativo = ativo

    def adicionar(self):
        pass


    def mudar_plano(self,novo_plano):
        if novo_plano in self.lista_planos:
            self.plano=novo_plano
        else:
            raise Exception("Plano inválido")

    
    def ver_filme(self,filme,plano_filme):
        if self.plano == plano_filme:
            print(f"Ver filme {filme}")
        elif self.plano=="premium":
            print(f"Ver filme {filme}")
        elif self.plano=="basic" and plano_filme=="premium":
            print(f"Você não pode assistir esse filme {filme}. Migre seu plano para o Premium")
        else:
            print("Plano inválido")

cliente = Cliente("Greg","greg@gmail.com","basic",True)

print(cliente.plano)
cliente.mudar_plano("premium")
print(cliente.plano)

cliente.ver_filme("Zorro","basic")
cliente.ver_filme("Zorro","premium")
cliente.mudar_plano("basic")
cliente.ver_filme("Zorro","premium")
cliente.ver_filme("Zorro","master")
