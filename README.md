
# 🧮 Laboratório Completo: Calculadora com CI (GitHub Actions) e Interface Web (Streamlit)

Este repositório contém um laboratório prático completo de **Integração Contínua (CI)** e **Deploy Local/Web** utilizando a linguagem Python. O projeto evoluiu de uma biblioteca simples de funções matemáticas para um Web App interativo totalmente testado de forma automatizada na nuvem.

---

## 🚀 O que este projeto faz?
1. **Lógica Matemática (`src/`):** Possui funções estáveis de soma e divisão (com tratamento de exceção para divisão por zero).
2. **Qualidade Garantida (`tests/`):** Contém testes automatizados usando a biblioteca **PyTest**.
3. **Automação na Nuvem (`.github/workflows/`):** Toda vez que um `push` é feito, o **GitHub Actions** valida se o código está correto e seguro.
4. **Interface Visual (`app.py`):** Um painel web dinâmico feito com **Streamlit** que permite usar a calculadora pelo navegador do computador e pelo celular!

---

## 🛠️ Tecnologias e Ferramentas Utilizadas
* **Linguagem:** Python 3.10
* **Framework de Testes:** PyTest
* **Interface Web:** Streamlit
* **Editor de Código:** Visual Studio Code (VS Code)
* **Controle de Versão:** GitHub Desktop & Git
* **Esteira de Automação:** GitHub Actions (CI)

---

## 📂 Estrutura Final do Projeto
A árvore de arquivos do repositório deve ficar exatamente assim:

```text
meu_projeto/
├── .github/
│   └── workflows/
│       └── python-app.yml     # Configuração do robô do GitHub Actions
├── src/
│   └── calculadora.py         # Arquivo fonte com as regras de negócio
├── tests/
│   └── test_calculadora.py    # Suite de testes automatizados com PyTest
├── app.py                     # Interface Web do projeto (Streamlit)
├── .gitattributes             # Configurações de atributos do Git
└── requirements.txt           # Declaração das dependências do ambiente

## ⌨️ Histórico de Todos os Comandos do Terminal (Ordem Cronológica)

Para fins de registro, aqui está a sequência exata de comandos executados no terminal do VS Code durante todo o desenvolvimento deste laboratório:

1. **Instalação Inicial do PyTest (Ambiente de Testes):**
   ```bash
   pip install pytest

 2  Execução dos Testes Automatizados Localmente:

   PYTHONPATH=src python -m pytest tests/

  3 Abertura do Interpretador Interativo do Python (Para testar funções ao vivo):

   python

  4 Comandos digitados DENTRO do modo interativo do Python (>>>):

   from src.calculadora import somar, dividir
somar(10, 5)
dividir(10, 2)
dividir(10, 0)
exit()

5 Instalação das novas dependências atualizadas (PyTest + Streamlit):

pip install -r requirements.txt

6 Inicialização do Servidor da Calculadora Web:

streamlit run app.py

7 Comando para desligar o servidor web e liberar o terminal:

Pressionar as teclas: Ctrl + C

---

### 💾 Salvando e Atualizando o GitHub

1. Após colar esse bloco no final do arquivo, salve com **`Ctrl + S`**.
2. Abra o **GitHub Desktop**.
3. Ele vai detectar que você adicionou essas novas linhas ao `README.md`.
4. Faça o commit (ex: `Docs: adicionando histórico de comandos do terminal`).
5. Clique em **Push origin**.


📝 Linha do Tempo do Laboratório (Passo a Passo)
Passo 1: Inicialização do Projeto
Criamos o repositório no GitHub Desktop e o publicamos como público no GitHub para habilitar os servidores gratuitos do GitHub Actions.

Estruturamos as pastas e os arquivos dentro do VS Code.

Passo 2: Desenvolvimento Seguro
Desenvolvemos as funções de soma e divisão em src/calculadora.py. Na divisão, adicionamos uma proteção para lançar um erro (ValueError) caso o usuário tente dividir por zero.

Criamos os testes correspondentes em tests/test_calculadora.py usando assert para garantir que o comportamento estaria correto.

Passo 3: Configuração da Esteira na Nuvem (CI)
Criamos o arquivo .github/workflows/python-app.yml. Ele ensina o robô do GitHub a:

Ligar um servidor Linux virtual toda vez que enviamos código novo (push).

Instalar o Python e as dependências do requirements.txt.

Rodar o comando do pytest para verificar se tudo está funcionando perfeitamente.

Passo 4: O Teste de Estresse do Robô
Validamos o comportamento do robô em três momentos na aba Actions do GitHub:

Sucesso (✓): O primeiro código subiu estável e o robô deu o selo verde de aprovação.

Bloqueio de Erro (❌): Alteramos o teste de soma de propósito para esperar um resultado absurdo (assert somar(2,3) == 99). O robô interceptou o erro na nuvem, interrompeu o processo e nos avisou onde estava a falha de segurança.

Correção (✓): Corrigimos o código para o valor real (5), enviamos de novo e o robô voltou a ficar verde, garantindo a estabilidade.

Passo 5: Criação da Interface Web e Mobile
Criamos o arquivo app.py utilizando o Streamlit para dar uma interface visual bonita e amigável ao usuário, eliminando a necessidade de usar telas pretas de terminal para interagir com as funções.

💻 Manual de Comandos do Terminal (Guia Prático)
Aqui está o histórico completo de todos os comandos utilizados no terminal do VS Code durante as fases do projeto:

1. Preparação do Ambiente e Testes Locais
Para instalar a ferramenta de testes e rodar as primeiras validações no seu próprio computador:

Bash
# Instala o framework de testes
pip install pytest

# Executa os testes de unidade locais mapeando a pasta src
PYTHONPATH=src python -m pytest tests/
2. Testando Código "Ao Vivo" no Terminal Interativo
Caso queira testar as funções Python linha por linha direto na memória do terminal:

Bash
# Abre o interpretador interativo do Python (o terminal mudará para >>>)
python

# COMANDOS INTERNOS DO PYTHON (Digite um por um e aperte Enter):
from src.calculadora import somar, dividir
somar(10, 5)        # Retornará: 15
dividir(10, 2)      # Retornará: 5.0
dividir(10, 0)      # Exibirá a mensagem: ValueError: Divisão por zero!
exit()              # Sai do modo interativo e volta ao terminal normal
3. Rodando o Aplicativo na Web e no Celular
Para instalar a interface visual e ligar o servidor do seu site:

Bash
# Instala todas as dependências do projeto de uma vez (PyTest + Streamlit)
pip install -r requirements.txt

# Liga o servidor local do aplicativo web
streamlit run app.py
💡 Nota de Execução: Na primeira vez que rodar o comando acima, o terminal perguntará se deseja cadastrar um e-mail. Deixe o campo vazio e aperte Enter no teclado para pular.

🛜 Como acessar pelo celular:
Ao ligar o servidor, o Streamlit exibirá duas URLs no terminal:

Local URL: Use para acessar no navegador do próprio computador (http://localhost:8501).

Network URL: O endereço IP para conectar outros aparelhos (Exemplo: http://192.168.1.5:8501).

Certifique-se de que o computador e o celular estão conectados na mesma rede Wi-Fi.

Abra o navegador do seu celular (Chrome, Safari, etc.) e digite o endereço completo gerado na sua Network URL.

Para desligar o servidor do site e liberar o terminal do VS Code quando terminar, pressione as teclas: Ctrl + C.





