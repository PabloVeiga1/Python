#Calculando empréstimo
valor_casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento?:'))

#taxa por mes
taxa_mes = valor_casa / (anos * 12)
#criando as condicoes
if taxa_mes <= salario * 0.3:
    print(f'Para pagar uma casa de R${valor_casa} em {anos} anos , a prestacao sera de {taxa_mes:.2f}')
    print('Emprestimo CONDECIDO!')
else:
    print(f'Para pagar uma casa de R${valor_casa} em {anos} anos , a prestacao sera de {taxa_mes:.2f}')
    print('Emprestimo NEGADO!')