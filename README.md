# codigobonito.github.io

Página do GitHub da organização do Código Bonito.

Para rodar o site localmente, você irá precisar ter o [Ruby](https://www.ruby-lang.org/en/documentation/installation/) e
também o [Jekyll e o Bundler](https://jekyllrb.com/docs/installation/) instalados.

Uma vez instalados, clone esse repositório:

```bash
git clone https://github.com/codigobonito/codigobonito.github.io
cd codigobonito.github.io/
```

Instale as dependências:

```bash
cd docs/
bundler install
```

E, então, ainda dentro do diretório docs/, sirva o website localmente:

```bash
bundler exec jekyll serve
```

Depois de alguns segundos, seu computador deve estar servindo o website em `localhost:4000`


## Extras
* Google Collab para extrair membros da organização: https://colab.research.google.com/drive/1LV7mh0PcsG1U2LbQbRBoFr-PaHQmdE_O?usp=sharing
