# Calculadora Desktop em Python & Tkinter

Uma aplicação desktop robusta, intuitiva e de alta performance desenvolvida em Python. O projeto utiliza a biblioteca nativa **Tkinter** para a construção de uma interface gráfica (GUI) moderna, aplicando conceitos práticos de manipulação de eventos, layout em grid e tratamento preventivo de exceções.

---

## Arquitetura e Uso do Tkinter

O **Tkinter** é a biblioteca padrão do Python para desenvolvimento de interfaces gráficas baseadas no *Tcl/Tk Toolkit*. Neste projeto, ela foi empregada para estruturar toda a camada visual e gerenciar as interações do usuário.

### Principais Componentes Utilizados:
* **`Tk()`**: Inicializa a janela principal do sistema, definindo suas dimensões (`geometry`) e cor de fundo global.
* **`Frame`**: Utilizado para criar divisões lógicas na interface, separando o container do visor (`frame_tela`) do container de controle (`frame_corpo`).
* **`Label` & `StringVar`**: O visor da calculadora utiliza uma `Label` vinculada a uma variável dinâmica (`StringVar`), permitindo atualizações em tempo real do texto na tela conforme o usuário interage com o teclado.
* **`Button`**: Elementos de controle configurados com eventos de clique via funções callback (`command`) e expressões `lambda`, permitindo a passagem de parâmetros dinâmicos para a lógica do sistema.
* **Gerenciadores de Layout (`grid` e `place`)**:
  * **`grid`**: Empregado na estruturação dos containers principais para garantir alinhamento vertical rigoroso.
  * **`place`**: Utilizado na renderização dos botões para um controle preciso de posicionamento por coordenadas X e Y dentro do corpo da calculadora.

---

## Lógica de Desenvolvimento & Engenharia

* **Gerenciamento de Estado:** A aplicação mantém o estado da expressão através de controle de strings, acumulando as entradas e enviando-as para processamento após a ação do usuário.
* **Tratamento de Exceções (`Try / Except`):** Evita falhas no sistema (*crashes*) interceptando exceções como `ZeroDivisionError` (divisão por zero) e `SyntaxError` (expressões malformadas), exibindo mensagens amigáveis diretamente no visor.
* **Formatador de Expressões:** Realiza a sanitização de operadores especiais antes do cálculo (como a conversão dinâmica de `%` para divisões proporcionais).

---

## Funcionalidades

- **Operações Aritméticas Básicas:** Soma, subtração, multiplicação e divisão com precisão.
- **Cálculo Aritmético de Porcentagem:** Tratamento direto para expressões percentuais.
- **Interface Responsiva & Tema Dark:** Layout otimizado com paleta de cores contrastantes baseada em Flat Design.
- **Tratamento Preventivo de Erros:** Exibição de alertas amigáveis em caso de operações matemáticas inválidas.

---

## Tecnologias Utilizadas

- **Python 3.x** — Linguagem base do projeto.
- **Tkinter (Tcl/Tk)** — Biblioteca nativa para a interface gráfica.

---

## Como Rodar o Projeto

### Pré-requisitos
Certifique-se de ter o **Python 3.x** instalado no seu sistema operacional. *(O Tkinter já vem instalado por padrão com a distribuição oficial do Python)*.

### Passo a Passo

1. **Clone este repositório:**
   ```bash
   git clone [https://github.com/joao-lucas-c/calculadora-python.git](https://github.com/joao-lucas-c/calculadora-python.git)
