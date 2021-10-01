#crie um formulário, onde o usuário irá informar dois valores e uma operação
#de soma, subtração, multiplicação ou divisão

#Haverá as seguintes funções:
#1) Ação - Responsável por obter os dados informados, selecionar um cálculo e exibir
#2) Soma - Haverá dois parâmetros que retornará a soma dos valores
#3) Subtração - Haverá dois parâmetros que retornará a subtração dos valores
#4) Multiplicação - Haverá dois parâmetros que retornará a multiplicação dos valores
#5) Divisão - Haverá dois parâmetros que retornará a divisão dos valores



def calculadora():
    valor_1 = int(input('Informe o Primeiro valor: '))
    valor_2 = int(input('Informe o Segundo valor: '))
    conta_operacao = int(input("Informe a Operação quer deseja: "
                               "1 para +"
                               "2 para -"
                               "3 para *"
                               "4 para /:"))
    if conta_operacao == 1:
        soma = valor_1 + valor_2
        return(soma)
    elif conta_operacao == 2:
        subtracao = valor_1 - valor_2
        return subtracao

resultado = calculadora()
print(resultado)




