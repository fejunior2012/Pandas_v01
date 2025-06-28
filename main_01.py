valores_list = [-1, 2, 7, -9, 23, -15, 8, 27]
valores_tuple = tuple(valores_list)
# print(valores_tuple)

soma = 0
for n in valores_tuple:
    soma += n

print(f'A soma é {soma}')
print(f'A média é {soma/len(valores_tuple)}')

n = 0
while n < 10:
    print(n)
    n += 1
    if n == 5:
        break
print("Fim do loop")

nome = "Juliano"
for caractere in nome:
    print(caractere)

valores = [10, 20, 30]
for valor in valores:
    print(f'O valor é: {valor}')

valores_list = [-1, 2, 7, -9, 23, -15, 8, 27]
valores = valores_list[:3] # [-1, 2, 7]
valores = valores_list[2:3] # [7]
valores = valores_list[1] # [2]
valores = valores_list[-1] # [27]
valores = valores_list[1:] # [2, 7, -9, 23, -15, 8, 27]
valores = valores_list[1:len(valores_list)] # [2, 7, -9, 23, -15, 8, 27]
print(valores)

valores_list = list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
valores_list = list(range(1, 10)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
valores_list = list(range(1, 10, 2)) # [1, 3, 5, 7, 9]
valores_list = list(range(10, 1, -2)) # [10, 8, 6, 4, 2]
del valores_list[0] # [8, 6, 4, 2]
print(valores_list)
print(dir(valores_list))
print(help(valores_list.pop))


produtos = {'banana': 1, 'maça': 2.50}

print(produtos.get('banana'))