# 🇨🇭 Swiss German Lab

Um pequeno laboratório em Python para explorar vocabulário associado ao **alemão suíço (Schweizerdeutsch)** e comparar exemplos com o alemão padrão.

> Projeto educacional de programação e exploração linguística. O alemão suíço reúne diferentes variedades regionais, portanto as formas apresentadas aqui são exemplos e não representam uma única forma universal de falar.

## 🎯 Objetivos

- praticar Python com um projeto temático;
- organizar dados de vocabulário em estruturas reutilizáveis;
- implementar consultas e validações simples;
- escrever testes automatizados;
- manter uma estrutura de projeto adequada para portfólio.

## ✨ Funcionalidades

- comparação de termos do alemão padrão com exemplos em alemão suíço;
- indicação de contexto de uso;
- tratamento de termos desconhecidos;
- validação de entradas vazias;
- demonstração executável pelo terminal;
- testes com `unittest`;
- GitHub Actions para execução automática dos testes.

## ▶️ Como executar

```bash
git clone https://github.com/marcellabongiolo/swiss-german-lab.git
cd swiss-german-lab
python tradutor_suico.py
```

Execute os testes:

```bash
python -m unittest discover -s tests -v
```

O projeto não possui dependências externas.

## 📁 Estrutura

```text
swiss-german-lab/
├── .github/
│   └── workflows/
│       └── tests.yml
├── tests/
│   └── test_tradutor_suico.py
├── .gitignore
├── LICENSE
├── README.md
└── tradutor_suico.py
```

## 🧠 Conceitos praticados

- Python;
- dicionários e estruturas de dados;
- classes e métodos;
- type hints;
- validação de entrada;
- tratamento de exceções;
- testes automatizados;
- organização de código;
- GitHub Actions.

## 🔎 Observação linguística

O termo **Schweizerdeutsch** normalmente se refere a um conjunto de variedades de alemão faladas na Suíça, com diferenças regionais de vocabulário, pronúncia e escrita. Por isso, este laboratório deve ser entendido como uma coleção de exemplos para estudo, e não como um tradutor completo de todos os dialetos suíço-alemães.

## 🚀 Próximos passos possíveis

- ampliar o banco de vocabulário;
- separar dados linguísticos da lógica da aplicação;
- adicionar busca sem diferenciar maiúsculas e minúsculas;
- incluir categorias e regiões quando houver fonte adequada;
- criar uma interface simples para consultas.

## 👩‍💻 Autora

**Marcella Bongiolo**

- GitHub: https://github.com/marcellabongiolo
- LinkedIn: https://linkedin.com/in/marcellabongiolo

## 📄 Licença

Este projeto está sob a licença MIT.
