# Engenharia de Requisitos: Da Descoberta ao Documento
## Guia de Aula: Levantamento, Análise e Documentação

### 1. Introdução ao Levantamento de Requisitos
O objetivo principal é entender as necessidades das partes interessadas (*stakeholders*) para definir o que o sistema deve fazer.

---

### 2. Técnicas de Elicitação (Coleta)

#### A. Brainstorming
*   **O que é:** Reunião criativa para gerar o máximo de ideias sem julgamentos prévios.
*   **Objetivo:** Explorar novas funcionalidades e soluções inovadoras.
*   **Dica:** Use post-its ou ferramentas digitais como Miro ou Jamboard.

#### B. Entrevistas
*   **Estruturadas:** Roteiro fixo de perguntas.
*   **Não estruturadas:** Conversa aberta para explorar o domínio do problema.
*   **Dica:** Sempre grave ou faça anotações focadas na "dor" do usuário.

#### C. Prototipagem
*   **Baixa Fidelidade:** Desenhos em papel (wireframes).
*   **Alta Fidelidade:** Protótipos interativos (Figma, Adobe XD).
*   **Objetivo:** Validar requisitos visualmente antes da codificação.

---

### 3. Classificação de Requisitos


| Tipo | Definição | Exemplo |
| :--- | :--- | :--- |
| **Funcionais (RF)** | Descrevem as funções e o comportamento do sistema. | "O sistema deve permitir o cadastro de sensores IoT." |
| **Não Funcionais (RNF)** | Descrevem restrições, atributos de qualidade e desempenho. | "O sistema deve responder a requisições em menos de 2s." |

---

### 4. Modelagem e Diagramas (UML)
Os diagramas ajudam a visualizar a estrutura e o comportamento do software.

*   **Diagrama de Caso de Uso:** Mostra as interações entre os atores (usuários/sistemas) e as funcionalidades.
*   **Diagrama de Sequência:** Detalha a troca de mensagens entre objetos ao longo do tempo.
*   **Diagrama de Classes:** Define a estrutura lógica de dados e métodos.

---

### 5. Documentação e Relatórios Técnicos
A entrega final do levantamento costuma ser o **Documento de Especificação de Requisitos de Software (ERS)**.

#### Estrutura Sugerida:
1.  **Introdução:** Objetivo do sistema e escopo.
2.  **Descrição Geral:** Perspectiva do produto e funções principais.
3.  **Requisitos Funcionais:** Lista numerada (RF01, RF02...).
4.  **Requisitos Não Funcionais:** (RNF01, RNF02...).
5.  **Modelos de Análise:** Inclusão dos diagramas criados.

---

### 6. Exercício Prático
**Cenário:** Sistema de Monitoramento de Estufa Inteligente.
1.  Realize um **Brainstorming** em grupo para listar 5 ideias.
2.  Defina **3 Requisitos Funcionais** (ex: leitura de umidade).
3.  Defina **2 Requisitos Não Funcionais** (ex: segurança de dados).
4.  Desenhe um **Protótipo de Baixa Fidelidade** da tela principal.

---

### 7. Ferramentas Recomendadas
*   **Gestão:** Jira, Trello, Azure DevOps.
*   **Diagramação:** Lucidchart, Draw.io, StarUML.
*   **Prototipagem:** Figma, Penpot.
