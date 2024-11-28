livros = {
    "teoria da relatividade": "disponivel",
    "a republica": "disponivel",
    "apologia de socrates": "disponivel",
    "assim falou zaratustra": "disponivel",
    "o banquete": "disponivel",
}


def pegar_livro(nome):
    if livros.get(nome) is None:
        print("livro inexistente!")
        return
    livros[nome] = "indisponivel"
    print("Livro retirado com sucesso!")


def devolver_livro(nome):
    if livros.get(nome) is None:
        print("livro inexistente!")
        return
    livros[nome] = "disponivel"
    print("Livro devolvido com sucesso!")


def adicionar_livro(nome):
    livros[nome] = "disponivel"

def remover_livro(nome):
    if livros.get(nome) is None:
        print("Livro inexistente!")
        return
    del livros[nome]
    print("Livro removido com sucesso!")

def listar_livros():
    for livro, disponibilidade in livros.items():
        print(f"{livro} --> {disponibilidade}")


print("-" * 40)


print(
    """Selecione uma opção:
1. Listar livros.
2. Pegar livro.
3. Devolver livro.
4. Adicionar livro.
5. Deletar livro."""
)

while True:
    print("-" * 40)

    print("Insira uma opção")
    ans = input("> ")

    match ans:
        case "1":
            listar_livros()
        case "2":
            livro = input("Insira o nome do livro: ")
            pegar_livro(livro)
        case "3":
            livro = input("Insira o nome do livro: ")
            devolver_livro(livro)
        case "4":
            livro = input("Insira o nome do livro: ")
            adicionar_livro(livro)
            print("Livro inserido com sucesso!")
        case "5":
            livro = input("Insira o nome do livro: ")
            remover_livro(livro)
        case _:
            print("Insira um número valido!")
