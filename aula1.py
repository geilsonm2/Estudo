#Class
#Syntaxe

#Atributos
#Marca, Memoria Ram, Placa de Video 

#Métodos
#Ligar, Desligar, Exibir Configurações
class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video): #Construtor que permite criar a funcionalidade inicial da classe
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
    pass

    def Ligar(self):
        print('Ligando')
    
    def Desligar(self):
        print('Desligando')

    def ExibirInformacoesDesteComputador(self):
        print(self.marca,self.memoria_ram,self.placa_de_video)

computador1 = Computador ('Acer', '16gb', 'ATM')
computador1.Ligar ()
computador1.Desligar ()
computador1.ExibirInformacoesDesteComputador()


# Class Carro com no minimo 3 propriedades e 3 metodos|

class Carro:
    def __init__(self, modelo, marca, ano):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
    pass

    def move(self):
        print ('Andando')

    def stop(self):
        print ('Parando')

    def exibindoInformacoes(self):
        print (self.modelo,self.marca,self.ano)

carro1 = Carro ('Uno' , 'Fiat', '1988')
carro1.move()
carro1.stop()
carro1.exibindoInformacoes()

            
      







# computador1 = Computador ('Asus', '8gb', 'Nvidia')
# computador2 = Computador ('Dell', '10gb', 'GeForce')
# computador3 = Computador ('Acer', '16gb', 'ATM')

# print(computador1.marca,computador1.memoria_ram, computador1.placa_de_video)
# print(computador2.marca,computador2.memoria_ram, computador2.placa_de_video)
# print(computador3.marca,computador3.memoria_ram, computador3.placa_de_video)