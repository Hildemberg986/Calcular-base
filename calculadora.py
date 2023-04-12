numero_cal = float(input("Qual numero deseja calcular ? "))
base = float(input("Qual a base esta esse numero ? "))
base_cal = float(input("Qual base deseja calcular ? "))
if int(base) != base:
    print('A base precisar ser um inteiro!')
elif int(base_cal) != base_cal:
    print('A base que queira calcular tem que ser um inteiro!')
else:

    if base == 10:
        if (numero_cal%2) == 0:
            resultado = [0]
        else:
            resultado = [1]
        while (numero_cal > base_cal):
            numero_cal = numero_cal//base_cal
            resto = numero_cal%base_cal
            resultado.insert(0,int(resto))
        else:
            print(resultado)
    else:
        print("Não calculado")