from sqlalchemy import select

from models import Autor, Livro

def listar_livros(session):
    # TODO: liste todos os livros com o nome do autor.
    stmt = select(Livro)
    livros = session.scalars(stmt).all()
    for livro in livros:
        print(f"Livro: {livro.titulo} | Autor: {livro.autor.nome}")

def livros_por_autor(session, nome_autor):
    # TODO: liste os livros de um autor informado pelo nome.
    stmt = select(Autor).where(Autor.nome.ilike(f"%{nome_autor}%"))
    autor = session.scalars(stmt).first()
    if autor:
        for livro in autor.livros:
            print(f"- {livro.titulo} ({livro.ano})")
    else:
        print(f"Autor '{nome_autor}' não encontrado.")

def buscar_livros(session, trecho):
    # TODO: busque livros por parte do título.
    stmt = select(Livro).where(Livro.titulo.ilike(f"%{trecho}%"))
    livros = session.scalars(stmt).all()
    for livro in livros:
        print(f"- {livro.titulo} (Autor: {livro.autor.nome})")

def listar_autores_com_quantidade(session):
    # TODO: liste autores e a quantidade de livros de cada um.
    stmt = select(Autor)
    autores = session.scalars(stmt).all()
    for autor in autores:
        print(f"Autor: {autor.nome} | Total de Livros: {len(autor.livros)}")

def detalhes_livro(session, titulo):
    # TODO: mostre título, ano, autor e país do autor.
    stmt = select(Livro).where(Livro.titulo.ilike(f"%{titulo}%"))
    livro = session.scalars(stmt).first()
    if livro:
        print(f"Detalhes:")
        print(f"Título: {livro.titulo}")
        print(f"Ano: {livro.ano}")
        print(f"Autor: {livro.autor.nome}")
        print(f"País do Autor: {livro.autor.pais}")
    else:
        print(f"Livro '{titulo}' não encontrado.")