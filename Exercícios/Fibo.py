n_1 = float(0)
n_2 = float(1)


def fibo(x):
    global n_1, n_2
    for i in range(x):
        n = n_1 + n_2
        print(f"Termo: {i}", f" Valor: {n}")
        n_2 = n_1
        n_1 = n


valor = int(input("Digite quantos valores devem ser impressos: "))
fibo(valor)
