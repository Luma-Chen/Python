#Faça um algoritmo que valide uma data. A mesma deve ser formada por dia, mês e ano. Por exemplo, se o usuário digitar a data 10/8 
#a mesma será inválida. Porém, caso a data seja 01/10/2018, a mesma deve ser considerada válida.

dia= int (input ("Digite um dia: "))
mes= int (input ("Digite um mês: "))
ano= int (input ("Digite um ano: "))
if ano > 0 and ano < 2100:
    if dia > 0 and dia < 32 and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        print (dia, "/", mes, "/", ano, "A data está válida")
    elif dia > 0 and dia < 30 and mes == 2:
        print (dia, "/", mes, "/", ano, "A data está válida")
    elif dia > 0 and dia < 31 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
            print (dia, "/", mes, "/", ano, "A data está válida")
    else:
        print("A data é inválida")
else:
    print ("A data é inválida")
print ()


#Faça um algoritmo que imprima os números no intervalo entre 1 e 100:

for i in range (1, 101, 1):
    print (i)
    

#Faça um algoritmo que imprima os valores no intervalo definido pelo usuário e permita que o mesmo possa definir 3 números que 
#deverão ser ignorados, ou seja, que não serão impressos na tela:

interv1= int (input ("Digite o primeiro número do intervalo: "))
interv2= int (input ("Digite o último número do intervalo: "))
num1, num2, num3= input ("Digite 3 números a serem excluídos: ").split (" ")
num1= int (num1)
num2= int (num2)
num3= int (num3)
for x in range (interv1, interv2 + 1, 1):
    if x == num1 or x == num2 or x == num3:
        continue
    print (x)
    

#Faça um algoritmo que imprima a frase "estou em looping" e, em seguida, solicite ao usuário digitar uma letra. Caso a letra seja 
#o "q" finalize a aplicação. Do contrário, imprima novamente a mesma frase até que o caractere "q" seja enviado:

letra= "l"
while (letra != "q"):
    print ("Estou em looping")
    letra= input ("Digite uma letra: ")
