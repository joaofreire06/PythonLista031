'''
fazer um algoritmo que efetue o cálculo do valor de uma prestação em atraso, utilizando a fórmula prestação	=
valor	+	(valor	x	(taxa	:	100)	x	tempo	em	dias)
'''

valor = float(input("Qual o valor normal da prestação?"))
taxa = float(input("Qual a taxa de juros?"))
tempo = float(input("Quantos dias de atraso?"))

#valor	+	(valor	x	(taxa	:	100)	x	tempo	em	dias)
prestacao = valor + (valor * (taxa / 100) * tempo)

print("O valor do prestação em atraso é R$",prestacao)
