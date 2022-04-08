import numpy as np

alunos = np.array([["A. Gomes", 50], ["B. Silva", 70], ["C. Costa", 30],
                   ["D. Simas", 80], ["E. Cabrita", 40], ["F. Fonte", 45], ["G. Souto", 100]])

notas = np.zeros(alunos.shape[0])

for i, aluno in enumerate(alunos):
    notas[i] = int(aluno[1]) / 5

print("Aprovados: ")
for i, nota in enumerate(notas):
    if nota >= 9.5:
        print(f"Aluno: {alunos[i][0]}; Nota: {nota}")
