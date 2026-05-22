#Sistema de cadastro de alunos 
alunos = []

def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

def verificar_situaçao(media):
    if media >= 7:
        return "aprovado"
    elif media >= 5:
        return "recuperação"
    else:
        return "reprovado"
    
def cadastrar_aluno(nome, nota1, nota2, nota3):
    media = calcular_media(nota1, nota2, nota3)
    situaçao = verificar_situaçao(media)

    aluno = {
        "nome": nome,
        "media": media,
        "situaçao": situaçao
    }

    alunos.append(aluno)

def mostrar_alunos():
        for aluno in alunos:
            print(f"Aluno: {aluno['nome']} | Media: {aluno['media']} | Situaçao: {aluno['situaçao']}")

cadastrar_aluno("joão", 8, 7, 9)
cadastrar_aluno("pedro", 5, 6, 4)
cadastrar_aluno("gabriel", 3, 4, 2)

mostrar_alunos()

