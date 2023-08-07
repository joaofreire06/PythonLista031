'''
 Fazer um programa que calcule e apresente a quantidade de litros que um automóvel gastará em uma viagem. O
programa deve coletar as seguintes informações: Distância a percorrer na viagem, em quilômetros; qual é o
valor do consumo médio do automóvel, em quilômetros por litro
'''

dist = float(input("Qual a distancia  a percorrer em km ?"))

cons = float(input("Qual o consumo médio do automóvel,em quilômetros por litro?"))

result = (dist / cons)

print("O consumo médio é",result)
