'''

i=0
while i<=100:
    print(i)
    i+=5
    


resposta = input("Deseja encontrar numeros pares (s/n)")


while resposta!= "n":
    num1 = int(input("Digite um numero ou fim para fianlizar as analises: "))


    if num1%2==0:
        print(f"{num1} é par")
    else:
        print(f"{num1} é impar")

    resposta = input("Se n quiser mais saber se um numero é par digite fim")
    if resposta=="fim":
        print("brocha")

    

'''


resposta = input("voce quer encontrar numeros pares ? (s/n) ")
j=0
while resposta != "s" and resposta != "n":
    print("Fala português alienigena FDP!!!")
    resposta = input("voce quer encontrar numeros pares ? (s/n) ")
    j+=1
    if j!=0:
        print("parabéns!!!!! voce sabe português!!!")
    elif resposta == "n":
        print("chato bacarai")
    else:
        print("voce é brabo")

    if resposta == "s":
        qtd = int(input("qts numeros vc quer ? "))
    i=0

while i<qtd:
    num = int(input("Diga um numero : "))
    if num%2==0:
        print(f"{num} é par")
    else:
        print(f"{num} é impar")
    i+=1
    if i==qtd:
        print("flw brabo")