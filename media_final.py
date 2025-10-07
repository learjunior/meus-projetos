

#CALCULAR MÉDIA FINAL DO ALUNO
disciplina=input("Você deve colocar os valores de sua média a cada bimestre para obter a média final! \nDigite a disciplina: ")
soma=int(input("Digite sua média do 1º bimestre: "))
soma=soma+int(input("Digite sua média do 2º bimestre: "))
soma=soma+int(input("Digite sua média do 3º bimestre: "))
soma=soma+int(input("Digite sua média do 4º bimestre: "))
soma=soma/4 #queremos um número real
print("Sua média final na disciplina de",disciplina,"é: ",soma)
