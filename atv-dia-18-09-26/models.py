from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

class Autor(Base):
# TODO: crie o modelo Autor.
# Campos: id, nome, pais.
# Relacionamento: livros.
    __tablename__ = "autores"

    id: Mapped[int] = mapped_column(primary_key = True)
    nome: Mapped[str]
    pais: Mapped[str]

    livros: Mapped[List["Livro"]] = relationship("Livro", back_populates="autor")

class Livro(Base):
# TODO: crie o modelo Livro.
# Campos: id, titulo, ano, autor_id.
# Relacionamento: autor.
    __tablename__ = "livros"

    id: Mapped[int] = mapped_column(primary_key = True)
    titulo: Mapped[str]
    ano: Mapped[int]
    autor_id: Mapped[int] = mapped_column(ForeignKey("autores.id"))

    autor: Mapped["Autor"] = relationship("Autor", back_populates="livros")