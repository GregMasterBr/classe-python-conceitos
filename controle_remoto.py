class ControleRemoto:
    def __init__(self,cor,altura, profundidade,largura,marca):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
        self.marca = marca
    
    def passar_canal(self, botao):
        if botao=="+":
            print("Aumentar o canal")
        else:
            print("Diminuir o canal")
    
    def volume():
        pass
    
    def abrirNetflix():
        pass

    def desligarTV():
        pass


controle_remoto = ControleRemoto("preto","10cm","2cm","4cm","AOC")


print(controle_remoto.cor)

print(controle_remoto.passar_canal("+"))
print(controle_remoto.passar_canal("-"))

