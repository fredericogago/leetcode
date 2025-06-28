# 🧠 LeetCode Python Clean Code

Repositório com soluções para problemas do [LeetCode](https://leetcode.com/) escritos em **Python 3.13**, seguindo princípios de **Clean Code**, **SOLID**, boas práticas de performance e documentação.

---

## 🚀 Objetivo

- Demonstrar proficiência em resolução de problemas usando Python
- Criar portfólio técnico atrativo para recrutadores
- Aplicar boas práticas de design e arquitetura mesmo em algoritmos

---

## 🧩 Estrutura do repositório

Organizado por categorias:

- arrays/
- strings/
- dp/
- trees/
- graphs/
- math/
- utils/


Cada solução inclui:

- Explicação do problema
- Link para o LeetCode
- Estratégia de resolução
- Complexidades
- Type hints e docstrings

---

## ✅ Progresso

| Categoria | Feitos | Exemplos                       |
|----------|--------|--------------------------------|
| Arrays   | ✅ 1    | `two_sum.py`                   |
| Strings  | ⏳ 0    |                                |
| DP       | ⏳ 0    |                                |
| Árvores  | ⏳ 0    |                                |
| Grafos   | ⏳ 0    |                                |
| Math     | ⏳ 0    |                                |

---

## 📌 Exemplo de solução

```python
"""
Problem: Two Sum
LeetCode: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Tags: Array, HashMap

Approach:
- Itera pelos números e usa um dicionário para guardar o complemento

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    lookup: dict[int, int] = {}
    for i, num in enumerate(nums):
        if (diff := target - num) in lookup:
            return [lookup[diff], i]
        lookup[num] = i
```


## ⚙️ Como usar este repositório


```bash
# Clona o repositório
git clone https://github.com/seu-usuario/leetcode-python-clean-code.git

# Resolve novos desafios
# Adiciona os arquivos na pasta correta

# Executa o script para fazer commit e push
./scripts/commit_and_push.sh "Add solution for X problem [medium, dp]"
```

## 📣 Contato

- [LinkedIn](www.linkedin.com/in/frederico-gago-5849281aa)
- [GitHub](https://github.com/fredericogago)
- [Website](https://fredericogago.github.io/frederico-gago/)
