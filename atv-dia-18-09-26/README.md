1. Onde estão os modelos ORM no seu projeto?

Eles estão no arquivo models.py

2. Qual classe representa o lado "um" e qual representa o lado "muitos" no relacionamento?

A classe de lado 1 é o Autor já que ele pode ter vários livros, e o lado muitos é o Livros já que um livro só pode ter 1 autor

3. Para que serve o ForeignKey em Livro.autor_id ?

Ela serve para ligar as tabelas, fazendo uma ligação entre autores e livros, por meio do autor_id

4. O que acontece se você esquecer o session.commit() após inserir os dados?

O que está no código não vai ser colocado no banco de dados, ou seja elas não vão ser salvas em biblioteca.bd, os dados ficarão somente salvos temporariamente até fechar o código
