# Sistema de Elevador de Prédio
# O prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para cima ou para baixo, e tem a capacidade de transportar até 5 pessoas.
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo, descendo, parando). O programa deve continuar rodando até que o usuário decida encerrar.

# Documento de Levantamento de Requisitos: Sistema de Elevador
# 1. Descrição Geral do Sistema
# O sistema tem como objetivo gerenciar e simular o comportamento de um elevador em um prédio residencial ou comercial de 10 andares. O programa deve controlar a movimentação do elevador, a capacidade de passageiros e interagir com o usuário exibindo o status de cada ação em tempo real, funcionando em um ciclo contínuo até que seja solicitado o encerramento.

# 2. Requisitos Funcionais (RF)
# Os requisitos funcionais descrevem o que o sistema deve fazer (as ações, telas, fluxos e regras de negócio).

# RF01 – Inicialização do Sistema
# Descrição: Ao iniciar, o sistema deve configurar o estado inicial do elevador.

# Regra: O elevador deve começar obrigatoriamente no andar 0 (térreo) e com 0 pessoas a bordo.

# RF02 – Menu de Opções e Chamada do Elevador
# Descrição: O sistema deve solicitar as informações de origem e destino para realizar a viagem.

# Dados de entrada necessários:

# O andar atual onde a pessoa está (Origem).

# O andar para onde a pessoa deseja ir (Destino).

# A quantidade de pessoas que vão entrar.

# RF03 – Controle de Capacidade
# Descrição: O sistema deve validar se o elevador suporta a quantidade de pessoas informada.

# Regra: A capacidade máxima é de 5 pessoas. Se o usuário digitar um número maior que 5 (ou se a soma com quem já está dentro passar de 5), o sistema deve exibir uma mensagem de alerta e barrar a entrada.

# RF04 – Movimentação para o Andar de Chamada (Origem)
# Descrição: O elevador deve se deslocar do seu andar atual até o andar onde o usuário fez a chamada.

# Regra: * Se o andar da pessoa for maior que o andar atual do elevador, o sistema deve exibir mensagens textuais simulando que está subindo andar por andar.

# Se for menor, deve exibir que está descendo andar por andar.

# Ao chegar, deve exibir a mensagem parando e abrir as portas para as pessoas entrarem.

# RF05 – Movimentação para o Andar de Destino
# Descrição: Após o embarque, o elevador deve se deslocar até o andar de destino solicitado.

# Regra: Segue a mesma lógica de atualização de status do RF04 (exibir subindo/descendo andar por andar e parar no destino para o desembarque).

# RF06 – Exibição de Status (Painel do Elevador)
# Descrição: A cada mudança de estado ou de andar, o sistema deve imprimir na tela as informações atuais para o usuário.

# Dados obrigatórios no print: Andar atual, número de pessoas a bordo e a ação que está acontecendo (subindo, descendo ou parando).

# RF07 – Encerramento do Programa
# Descrição: O sistema deve perguntar ao usuário se ele deseja continuar realizando simulações ou encerrar o programa.

# 3. Requisitos Não Funcionais (RNF)
# Os requisitos não funcionais descrevem como o sistema deve funcionar (características de qualidade, restrições técnicas, limites).

# RNF01 – Limites do Cenário (Restrição de Escopo)
# Descrição: O prédio possui um limite físico estrito.

# Regra: O sistema não pode aceitar andares menores que 0 (térreo) e nem maiores que 10.

# RNF02 – Ciclo de Vida do Programa (Disponibilidade)
# Descrição: O programa deve ser capaz de realizar infinitas viagens consecutivas.

# Regra: O código deve utilizar uma estrutura de repetição contínua (while True) para que o elevador não "resete" ou feche após levar apenas uma pessoa. O estado final da última viagem (andar atual) deve ser o estado inicial da próxima.

# RNF03 – Robustez e Tratamento de Erros (Confiabilidade)
# Descrição: O sistema não pode quebrar (fechar com erro na tela) caso o usuário digite dados inválidos.

# Regra: O programa deve validar se as entradas são números inteiros válidos. Caso o usuário digite letras no lugar de andares ou números de pessoas, o sistema deve tratar o erro com try-except e pedir o dado novamente.

# RNF04 – Interface de Usuário Simples (Usabilidade)
# Descrição: A interface do sistema deve ser baseada em modo texto (Terminal/Console).

# Regra: As mensagens textuais devem ser claras, limpas e indicar o passo a passo de forma cronológica (ex: "Elevador no andar 1...", "Elevador no andar 2...").