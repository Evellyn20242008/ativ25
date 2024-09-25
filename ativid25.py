 #Enunciado: Crie um programa que receba a nota de 5 alunos e exiba quantos foram aprovados (nota maior ou igual a 7).

aprovados = 0

# Loop para receber as notas dos alunos
for i in range(5):
    # Solicita a nota do aluno
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    
    # Verifica se a nota é maior ou igual a 7
    if nota >= 7:
        aprovados += 1

# Exibe o resultado
print(f"Total de alunos aprovados: {aprovados}")