# Calculadora POO

## Sobre o projeto

Este projeto consiste no desenvolvimento de uma calculadora desktop utilizando a linguagem Python, a biblioteca Tkinter e os conceitos de Programação Orientada a Objetos (POO).

O objetivo é criar uma aplicação que realize operações matemáticas básicas por meio de uma interface gráfica, aplicando conceitos de organização, reutilização e estruturação de código.

## Funcionalidades

- Realizar operações de adição.
- Realizar operações de subtração.
- Realizar operações de multiplicação.
- Realizar operações de divisão.
- Exibir o resultado das operações.
- Armazenar o histórico de cálculos.
- Limpar os campos de entrada.
- Limpar o histórico de operações.
- Validar os valores informados pelo usuário.
- Impedir divisão por zero.

## Tecnologias utilizadas

- Python
- Tkinter
- Programação Orientada a Objetos
- PyInstaller

## Estrutura do projeto

```text
CalculadoraPOO/
│
├── operacoes.py
├── historico.py
├── calculadora.py
├── interface.py
├── main.py
├── testes.py
└── README.md
```

### Descrição dos arquivos

- `operacoes.py`: contém as classes responsáveis pelas operações matemáticas.
- `historico.py`: armazena e gerencia o histórico de cálculos.
- `calculadora.py`: controla a execução das operações e o histórico.
- `interface.py`: contém a interface gráfica desenvolvida com Tkinter.
- `main.py`: arquivo principal responsável por iniciar o programa.
- `testes.py`: contém os testes das funcionalidades da calculadora.

## Conceitos de POO aplicados

Durante o desenvolvimento foram utilizados os seguintes conceitos:

- **Classes e objetos:** utilizados para organizar as funcionalidades da aplicação.
- **Encapsulamento:** protege os atributos e organiza o acesso aos dados.
- **Abstração:** define uma estrutura comum para as operações matemáticas.
- **Herança:** permite que as operações específicas herdem características de uma classe base.
- **Polimorfismo:** permite executar diferentes operações por meio de uma estrutura comum.
- **Composição:** permite que a calculadora utilize o histórico como parte de seu funcionamento.

## Como executar o projeto

É necessário ter o Python instalado no computador.

1. Abra o terminal na pasta do projeto.
2. Execute o seguinte comando:

```bash
python main.py
```

A interface gráfica da calculadora será aberta.

## Como executar os testes

Para verificar o funcionamento das operações e do histórico, execute:

```bash
python testes.py
```

## Como gerar o executável

Para transformar o projeto em um arquivo `.exe`, instale o PyInstaller:

```bash
python -m pip install pyinstaller
```

Depois, execute:

```bash
python -m PyInstaller --onefile --windowed --name CalculadoraPOO main.py
```

Após a conclusão, o executável estará disponível na pasta:

```text
dist/CalculadoraPOO.exe
```

## Considerações finais

O desenvolvimento deste projeto permitiu aplicar na prática os principais conceitos de Programação Orientada a Objetos utilizando Python.

Além disso, foi possível trabalhar com interfaces gráficas, organização de arquivos, validação de dados, tratamento de erros e testes de funcionamento.
