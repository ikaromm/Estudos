# sep= '' separa as coisas, end='' mostra algo ao final da linha com padrão /r/n pular linha
# str -> string -> texto
#tipagem dinamica e forte
#int = inteiro
# float = real.
#Tipo (bool) boolean retorna true or false 
#type mostra o tipo da classe do objeto type('objeto') => class str
# == serve para ver se objetos são iguais por exemplo 1 == 1
#Para trocar o type podemos fazer int('1') vai de str -> inteiro
#variável é para diminuir repetição por exemplo nome = 'ikaro moribayashi'
# % resto da divisão // divisão inteira, isso é, volta o valor inteiro ignora as casa ** exponencial
# se fizer str * int = str str str, exemplo a_3vezes = 'a' * 3
#linha_1 = f'{nome} tem {altura:.2f} de altura,' formatar string com 2 casas decimais e as variaveis são chamadas via {} (f strings)
'''
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)
'''

nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos'
print(formato.format(idade,nome))