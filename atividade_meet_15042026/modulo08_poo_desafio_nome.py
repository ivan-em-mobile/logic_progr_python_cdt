class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        status = "Disponivel" if self.disponivel else "Emprestado"
        # CORREÇÃO: Removidos os parênteses retos colados ao autor
        return f"'{self.titulo}' - {self.autor} ({status})"
    
class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def emprestar_livro(self, titulo_procurado):
        for livro in self.livros:
            if livro.titulo == titulo_procurado:
                if livro.disponivel:
                    livro.disponivel = False
                    print(f"Empréstimo de '{livro.titulo}' realizado!")
                else:
                    print(f"O Livro '{livro.titulo}' já está emprestado.")
                return # Sai da função se encontrar o livro
        
        # CORREÇÃO: Este print deve ficar FORA do ciclo for
        # Só chega aqui se o ciclo terminar sem encontrar o título
        print("Livro não está no acervo.")

# --- Teste ---
biblioteca_municipal = Biblioteca()
l1 = Livro("Dom Quixote", "Miguel de Cervantes")

l2 = Livro("O pequeno príncipe", "Antoine de Saint-Exupéry")

l3 = Livro("Verity", "Collen Hoover")

l4 = Livro("O alienista", "Machado de Assis")

biblioteca_municipal.adicionar_livro(l1)

biblioteca_municipal.adicionar_livro(l2)

biblioteca_municipal.adicionar_livro(l3)

biblioteca_municipal.adicionar_livro(l4)

print(l3) # Estado inicial
biblioteca_municipal.emprestar_livro("Verity")
print(l3) # Estado após empréstimo