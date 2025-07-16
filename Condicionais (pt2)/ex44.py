print('=========== LOJAS GUANABARA ===========')

preco_compras = float(input('Preco das compras:R$'))
print('FORMAS DE PAGAMENTO')
print('[1] a vista dinheiro/cheque')
print('[2] a vista no cartao')
print('[3] 2X no cartao')
print('[4] 3X ou mais no cartao')
opcao = int(input('Qual e a opcao? '))

if opcao == 1:
     preco_final = preco_compras - (preco_compras * 0.10)
     print(f'Sua compra de R${preco_compras} vai custar R${preco_final:.2f} no final')
elif opcao == 2:
     preco_final = preco_compras - (preco_compras * 0.05)
     print(f'Sua compra de R${preco_compras} vai custar R${preco_final:.2f} no final')
elif opcao == 3:
    preco_final = preco_compras
    parcelas = int(input('Quantas parcelas? '))
    print(f'Sua compra sera parcelada em {parcelas} parcelas de {preco_final/parcelas} cada uma.')
elif opcao == 4:
    preco_final = preco_compras + (preco_compras * 0.20)
    parcelas = int(input('Quantas parcelas? '))
    print(f'Sua compra sera parcelada em {parcelas} parcelas de {preco_final / parcelas} COM JUROS')
    print(f'Preco final da compra: R${preco_final:.2f}')
else:
    print('Digite uma opcao valida!')




