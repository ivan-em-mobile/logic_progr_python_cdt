
###@Myriam_Monteiro
##MVC

#model
### def logica_escolha
### while - repete a pergunta
### if - manipula as opções

#view
### def apresentacao
### print(funções()) == console, executar código

#controller
### input opcao
### input - entrada dos dados
### print - exibe informações

def apresentacao():
    print ("Seja bem-vindo(a) ao Banco MMS!")
    print("-"*20)

    print ("Veja as opções a seguir:\n"
                "1 - Conta Corrente \n"
                "2 - Conta Poupança\n"
                "3 - Encerrar sistema")
    print("-"*20)

def logica_escolha():
 
    while True:
        opcao = int ( input ( "Qual opção deseja acessar? " ) )

        if opcao == 1:
            print ("Você acessou a conta Corrente.")
            #inserir o valor de conta corrente

        elif opcao == 2:
            print ("Você acessou a conta Poupança.")
            #inserir o valor de conta poupança, ou qual o valor que você tem.
            
        elif opcao == 3:
            print ("Sistema encerrado. Obrigado por usar o Banco MMS!")
            break
        else:
            print("Opção inválida.")

print(apresentacao())
print(logica_escolha())