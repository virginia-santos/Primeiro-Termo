# Sistemas Operacionais
## Guia de Aula: Gerenciamento, Filosofias de Software e Instalação Linux

### 1. O que é um Sistema Operacional?
O SO é a camada de software que atua como intermediária entre o **usuário** e o **hardware**. Ele gerencia os recursos para que as aplicações funcionem de forma eficiente e segura.

---

### 2. Gerenciamento de Hardware
O SO controla os componentes físicos através de quatro pilares principais:

*   **Processador (CPU):** Escalonamento de processos (quem usa a CPU e por quanto tempo).
*   **Memória (RAM):** Alocação de espaços para programas e proteção de memória (evitar que um programa invada o espaço de outro).
*   **Dispositivos de E/S (Entrada e Saída):** Gerenciamento de periféricos (teclado, mouse, discos, placas de rede) através de *drivers*.
*   **Sistemas de Arquivos:** Organização de como os dados são gravados e lidos no armazenamento (HD/SSD).

---

### 3. Código Aberto vs. Código Fechado


| Característica | Código Aberto (Open Source) | Código Fechado (Proprietário) |
| :--- | :--- | :--- |
| **Acesso** | Qualquer um pode ver, modificar e distribuir o código. | Apenas a empresa dona do software tem acesso ao código. |
| **Licença** | Ex: GPL, MIT, Apache. | Ex: EULA (Contrato de Usuário Final). |
| **Custo** | Geralmente gratuito (comunidade). | Geralmente pago (licenciamento). |
| **Exemplos** | Linux (Kernel), Android, FreeBSD. | Windows, macOS, iOS. |

---

### 4. O Ecossistema Linux
O Linux não é um SO único, mas um **Kernel**. O que usamos são as **Distribuições (Distros)**, que combinam o Kernel com ferramentas e interfaces.

*   **Principais Famílias:**
    *   **Debian/Ubuntu:** Foco em facilidade e servidores.
    *   **Red Hat/Fedora/CentOS:** Foco corporativo e estabilidade.
    *   **Arch Linux:** Foco em personalização profunda (usuários avançados).

---

### 5. Guia Prático: Instalação do Linux
Para instalar uma distribuição (ex: Ubuntu ou Linux Mint), seguimos este fluxo:

1.  **Obtenção da ISO:** Download da imagem do sistema no site oficial.
2.  **Criação de Mídia Bootável:** Uso de ferramentas como *Rufus* ou *Ventoy* para preparar um Pendrive.
3.  **Configuração de BIOS/UEFI:** Alterar a ordem de boot para iniciar pelo USB.
4.  **Particionamento de Disco:**
    *   **Swap:** Memória de troca (usada quando a RAM lota).
    *   **Raiz ( / ):** Onde o sistema e programas ficam instalados.
    *   **Home ( /home ):** Onde ficam os arquivos pessoais (opcional separar).
5.  **Configuração de Usuário:** Criação do usuário padrão e senha de administrador (*root*).

---

### 6. Exercício de Fixação
1. Explique o papel do **Kernel** no gerenciamento de hardware.
2. Liste duas vantagens de uma empresa adotar sistemas de **código aberto**.
3. **Mão na Massa:** Identifique no seu computador atual qual o sistema de arquivos utilizado (ex: NTFS no Windows, ext4 no Linux).

---

### 7. Comandos Básicos de Terminal (Pós-Instalação)
*   `ls`: Lista arquivos.
*   `cd`: Navega entre pastas.
*   `sudo apt update`: Atualiza a lista de repositórios (em distros Debian-based).
*   `df -h`: Verifica o uso de espaço em disco.
