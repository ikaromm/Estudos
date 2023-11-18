
cpf = input('digite seu cpf: ')
# cpf.strip()
cpf = cpf.strip()
cpf = cpf.replace('.','')
cpf = cpf.replace('-','')

print(f'{cpf}')


if cpf.isnumeric():
    if len(cpf) == 11:
        print('cpf valido')
    else:
        print('cpf invalido')
else:
    print('cpf invalido')        

