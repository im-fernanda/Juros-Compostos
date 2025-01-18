<h1 align="center" style="font-weight: bold;"> TechFlow - Juros Compostos </h1>

<p align="center"> 
  <a href="#features">Funcionalidades</a> • 
  <a href="#started">Instruções</a> • 
  <a href="#tech">Tecnologias utilizadas</a>
</p>

<p align="justify">
Este repositório foi desenvolvido como parte da disciplina Planejamento e Gerência de Projetos, com o objetivo de demonstrar a aplicação de boas práticas no uso do Git e GitHub. O cenário do projeto envolve a contratação pela empresa fictícia TechFlow Solutions para criar e gerenciar um software no GitHub, com foco em versionamento eficiente, organização estruturada e documentação clara. O projeto consiste em um sistema simples destinado ao cálculo de juros compostos.

</p>

---  

<h2 id="features">📝 Funcionalidades </h2>

A calculadora permite calcular o crescimento de um capital inicial baseado em uma taxa de juros composta ao longo de um número definido de períodos. Além disso, é possível:
- Gerar uma tabela detalhada de como os juros e o montante evoluem a cada período.
- Exportar os resultados para um arquivo Excel.
- Visualizar a evolução do montante por meio de gráficos

---


## 🔢 Exemplos de Entrada e Saída

### Entrada
- Capital inicial: **R$ 1.000,00**
- Taxa de juros: **5% por período**
- Tempo: **12 períodos**

### Saída
```plaintext
Montante Final: R$ 1.795,85
Juros Totais: R$ 795,85
```

---  

<h2 id="started">🚀 Instruções </h2>

1. Certifique-se de ter o Python instalado (versão 3.7 ou superior).
2. Clone o repositório e acesse o diretório do projeto:
   ```bash
   git clone https://github.com/im-fernanda/juros-compostos.git
   cd juros-compostos
3. Instale as dependências do projeto:
    ```bash
    flutter pub get
4. Execute o arquivo principal:
    ```bash  
    python juros_compostos.py
    
Para validar o funcionamento da calculadora, execute:
  ```bash
  python -m unittest test_juros_compostos.py
```

---  

<h2 id="tech">🛠️ Tecnologias Utilizadas </h2>
Python: Linguagem principal. <br>
Pandas: Para manipulação de tabelas e exportação para Excel. <br>
Matplotlib: Para a geração de gráficos.

