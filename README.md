# 🧠 LeetCode Python Clean Code

Repositório com soluções para desafios do [LeetCode](https://leetcode.com/) desenvolvidas em **Python 3.13**, aplicando princípios de **Clean Code**, **SOLID**, boas práticas de performance e documentação clara.

---

## 🚀 Objetivo

- 📈 Demonstrar proficiência em resolução de problemas com Python moderno
- 💼 Criar um portfólio técnico atrativo para recrutadores
- 🧩 Aplicar boas práticas de design e arquitetura até mesmo em algoritmos

---

## 🧩 Estrutura do repositório

src
├── __init__.py
├── leetcode
│   └── editor
│       └── en
│           ├── [1]Two Sum.py
│           ├── [9]Palindrome Number.py
└── utils
    └── __init__.py



Cada solução inclui:

- ✅ Explicação clara do problema  
- 🔗 Link direto para o enunciado original  
- 🧠 Estratégia de resolução com boas práticas  
- ⏱️ Análise de complexidade (tempo e espaço)  
- 🧾 Type hints e docstrings seguindo o padrão Google Style

---

## 📌 Exemplo de solução

```python
"""
Problem: Two Sum
LeetCode: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Tags: Array, HashMap

Approach:
- Itera pelos números e utiliza um dicionário para armazenar complementos.
- Se o complemento do número atual já estiver no dicionário, retorna os índices.

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

---

## 📌 Futuras melhorias

* ✅ Testes com `pytest`
* 📊 Benchmarks para comparar abordagens
* 🧠 Templates padrão para novos problemas
* 🌐 Versão traduzida para português e inglês

---

## 📣 Contato

- [LinkedIn](www.linkedin.com/in/frederico-gago-5849281aa)
- [GitHub](https://github.com/fredericogago)
- [Website](https://fredericogago.github.io/frederico-gago/)

---

## 📘 Diário de Progresso

Acompanho minha evolução no ficheiro [`leetcode-journal.md`](./leetcode-journal.md), onde anoto:

- ✅ Problemas resolvidos com link para a solução
- 📌 Problemas que quero revisar ou reescrever
- 🧠 Padrões recorrentes (e.g., sliding window, binary search)
- 📓 Notas sobre otimizações, abordagens alternativas e aprendizados

> Este diário ajuda a manter um ciclo de melhoria contínua — e também serve como referência rápida para revisões técnicas.
