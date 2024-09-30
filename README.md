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
```
**Instalação:**

Para instalar esta biblioteca, utilize o seguinte comando:
```bash
pip install ifal_library
```

**Contribuições:**

Contribuições são bem-vindas! Para contribuir, por favor, fork este repositório, faça as suas alterações e abra um pull request.

**Licença:**

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
