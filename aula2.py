#Como criar e modificar Arquivos:
#Guardar informações de preços de celulares em uma cidade

# 'r' -> Ler algo
# 'w' -> Escrever algo
# 'r+' -> Ler e Escrever algo
# 'a' -> Acrescentar algo

valores_celulares = [850, 2230, 1500, 3500, 5000]

#'W' para escrever os dados em um arquivo de texto. A variavel valor vai verificar em valores e escrever no arquivo txt criado, convertendo em String.

with open('valores_celulares.txt', 'w') as arquivo: 
    for valor in valores_celulares:
        arquivo.write(str(valor) + '\n')


#'A' para adicionar os dados em um arquivo de texto.
with open('valores_celulares.txt', 'a') as arquivo: 
    for valor in valores_celulares:
        arquivo.write(str(valor) + '\n')


#'R' apenas para leitura, e ao invés de escrever com 'Write' iremos apenas imprimir com 'Print'
with open('valores_celulares.txt', 'r') as arquivo: 
    for valor in valores_celulares:
        print(valor)

with open('valores_celulares.txt', 'r') as arquivo: 
    for valor in arquivo:
        print(valor)


#'R+' para leitura e adicionar um novo valor
with open('valores_celulares.txt', 'r+') as arquivo: 
    for valor in arquivo:
        print(valor)
    arquivo.write('9000')    

























