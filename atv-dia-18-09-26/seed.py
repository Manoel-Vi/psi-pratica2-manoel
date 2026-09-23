from models import Autor, Livro

def popular_banco(session):
    # TODO: crie pelo menos 3 autores e 6 livros.
    # TODO: relacione os livros aos autores.
    # TODO: use session.add ou session.add_all e session.commit.

    autor1 = Autor(nome="Hugo Wendell", pais="Brasil")
    autor2 = Autor(nome="Max Miller", pais="Brasil")
    autor3 = Autor(nome="Romeras Campos", pais="Brasil")

    livro1 = Livro(titulo="Bd básicos", ano=2026, autor=autor1)
    livro2 = Livro(titulo="Dart = Python 2.0", ano=2026, autor=autor1)
    livro3 = Livro(titulo="Unity é boa msm?", ano=2025, autor=autor2)
    livro4 = Livro(titulo="Jogos com pygame", ano=2026, autor=autor2)
    livro5 = Livro(titulo="Js e o diabo", ano=2026, autor=autor3)
    livro6 = Livro(titulo="O que é 67?", ano=2026, autor=autor3)

    session.add_all([
        autor1, autor2, autor3,
        livro1, livro2, livro3, livro4, livro5, livro6
    ])

    session.commit()