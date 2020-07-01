area = float(input('\nDigite a area do local a ser pintado : '))
tinta = area / 6
latasP = int((tinta / 3.6)+1)
latasG = int((tinta / 18)+1)
# misto é 10.8 litros por 52.5 que é a media das duas latas
misto = int((tinta / 10.8)+1)
print('\nSerão necessários {:.1f} litros de tinta'.format(tinta))
print('O total comprando apenas latas de 3.6 litros será de R${:.2f}'.format(latasP*25))
print('O total comprando apenas latas de 18 litros será de R${:.2f}'.format(latasG*80))

print('\nFim do código\n')
