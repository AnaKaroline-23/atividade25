# Enunciado: Crie um programa que receba a nota de 5 alunos e exiba quantos foram aprovados (nota maior ou igual a 7).
Aprovados = 0

for nota in range(5):
    nota = float(input("Digite a nota do aluno : "))
    
    if nota >= 7:
        Aprovados += 1

print(f"Total de alunos aprovados é: {Aprovados}")