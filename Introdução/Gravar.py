arquivo = open('arqText.txt', 'a+')

arquivo.write("Curso Python \n")
arquivo.write(input("Escreva algo: "))
arquivo.close()

leitura = open('arqText.txt', 'r')
print(leitura.read())
leitura.close()