## volta a cada 76 anos
## passou em 1986 (resto por 76) 10

ano = 1986
data = int(input("digite o ano: "))

if data - ano > 0:
    a = data - ano
    b = 76 - (a % 76)

    print(f"Vai passar em {data + b}")

elif ano - data > 0:
    a = ano - data
    b = 76 - (a % 76)

    print(f"Vai passar em {data + b}")
