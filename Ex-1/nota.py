def calcular_media(notas):
    return sum(notas) / len(notas)

def situacao_aluno(media):
    if 3 <= media <= 5.9:
        return "Exame"
    elif media >= 6:
        return "Aprovado"
    else:
        return "Reprovado"

def main():
    nome_aluno = input("Digite o nome do aluno: ")
    notas = []

    for i in range(2):
        while True:
            nota = float(input(f"Digite a nota {i + 1} do aluno {nome_aluno}: "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("Nota inválida! Digite um valor entre 0 e 10.")
                
    media = calcular_media(notas)
    situacao = situacao_aluno(media)

    print(f"Aluno: {nome_aluno}\nMédia: {media:.2f}\nSituação: {situacao}")

if __name__ == "__main__":
    main()
