# Crie um programa que receba uma lista com os nomes dos alunos presentes em uma aula e exiba quantos alunos estão presentes e a lista dos nomes. Se o total de alunos presentes for menor que 5, exiba uma mensagem sugerindo uma revisão da lista de chamada.

# Exemplo de entrada:
# Alunos presentes: ['Ana', 'Bruno', 'Carlos', 'Daniela']

# Exemplo de saída:
# Alunos presentes: 4
# Lista de alunos presentes: Ana, Bruno, Carlos, Daniela
# Aviso: Poucos alunos presentes. Revisar lista de chamada.

chamada = []
contador = 0

while True:
    alunosPresentes = input("Digite o nome dos alunos presentes (0 para parar): ")
    if alunosPresentes == '0':
        break
    chamada.append(alunosPresentes) 
    contador += 1

print("-=-" * 20)
print(f"Alunos presentes : {contador}")
print(f"Lista de alunos presentes: {chamada}")
print("-=-" * 20)

if contador < 5:
    print ("*Aviso: Poucos alunos presentes. Revisar lista de chamada.*")
else:
    print ("Tudo certo!")




