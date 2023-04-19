while True:
  print("Selecione a opção que deseja realizar: ")
  opcao = input("1- Fazer calculo ou 2- Sair: ")
  
  if opcao == "2":
    print("Voce finalizou sessao.")
    break
  if opcao == "1":
    num1 = input("Digite primeiro numero: ")
    num2 = input("Digite segundo numero: ")
    print("1- Soma\n2- Subtração\n3- Multiplicação\n4- Divisão")
    operacao = input("Qual deseja realizar: ")

    if not num1.isnumeric() or not num2.isnumeric():
      print("Digite um numero valido.")
      continue
    num1 = float(num1)
    num2 = float(num2)

    if operacao == "1":
      print(f"O resultado da soma entre {num1} e {num2} é: {num1 + num2}")
    elif operacao == "2":
      print(f"O resultado da subtração entre {num1} e {num2} é: {num1 - num2}")
    elif operacao == "3":
      print(f"O resultado da multiplicação entre {num1} e {num2} é: {num1 * num2}")
    elif operacao == "4":
      print(f"O resultado da divisão entre {num1} e {num2} é: {num1 / num2}")
    else:
      print("Escolha uma opção valida.")
      continue
