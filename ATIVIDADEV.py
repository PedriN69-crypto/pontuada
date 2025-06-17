class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.emprestado = False

    def __str__(self):
        status = "Emprestado" if self.emprestado else "Disponível"
        return f"{self.titulo} - {self.autor} [{status}]"


class Biblioteca:
    def __init__(self):
        self.livros = []

    def cadastrar_livro(self, titulo, autor):
        livro = Livro(titulo, autor)
        self.livros.append(livro)
        print(f'📚 Livro "{titulo}" cadastrado com sucesso.')

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
            return
        print("📚 Lista de Livros:")
        for i, livro in enumerate(self.livros, start=1):
            print(f"{i}. {livro}")

    def buscar_por_titulo(self, termo):
        encontrados = [
            livro for livro in self.livros
            if termo.lower() in livro.titulo.lower()
        ]
        if not encontrados:
            print(f'Nenhum livro encontrado com o título "{termo}".')
        else:
            print("🔍 Resultados da busca:")
            for livro in encontrados:
                print(f"- {livro}")

    def alternar_emprestimo(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                livro.emprestado = not livro.emprestado
                acao = "emprestado" if livro.emprestado else "devolvido"
                print(f'📦 Livro "{livro.titulo}" foi {acao} com sucesso.')
                return
        print(f'Livro "{titulo}" não encontrado.')

def menu():
    print("""
====== Menu Biblioteca ======
1. Cadastrar Livro
2. Listar Livros
3. Buscar Livro por Título
4. Emprestar/Devolver Livro
0. Sair
""")

biblioteca = Biblioteca()

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Título: ")
        autor = input("Autor: ")
        biblioteca.cadastrar_livro(titulo, autor)

    elif opcao == "2":
        biblioteca.listar_livros()

    elif opcao == "3":
        termo = input("Digite o título ou parte do título: ")
        biblioteca.buscar_por_titulo(termo)

    elif opcao == "4":
        titulo = input("Digite o título do livro para emprestar/devolver: ")
        biblioteca.alternar_emprestimo(titulo)

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")