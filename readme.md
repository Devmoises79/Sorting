# 🗂️ Sistema de Ordenação de Números

Este é um pequeno sistema em Python que ordena uma lista de números em **ordem crescente** ou **decrescente**, de acordo com a escolha do usuário.

---

## 📌 Funcionalidades
- Exibe um menu para o usuário escolher o tipo de ordenação:
  - `c` → crescente
  - `d` → decrescente
- Validação de entrada (não aceita opções inválidas).
- Saída formatada para melhor visualização no terminal.

---

## 💻 Exemplo de Uso

### Entrada:

```text
=======================================================================
                 SISTEMA DE ORDENAÇÃO DE NÚMEROS
=======================================================================
Digite 'c' para crescente ou 'd' para decrescente: c
Saída:

Lista em ordem CRESCENTE:
[1, 3, 5, 7, 8]
=======================================================================
text```

## 🚀 Como Executar
Tenha o Python 3 instalado.

Salve o arquivo principal como ordenacao.py.

Execute no terminal:

```bash

python ordenacao.py
```

## 🧪 Testes
Além do código principal (ordenacao.py), este projeto inclui o arquivo test.py, que contém listas pré-definidas para testar o sistema:

python
Copiar
Editar
import random 

# Lista aleatória
any_numbers = random.sample(range(1, 1000), 42)

# Lista já quase ordenada
already_sorted = [1, 2, 3, 4 , 5 , 6 , 9, 20, 22, 23, 28,
                  32, 34, 76, 39, 40 , 42, 87, 99, 112]

# Lista em ordem inversa (pior caso para alguns algoritmos)
* inversed = [117, 90, 88, 83, 81, 77, 74, 69, 64, 63, 51, 
            50, 49, 42, 41, 34, 32, 29, 28, 22, 16 ,8 , 6, 5, 3, 1]

* Como usar nos testes:
- Importe as listas no seu código:

``` python

from test import any_numbers, already_sorted, inversed
``` 

* Defina qual lista quer testar:

```python

lista = inversed  # ou any_numbers, ou already_sorted
```

- Execute o programa normalmente e veja o resultado.


## 🛠️ Tecnologias Utilizadas
- Python 3

- Funções nativas: sorted(), input(), print()

## 📄 Licença
* Este projeto é de uso livre para estudos e modificações.

