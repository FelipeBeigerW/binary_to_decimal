arr = []

def to_binary(number):
  number = int(number)
  division = number // 2
  rest = number % 2

  arr.append(str(rest))
  if division != 1:
    to_binary(division)
  else:
    arr.append(str(1))

  arr.reverse()
  print(''.join(arr))

def to_decimal(binary):
  arr = [*str(binary)]
  arr.reverse()
  i = 0
  sum = 0
  exp = 0
  for number in arr:
    if int(number) != 0:
      exp = 2 ** int(i)
      sum += exp  
    i += 1
  print(sum)


DIV_LENGTH = 25

def converter():
  print('='* DIV_LENGTH)
  print('Binary to Decimal Converter')
  print('='* DIV_LENGTH)

  print("Qual operação você deseja realizar? \n 1: Binário -> Decimal \n 2: Decimal -> Binário")
  operation = int(input())

  if operation == 1:
    print("Informe o número que deseja converter para decimal")
    binary_number = input()
    to_decimal(binary_number)
  elif operation == 2:
    print("Informe o número que deseja converter para binário")
    decimal_number = input()
    to_binary(decimal_number)
  else: 
    print('Operação inválida')


converter()
