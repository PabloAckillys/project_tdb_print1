print("Opções de caixa de entrada:\n\n1 - Todas as entradas\n2 - E-mail\n3 - Sms\n4 - WhatsApp\n0 - sair\n")
opcao = int(input("Digite a opção desejada:"))

match opcao:
    case 1:
        def allmaill():
            print("Todas as entradas")
    case 2:
        def emaill():
            print("Todos os emails")
    case 3:
        def sms():
            print("Todos os sms")
    case 4:
        def whatsapp():
            print("Todos os whatsapp")
    case 0:
        print("sair")
    case _:
        print("Opção invalida")