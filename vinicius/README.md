## Aula de Programação:

## 🎯 Objetivos da Aula
- Aplicar conceitos de **Clean Code** em scripts Python.
- Gerenciar versões do código com **Git**.
- Colaborar e hospedar projetos no **GitHub**.

---

## 🐍 Desenvolvimento em Python
*Espaço para o código da aula focando em lógica e sintaxe.*

```python
# Exemplo de script Python
def calcular_media(notas):
    return sum(notas) / len(notas)

if __name__ == "__main__":
    minhas_notas = [8.5, 9.0, 7.5]
    print(f"A média é: {calcular_media(minhas_notas)}")
```

---

## ✨ Princípios de Clean Code Aplicados
*Regras de ouro para manter o código legível e profissional:*

1.  **Nomes Significativos:** Variáveis e funções devem dizer a que vieram (ex: `soma_total` em vez de `s`).
2.  **Funções Pequenas:** Cada função deve fazer apenas uma coisa.
3.  **Comentários Necessários:** O código deve ser claro o suficiente para não precisar de excesso de comentários.
4.  **DRY (Don't Repeat Yourself):** Evite repetição de lógica.

---

## 🛠️ Fluxo Git & GitHub
*Guia rápido para os comandos utilizados no projeto.*

### Configuração Inicial
```bash
git init
git remote add origin [URL-DO-REPOSITORIO]
```

### Ciclo de Trabalho
1. **Status:** `git status` (verificar alterações)
2. **Stage:** `git add .` (preparar arquivos)
3. **Commit:** `git commit -m "feat: implementa função de média"`
4. **Push:** `git push origin main` (enviar para o GitHub)

---

## 📁 Estrutura do Projeto
*Como organizar as pastas seguindo padrões de mercado:*

- `src/` (Código fonte)
- `tests/` (Testes unitários)
- `docs/` (Documentação extra)
- `README.md` (Explicação do projeto)
- `.gitignore` (Arquivos que o Git deve ignorar)

---

## 🚀 Desafio do Projeto
Crie um programa que receba dados do usuário, aplique os conceitos de **Clean Code** discutidos e suba para um novo repositório no seu **GitHub** utilizando pelo menos 3 commits diferentes.

---
*Dica: Utilize o [Guia de Estilo PEP 8](https://python.org) para padronizar seu P