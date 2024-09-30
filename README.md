# ifal-dev01-2024
# ifal_library

**Descrição:**

Esta biblioteca Python contém funções utilitárias para obter entrada do usuário de forma segura e robusta.

**Funcionalidades:**

* **get_int(prompt, show_msg=False):** Obtém um número inteiro do usuário.
* **get_float(prompt, show_msg=False):** Obtém um número de ponto flutuante do usuário.
* **get_string(prompt, show_msg=False):** Obtém uma string do usuário.

**Exemplo de Uso:**

'''python
from ifal_library import get_int, get_float, get_string

idade = get_int("Digite sua idade: ")
altura = get_float("Digite sua altura: ")
nome = get_string("Digite seu nome: ")

print(f"Olá, {nome}! Você tem {idade} anos e {altura} metros de altura.")
'''

**Instalação:**

Para instalar esta biblioteca, utilize o seguinte comando:

pip install ifal_library


Analisando e Comentando o Código
Excelente código! As funções get_int, get_float e get_string são ferramentas robustas para garantir a entrada correta de dados pelo usuário em Python. A estrutura de repetição while True garante que a função só retorne um valor válido, enquanto o bloco try-except trata as possíveis exceções de valor, como quando o usuário digita um texto ao invés de um número.

Comentários Adicionados:

Python
def get_int(prompt, show_msg=False):
    """
    Obtém um número inteiro do usuário.

    Args:
        prompt (str): Mensagem a ser exibida para o usuário.
        show_msg (bool, optional): Indica se deve mostrar uma mensagem de erro caso o usuário digite um valor inválido. Defaults to False.

    Returns:
        int: O número inteiro digitado pelo usuário.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            if show_msg:
                print("Não é um número inteiro (integer)")

# ... (similar para get_float e get_string)
Use o código com cuidado.

Explicação dos Comentários:

Docstrings: As docstrings explicam o propósito de cada função, seus argumentos e o valor de retorno. Isso facilita a compreensão do código, especialmente para outros desenvolvedores.
Args: A seção Args descreve os argumentos da função, seus tipos e o que representam.
Returns: A seção Returns indica o tipo de valor que a função retorna.
Criando um Exemplo de Uso e README.md
Exemplo de uso (arquivo main.py):

Python
from ifal_library import get_int, get_float, get_string

idade = get_int("Digite sua idade: ")
altura = get_float("Digite sua altura: ")
nome = get_string("Digite seu nome: ")

print(f"Olá, {nome}! Você tem {idade} anos e {altura} metros de altura.")
Use o código com cuidado.

Conteúdo do README.md:

Markdown
# ifal_library

**Descrição:**

Esta biblioteca Python contém funções utilitárias para obter entrada do usuário de forma segura e robusta.

**Funcionalidades:**

* **get_int(prompt, show_msg=False):** Obtém um número inteiro do usuário.
* **get_float(prompt, show_msg=False):** Obtém um número de ponto flutuante do usuário.
* **get_string(prompt, show_msg=False):** Obtém uma string do usuário.

**Exemplo de Uso:**

```python
from ifal_library import get_int, get_float, get_string

idade = get_int("Digite sua idade: ")
altura = get_float("Digite sua altura: ")
nome = get_string("Digite seu nome: ")

print(f"Olá, {nome}! Você tem {idade} anos e {altura} metros de altura.")
Use o código com cuidado.

Instalação:

Para instalar esta biblioteca, utilize o seguinte comando:

'''Bash
pip install ifal_library
'''

**Contribuições:**

Contribuições são bem-vindas! Para contribuir, por favor, fork este repositório, faça as suas alterações e abra um pull request.

**Licença:**

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.



