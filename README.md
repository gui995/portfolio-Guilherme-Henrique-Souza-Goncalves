<!-- BANNER DE APRESENTAÇÃO -->
<div align="center">

```
╔═══════════════════════════════════════════════════════════╗
║   👨‍💻  GUILHERME HENRIQUE SOUZA GONÇALVES                 ║
║   🔧  Infraestrutura · Cloud · Suporte Avançado · Web     ║
╚═══════════════════════════════════════════════════════════╝
```

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=22&pause=1000&color=0078D4&center=true&vCenter=true&width=600&lines=Analista+de+Suporte+Pleno;Azure+AD+%7C+Intune+%7C+Microsoft+365;Estudante+de+TI+em+constante+evolução;Explorando+o+mundo+do+desenvolvimento+web)](https://git.io/typing-svg)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/guilherme-gonçalves-b60597241/)
[![E-mail](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:guihsg31@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/gui995)

</div>

---

## 👨‍💻 Sobre mim

Profissional de TI com atuação em ambientes corporativos complexos, combinando sólida experiência em **infraestrutura, cloud e suporte avançado** com o crescente interesse em **desenvolvimento web**. Atualmente cursando Gestão da Tecnologia da Informação e expandindo minhas habilidades para o universo do desenvolvimento front-end.

```yaml
Nome        : Guilherme Henrique Souza Gonçalves
Cargo Atual : Analista de Suporte Pleno
Formação    : CST em Gestão da TI — Universidade Cidade de São Paulo (2025–2027)
Localização : São Paulo, SP — Brasil 🇧🇷
Foco Atual  : Infraestrutura Cloud + Desenvolvimento Web (HTML/CSS)
Disponível  : Para projetos, estágios e colaborações
```

---

## 🛠️ Stack Técnica

### ☁️ Cloud & Identidade
![Azure](https://img.shields.io/badge/Microsoft_Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Azure AD](https://img.shields.io/badge/Azure_AD_(Entra_ID)-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Microsoft 365](https://img.shields.io/badge/Microsoft_365-D83B01?style=for-the-badge&logo=microsoftoffice&logoColor=white)
![Intune](https://img.shields.io/badge/Microsoft_Intune-0078D4?style=for-the-badge&logo=microsoft&logoColor=white)

### 🖥️ Sistemas Operacionais & Endpoints
![Windows](https://img.shields.io/badge/Windows_Server-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![macOS](https://img.shields.io/badge/macOS-000000?style=for-the-badge&logo=apple&logoColor=white)
![Active Directory](https://img.shields.io/badge/Active_Directory-003087?style=for-the-badge&logo=windows&logoColor=white)

### 🌐 Redes & Segurança
![Wireshark](https://img.shields.io/badge/Wireshark-1679A7?style=for-the-badge&logo=wireshark&logoColor=white)
![VPN](https://img.shields.io/badge/VPN_(IPSec%2FSSL)-333333?style=for-the-badge&logo=cisco&logoColor=white)
![TCP/IP](https://img.shields.io/badge/TCP%2FIP%20%7C%20DNS%20%7C%20DHCP-02569B?style=for-the-badge&logo=cloudflare&logoColor=white)

### 💻 Desenvolvimento Web (Acadêmico)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

### 📋 Gestão & Processos
![ITIL](https://img.shields.io/badge/ITIL-6A0DAD?style=for-the-badge&logo=bookstack&logoColor=white)
![SCCM](https://img.shields.io/badge/SCCM_/_Endpoint_Manager-0078D4?style=for-the-badge&logo=microsoft&logoColor=white)

---

## 📂 Portfólio de Projetos


# Relatório Técnico: Algoritmo de Auditoria de Vendas e Teste de Estresse

## 🧐 O Conceito: Discrepância e Normalização
Este projeto simula um sistema bancário que busca por **Outliers** (valores atípicos). 
- **O Problema:** Uma única venda muito alta pode distorcer a média, mascarando falhas ou fraudes.
- **A Solução:** Implementamos uma lógica de **Normalização**, onde o sistema ignora o "ruído" para focar na massa crítica dos dados.

## ⚖️ Lógica de Negócio: Margem de Tolerância
O algoritmo utiliza o conceito de **Materialidade**. Em auditoria, não investigamos cada centavo se o custo da investigação for maior que o erro. O sistema foca o esforço computacional onde o risco é real.

## 🛠️ O Código e a "Vulnerabilidade Consciente"
O script realiza o casting de dados (tratando vírgulas e pontos) e processa os alertas de quarentena.
> **Nota de Engenharia:** Durante o desenvolvimento, foi identificado que o uso de `global LIMITE_SEGURANCA` é uma vulnerabilidade. Em sistemas reais, esses limites devem ser **Encapsulados** para evitar que scripts maliciosos alterem as regras de auditoria na memória compartilhada.

## 🧪 Teste de Estresse (Cenário Real)
- **Entradas:** 100, 200, 5000.
- **Resultado:** Média de R$ 1.766,66.
- **Análise Crítica:** O sistema não ativou a quarentena, revelando que o multiplicador de sensibilidade (5x) pode precisar de recalibração para cenários bancários mais rígidos.



### 🌐 Desenvolvimento Web
| Projeto | Descrição | Tecnologias | Link |
| **Maternidade Inteligente** | Site de apoio informativo para mães com assistente virtual, tópicos sobre amamentação, sono, puerpério e saúde emocional. | HTML5, CSS3 |


## 💼 Experiência Profissional em Destaque

```
🏢 Analista de Suporte Pleno
   ├── Gestão de identidades: Azure AD, Entra ID, Microsoft 365
   ├── MDM: Microsoft Intune + Autopilot (deployment e conformidade)
   ├── Automação de provisionamento via SCCM
   ├── Suporte avançado MacBook (BR/LATAM)
   ├── Redes: TCP/IP, VLANs, DHCP, DNS, VPN IPSec/SSL
   ├── Análise de tráfego: Wireshark
   ├── Compliance farmacêutico (BPF/GxP)
   └── Gestão de SLA com base em práticas ITIL
```

---

<div align="center">

### 💬 Vamos nos conectar!

*"A tecnologia move o mundo — e eu movo a tecnologia."*

[![LinkedIn](https://img.shields.io/badge/Me_encontre_no_LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/guilherme-gonçalves-b60597241/)
[![Gmail](https://img.shields.io/badge/Envie_um_email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:guihsg31@gmail.com)

![Visitor Count](https://komarev.com/ghpvc/?username=gui995&color=0078D4&style=for-the-badge&label=Visitas+ao+Perfil)

</div>
