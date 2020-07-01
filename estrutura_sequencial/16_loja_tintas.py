# Programa para uma loja de tintas

area = float(input('\nDigite a area do local a ser pintado : '))
tinta = area / 3
#fiz a conversão para  latas inteiras porque não se pode comprar va-
#lores quebrados de latas de tinta
latas = int((tinta / 18)+1)
total = latas * 18

print('\nVocê precisará de {:.1f} litros de tinta'.format(tinta))
print('Você presisará comprar {} latas de tinta'.format(latas))
print('E o total será R${:.2f}'.format(total))

print('\nFim do Código\n')

