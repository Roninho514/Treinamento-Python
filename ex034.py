salario = float(input('Qual o salário do funcionário? R$'))
if salario > 1250.00:
    print('Quem ganhava R${:.2f} vai ganhar agora R${:.2f}'.format(salario , salario + (salario*10)/100))
else:
    print('Quem ganhava R${:.2f} vai ganhar agora R${:.2f}'.format(salario , salario + (salario*15)/100))
   