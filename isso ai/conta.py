conta = input('''
Selecione a conta matématica que voçe quer:
+ pra adição
- pra subtração
* pra multiplicação
/ pra divisão
''')
a = int(input("Insira um numero: "))
b = int(input("Insira outro numero: "))

#multiplicação
if conta == '*':
 print('{} * {} = '.format(a,b))
 print(a * b)

#divisão
elif conta == '/': 
 print('{} / {} ='.format(a,b))
 print(a / b)
#adição
elif conta == '+':
 print('{} + {} ='.format(a,b))
 print(a + b)

#subtração
elif conta =='-':
 print('{} - {} ='.format(a,b))
 print(a - b)





