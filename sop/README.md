# Aula de Sistemas Operacionais:

## 🎯 Objetivos de Aprendizado
- Compreender a gestão de [Processos/Memória/Arquivos].
- Praticar comandos de administração via terminal.
- Analisar a interação entre hardware e software.

---

## 🏗️ Conceitos Fundamentais
*Resumo teórico dos pilares abordados nesta aula.*

- **Componente:** [Ex: Kernel, Escalonador, File System]
- **Definição:** Breve explicação do conceito.
- **Importância:** Por que o SO gerencia isso?

---

## 🐚 Prática no Terminal (Shell Script / Comandos)
*Espaço para comandos Linux/Unix fundamentais para a aula.*

### Gerenciamento do Sistema
```bash
# Verificar processos em execução
top

# Listar arquivos com permissões detalhadas
ls -la

# Verificar uso de memória
free -h
```

### Script de Automação (Exemplo)
```bash
#!/bin/bash
echo "Iniciando verificação do sistema..."
uptime
df -h
```

---

## 📑 Gerenciamento de Recursos

### 1. Processos e Threads
- **Estados do Processo:** Pronto, Executando, Bloqueado.
- **Escalonamento:** [Ex: Round Robin, FIFO, Prioridade].

### 2. Memória
- **Memória Virtual:** Uso de paginação e segmentação.
- **Swap:** O que acontece quando a RAM lota.

---

## 🛠️ Laboratório Prático
**Cenário:** Simulação de Deadlock ou Gerenciamento de Permissões.

1.  **Tarefa 1:** Criar uma estrutura de diretórios e alterar donos (`chown`) e permissões (`chmod`).
2.  **Tarefa 2:** Identificar processos que consomem mais CPU e finalizá-los (`kill`).

---

## 📝 Questões de Revisão
1. Qual a diferença entre uma **Thread** e um **Processo**?
2. O que é uma **Chamada de Sistema (System Call)**?
3. Explique o conceito de **Interrupção**.

---
*Referências: [Dinossauro (Silberschatz)](https://os-book.com) | [Tanenbaum](https://pearson.com)*