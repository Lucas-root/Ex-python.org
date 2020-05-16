# Programa para verificar se um cpf é valido
# o cpf deve estar no formato xxx.xxx.xxx-xx
# me desculpem pela bagunça do código

cpf = str(input('Digite o seu cpf : '))

cpf_formatado = cpf.strip()
cpf_formatado = cpf_formatado.replace('.', '')
cpf_formatado = cpf_formatado.replace('-', '')
# formata o cpf com o formato xxx.xxx.xxx-xx para xxxxxxxxxxx

cpf_f = cpf_formatado # para facilitar joguei o conteudo da variavel cpf_formatado para cpf_f

primeiro_digito = int(cpf_f[0])*10 + int(cpf_f[1])*9 + int(cpf_f[2])*8 + int(cpf_f[3])*7 + int(cpf_f[4])*6
primeiro_digito += int(cpf_f[5])*5 + int(cpf_f[6])*4 + int(cpf_f[7])*3 + int(cpf_f[8])*2

corpo = cpf_f[0:9]
primeiro_digito = (primeiro_digito * 10) % 11

cpf_f = corpo + str(primeiro_digito) # adiciona o primeiro digito verificador ao corpo (os nove primeiros numeros)

segundo_digito = int(cpf_f[0])*11 + int(cpf_f[1])*10 + int(cpf_f[2])*9 + int(cpf_f[3])*8 + int(cpf_f[4])*7
segundo_digito += int(cpf_f[5])*6 + int(cpf_f[6])*5 + int(cpf_f[7])*4 + int(cpf_f[8])*3 + int(cpf_f[9])*2
# Eu dividi a conta para não ficar em apenas uma linha

segundo_digito = (segundo_digito * 10) % 11

cpf_f = cpf_f + str(segundo_digito)

if cpf_f == cpf_formatado: # compara o cpf digitado com o cpf com os digitos que eu formatei
    print('\nEste cpf é valido.')
elif cpf_f != cpf_formatado:
    print('\nEste cpf não é valido!.')
else: # caso algum erro ocorra eu criei este else para avisar
    print('Algum erro ocorreu.')

print('\nFim do código\n')
# esta linha sinaliza que o programa terminou de ler todo o meu código 



        

