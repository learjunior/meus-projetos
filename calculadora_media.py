
a = float(input('Digite a média do 1º bimestre: '))
b = float(input('Digite a média do 2º bimestre: '))    
c = float(input('Digite a média do 3º bimestre: '))
d = float(input('Digite a média do 4º bimestre: '))

def media(a, b, c, d):
    resultado = (a + b + c + d) / 4
    return resultado

media_final = media (a, b, c, d)

print(f"A média final é {media_final:.1f}")