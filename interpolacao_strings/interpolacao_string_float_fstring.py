valor1 = 8.75217
valor2 = 73032
valor3 = 11.349

#formatação apenas como valor float
print(f"Valor 1:{valor1:f}")

#formação float com decimal em digitos
print(f"Valor{valor1:f}")
print(f"Valor{valor2:f}")
print(f"Valor{valor3:f}")


#formatação float, com separador de milhares e decimal em 2 dìgitos
print("Valor 2:{:.2f}".format(valor2))

#------------------------
# formação float, com total de 10 dìgitos (numeros e ponto), sendo 2 decimais.
print(f"Valor{valor1:.2f}")
print(f"Valor{valor2:.2f}")
print(f"Valor{valor3:.2f}")

# semelhante ao anterior, mas preenche casas antes do ponto com zero quando necessário.
print(f"Valor{valor1:10.2f}")
print(f"Valor{valor2:10.2f}")
print(f"Valor{valor3:10.2f}")


valor4 = 8.7536

#formatação float exibindo em percentual com decimal em 1 dígitoprint
print(f"Valor{valor1:.1%}")

#incluindo R$ antes do valor e substituindo a vírgula do milhar por underline
texto_valor2 = f"R$ {valor2:_.2f}"
print(f"Texto Valor 2: {texto_valor2})

# Incluindo R$ antes do valor e substituindo a virgula e oque é underline por ponto
texto_valor_br = texto_valor2.replace("."","",").replace("_"","",")
print(f"Texto Valor BR: {texto_valor_br}")






