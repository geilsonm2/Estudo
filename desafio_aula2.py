inscritos = ['jhonatan',
'Patricio Silva',
'Kid Boy 3000',
'Ricardo Piedade',
'Victor Ravagnani',
'Eder Macario',
'Luiz Guilherme',
'Lucimar Chiamulera',	
'vinicius queiroz',
'Jonatas Alves',
'Giuliano Richards',
'Hugo Marques',
'Marcelo M',
'Luiz Alberto Araujo',
'Niwber Cavalcante',	
'Andre Neves',
'Borges	Borges',
'Alex Marciel',
'Davi Adelino',
'90Tão Games',
'jose valderi',
'Márcio Lopes',
'Mikael',
'Tálisson Neiva',
]

# Desafio 1 - Exiba todos os nomes dos inscritos que estão no arquivo inscritos.txt no console
# with open ('inscritos.txt', 'r') as arquivo2:
#     for valor in inscritos:
#         print(valor + '\n')
# Desafio 2 - Adicione o seu nome na lista de inscritos e depois todos os nomes que estão no arquivo inscritos.txt no console

# with open ('inscritos.txt', 'a') as arquivo2:
#     arquivo2.write('Geilson Marcelo' '\n')
# Desafio 3 - Com o seu nome já na lista de inscritos, exiba o nome de cada pessoas que está inscrito na lista + o número que ele representa na lista em ordem crescente (ex: 1 jhonatan , 2 Patricio Silva, 3 Kid Boy 3000)
with open('inscritos.txt', 'r') as arquivo2:
    for index, valor in enumerate(arquivo2):
        print(index + 1, valor)

