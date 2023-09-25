while True:

    cpf = input('Digite o CPF: ') \
    .replace('.','') \
    .replace('-','')\
    .replace(' ', '')

    tam_cpf = int(cpf)

    if len(cpf) != 11 or not cpf.isdigit():
        print('Digite um CPF válido')
        restart = input('Deseja tentar novamente? (S/N): ').strip().lower()
        if restart != 's':
            break
        continue
        
    lista_cpf = []
    lista_cpf_multiplicada = []
    lista_cpf_multiplicada2 = []
    n=11
    k=10
    j=0
    soma_dig_cpf=0
    soma_dig_cpf2 = 0
    for numero in cpf:
        lista_cpf.append(int(numero))

    while k > 1:
        numero1 = lista_cpf[j]      
        lista_cpf_multiplicada.append(numero1*k)
        k = k - 1
        j += 1      

    for soma_multiplicada_cpf in lista_cpf_multiplicada:
        soma_dig_cpf += soma_multiplicada_cpf 

    soma_dig_cpf_x10 = soma_dig_cpf * 10
    resto_soma_dig_cpf_x10 = soma_dig_cpf_x10 % 11

    if resto_soma_dig_cpf_x10 > 9: 
        resto_soma_dig_cpf_x10 = 0
    else: 
    #    print(f'O primeiro digito do cpf é {resto_soma_dig_cpf_x10}') 

        j=0

    while n > 1:
        numero1 = lista_cpf[j]      
        lista_cpf_multiplicada2.append(numero1*n)
        n = n - 1
        j += 1 

    for soma_multiplicada_cpf2 in lista_cpf_multiplicada2:
        soma_dig_cpf2 += soma_multiplicada_cpf2 

    soma_dig_cpf_x102 = soma_dig_cpf2 * 10
    resto_soma_dig_cpf_x102 = soma_dig_cpf_x102 % 11

    if resto_soma_dig_cpf_x102 > 9: 
        resto_soma_dig_cpf_x102 = 0
    else: 
    #    print(f'O segundo digito do cpf é {resto_soma_dig_cpf_x102}') 

        if lista_cpf[9] == resto_soma_dig_cpf_x10 and lista_cpf[10] == resto_soma_dig_cpf_x102:
            print(f'O seu cpf {cpf} é valido ') 
        else:
            print('Seu cpf é invalido')    

    tecla_final =input('Qualquer Tecla para Reiniciar ou [s]air: ')    
    if tecla_final == 's':
        break
    else:
        continue    