print("Ano e Semestre de Matricula")
Matricula = int(input("Digite a Matricula AASDDDD:"))
Ano = Matricula//100000
Semestre = (Matricula - Ano * 100000)//10000
print("O Ano e Semestre sao:", Ano,Semestre)
