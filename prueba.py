import math
edad = int(input("Digite edad del niño: "))
peso = float(input("Digite peso del niño: "))
pDest = [2, 1, 2] #porciones diarias de carbohidratos, proteinas y verduras para desnutridos
pSob = [0.6, 1, 4] #porciones diarias de carbohidratos, proteinas y verduras para obesos
pSal = [0.5, 0.7, 2] #porciones diarias de carbohidratos, proteinas y verduras para personas saludables
aP = 30.5 #aporte diario en peso de proteinas
aC = 60.1 #aporte diario en peso de carbohidratos
aV = -24.4 #aporte diario en peso de frutas y verduras
i = 0
estado = ""
peso = peso * 1000

if edad >= 5 and edad <= 10:
    if peso < 16000:
        aux = peso
        estado = 'a'
        objetivo = 22000
        while peso <= objetivo:
            i+=1
            peso = aux + (pDest[0]*aC + pDest[1]*aP + pDest[2]*aV) * i
    elif peso >= 16000 and peso <= 28000:
        aux = peso
        estado = 'c'
        objetivo = 28000
        while peso <= objetivo:
            i+=1
            peso = aux + (pSal[0]*aC + pSal[1]*aP + pSal[2]*aV) * i
    else :
        aux = peso
        estado = 'b'
        objetivo = 24000
        while peso >= objetivo:
            i+=1
            peso = aux + (pSob[0]*aC + pSob[1]*aP + pSob[2]*aV) * i
elif edad >= 10 and edad <= 13:
    if peso < 30000:
        aux = peso
        estado = 'a'
        objetivo = 32000
        while peso <= objetivo:
            i+=1
            peso = aux + (pDest[0]*aC + pDest[1]*aP + pDest[2]*aV) * i
    elif peso >= 30000 and peso <= 50000:
        aux = peso
        estado = 'c'
        objetivo = 50000
        while peso <= objetivo:
            i+=1
            peso = aux + (pSal[0]*aC + pSal[1]*aP + pSal[2]*aV) * i
    else :
        aux = peso
        estado = 'b'
        objetivo = 43000
        while peso >= objetivo:
            i+=1
            peso = aux + (pSob[0]*aC + pSob[1]*aP + pSob[2]*aV) * i
elif edad > 13 and edad <= 17:
    if peso < 51000:
        aux = peso
        estado = 'a'
        objetivo = 56000
        while peso <= objetivo:
            i+=1
            peso = aux + (pDest[0]*aC + pDest[1]*aP + pDest[2]*aV) * i
    elif peso >= 51000 and peso <= 63000:
        aux = peso
        estado = 'c'
        objetivo = 63000
        while peso <= objetivo:
            i+=1
            peso = aux + (pSal[0]*aC + pSal[1]*aP + pSal[2]*aV) * i
    else :
        aux = peso
        estado = 'b'
        objetivo = 58000
        while peso >= objetivo:
            i+=1
            peso = aux + (pSob[0]*aC + pSob[1]*aP + pSob[2]*aV) * i
if estado == "a" or estado == "b":
    print(f"El estado nutricional del niño es {estado} y se requieren {i} dias para que alcance un peso saludable ",math.trunc(peso/1000))
else:
    print("El estado nutricional del niño es ",estado," y se requieren ",i," dias para que alcance un peso maximo ",math.trunc(peso/1000))
