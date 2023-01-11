texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() #adiciona uma qubera de linha
    print("Executa no final do laço")
    
    
# exemplo utilizando a função built-in range
for numero in range (0, 41, 2):
    print (numero, end=" ")