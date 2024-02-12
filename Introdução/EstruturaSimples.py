A = int(input("Informe um valor para a variavel A: "))
B = int(input("Informe um valor para a variavel B: "))

if (A>B):
    aux = A;
    A = B;
    B = aux;

tipoa = type(A)
tipob = type(B)

print("O valor da Variável A agora é: ", A)
print("O valor da Variável B agora é: ", B)
print(tipoa, tipob)