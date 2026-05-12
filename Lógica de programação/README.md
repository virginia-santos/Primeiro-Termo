# Lógica de Programação com Python
## Do Algoritmo ao Código Limpo e Versionado

### 1. Fundamentos de Lógica em Python
Python é uma linguagem de sintaxe limpa, ideal para traduzir algoritmos de forma direta.

#### Variáveis e Tipos de Dados
```python
# Tipagem dinâmica, mas forte
sensor_id = "A10"       # string
temperatura = 25.5      # float
ativo = True            # boolean
```

#### Estruturas de Controle
*   **Condicionais:** `if`, `elif`, `else`.
*   **Repetição:** `for` (iteração sobre coleções) e `while` (repetição baseada em condição).

---

### 2. Princípios de Clean Code (Código Limpo)
Escrever código que humanos entendam, não apenas máquinas.

*   **Nomes Significativos:** Use `temperatura_estufa` em vez de `t`.
*   **Funções Pequenas:** Uma função deve fazer apenas uma coisa (Princípio da Responsabilidade Única).
*   **Comentários:** Devem explicar o "porquê", não o "quê". Se o código está claro, o comentário é desnecessário.
*   **PEP 8:** Siga o guia de estilo oficial do Python (espaçamentos, identação, nomes de classes).

#### Exemplo: Refatorando para Clean Code
**Ruim:**
```python
def p(a, b):
    return a * b # multiplica
```

**Bom (Clean):**
```python
def calcular_area_retangulo(base: float, altura: float) -> float:
    """Calcula a área para o dimensionamento do hardware."""
    return base * altura
```

---

### 3. Versionamento com Git & GitHub
O GitHub não é apenas um backup, é uma ferramenta de colaboração e portfólio.

#### Comandos Essenciais (Terminal)
1. **Iniciar repositório:** `git init`
2. **Status dos arquivos:** `git status`
3. **Adicionar para "palco":** `git add .`
4. **Salvar snapshot:** `git commit -m "feat: adiciona calculo de sensores"`
5. **Enviar para a nuvem:** `git push origin main`

#### O arquivo `.gitignore`
Sempre inclua um arquivo `.gitignore` para não subir arquivos desnecessários como:
*   `__pycache__/`
*   `.env` (senhas e chaves de API)
*   Ambientes virtuais (`venv/`)

---

### 4. Fluxo de Trabalho do Aluno
Para cada aula/projeto:
1. Crie uma pasta para o projeto.
2. Inicie o Git.
3. Desenvolva a lógica aplicando **Clean Code**.
4. Faça pequenos commits (atômicos) explicando o que foi feito.
5. Suba para o seu GitHub pessoal.

---

### 5. Desafio de Lógica
**O Problema:** Crie um programa que leia uma lista de temperaturas de sensores.
1. Filtre apenas as temperaturas acima de 30°C.
2. Calcule a média dessas temperaturas.
3. **Requisito Clean Code:** Crie uma função específica para o cálculo da média.
4. **Requisito Git:** Suba a solução para um repositório chamado `logica-python-exercicios`.

---

### 6. Recursos Adicionais
*   [Real Python (Tutoriais)](https://realpython.com)
*   [Guia de Estilo PEP 8](https://python.org)
*   [Documentação Oficial do Git](https://git-scm.com)
