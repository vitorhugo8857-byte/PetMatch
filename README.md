# PetMatch: Plataforma de Adoção Consciente 🐾

## Tema do Projeto
Desenvolvimento de solução mobile responsável pela conexão assertiva entre adotantes e animais em situação de vulnerabilidade, apopriando da análise de dados para assegurar adoções responsáveis.

## Objetivo da Análise
Identificação de padrões de compatibilidade entre perfil psicossocial do adotante e necessidades do pet, visando redução de taxas de devolução e tempo de permanência dos animais em abrigos.

## Integrantes
* [vitorhugo8857-byte] - RM: 001

##Estrutura inicial do projeto
1. **/data:** Armazenamento de datasets (arquivos .csv ou .json) sobre abrigos e animais.
2. **/src:** Código-fonte da aplicação (Backend/Frontend).
3. **/docs:** Documentação complementar, diagramas de entidade-relacionamento e protótipos.
4. **/analysis:** Scripts (Python/R) para o processamento de dados e geração de métricas.

## Definição de base de dados
1. **Escolha da Base:** Utilização de combinação de PostgreSQL (para dados estruturados de usuários e pets) e Firebase Firestore (para atualizações em tempo real de chats e notificações). Em fase de análise, podem ser importados datasets públicos de bem-estar animal (como os do Austin Animal Center) para treinamento do modelo de compatibilidade.
2. **Contexto e Objetivo:** A base gerencia o ciclo de vida do pet, desde o resgate até a adoção final. O objetivo da análise é cruzar variáveis comportamentais (porte, energia, sociabilidade) com o perfil do adotante (estilo de vida, espaço físico) para prever a taxa de sucesso da adoção.

## Planejamento de Tarefas
1. **Estruturação:** Setup do repositório e definição da arquitetura de dados.
2. **Desenvolvimento:** Implementação do sistema de match e interface mobile.
3. **Análise:** Processamento de métricas de impacto social e eficácia de adoção.
4. **Entrega:** Dashboard de monitoramento para ONGs parceiras.

### Definição de Tarefas e Cronograma
#### Semana 1
* Tarefa: Modelagem do Banco de Dados e Setup do GitHub
* Responsável: Colaborador 001, Colaborador 002

#### Semana 2
* Tarefa: Desenvolvimento do Algoritmo de Match (Lógica de Compatibilidade)
* Responsável: Colaborador 003, Colaborador 004, Colaborador 005

#### Semana 3
* Tarefa: Criação do Dashboard de Métricas e Análise de Dados
* Responsável: Colaborador 006, Colaborador 007

#### Semana 4
* Tarefa: Finalização da Documentação e Testes de Usabilidade
* Responsável: Todos

### Transformações de Dados
1. **Categorização por Score:** Transformar respostas do formulário de adoção em valores numéricos para cálculo de compatibilidade.
2. **Tratamento de Datas:** Calcular o "Tempo de Permanência" (Data de entrada - Data atual) para identificar animais que precisam de maior visibilidade.
3. **Padronização Geográfica:** Converter endereços em coordenadas para calcular o raio de distância entre adotante e animal.

### Visualizações e Métricas (Dashboard)
1. **Métrica de Sucesso:** Porcentagem de matches que resultaram em adoção efetiva.
2. **Tempo Médio para Adoção:** Segmentado por raça, porte e idade.
3. **Mapa de Calor:** Áreas com maior demanda de adoção vs. áreas com maior concentração de animais abandonados.

## Ideia Inicial de Dashboard
O dashboard será focado em **Gestão de Impacto**, apresentando:
- Indicadores de "Adoções de Longa Permanência" (animais idosos ou com deficiência).
- Gráficos de funil: Visualizações -> Interesse -> Visita -> Adoção.
- Ranking de compatibilidade média por região.

## Execução e Link de visualização
Visualização foi publicada e pode ser acessada em: [https://petmatch-v8857.streamlit.app/]

## Tecnologias Utilizadas
- **Linguagem:** Python
- **Dashboard:** Streamlit & Plotly
- **Banco de Dados:** PostgreSQL (Estrutura) & Firebase (Tempo Real)
- **Hospedagem:** Streamlit Cloud

## Resultados da Análise (Dashboard)
Dashboard apresenta métricas de assertividade de match e tempo de permanência, permitindo aos gestores de ONGs, identificação acerca de tempo de adoção de perfis de animais e ajustes de estratégias de divulgação.
