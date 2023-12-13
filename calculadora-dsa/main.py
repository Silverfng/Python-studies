print('********************  Calculadora DSA  ********************')
print('\nSelecione o número da operação desejada:\n')

print('1 - Soma\n' +
      '2 - Subtração\n' +
      '3 - Multiplicação\n' +
      '4 - Divisão\n')

user_choice = int(input('Digite sua opção (1/2/3/4): '))

num1 = int(input('\nDigite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

def calculadora(num1, num2):
    if user_choice == 1:
        return num1 + num2
    if user_choice == 2:
        return num1 - num2
    if user_choice == 3:
        return num1 * num2
    if user_choice == 4:
        return num1 / num2
    else:
        print('Opção inválida!')

print('Resultado = %d' % calculadora(num1, num2))