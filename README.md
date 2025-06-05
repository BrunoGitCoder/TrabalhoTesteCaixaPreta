# 🧪 Teste de Caixa Preta - OrangeHRM (2º Bimestre)

Este repositório contém os testes automatizados desenvolvidos como parte do trabalho de Teste de Caixa Preta solicitado pelo professor Valdinei Saugo, referente ao 2º bimestre.

---

## 📌 Descrição

Aplicamos **testes de caixa preta** no sistema **[OrangeHRM](https://opensource-demo.orangehrmlive.com/)** (versão demo), utilizando a biblioteca **Selenium** com **Pytest**, para validar funcionalidades e aspectos não funcionais como usabilidade e segurança.

Os testes foram feitos **sem acesso ao código-fonte**, simulando a experiência de um usuário comum.

---

## ✅ Testes Implementados

### Funcionais:
- Login válido
- Login inválido
- Cadastro de funcionário com dados válidos
- Cadastro com campos obrigatórios ausentes
- Cadastro com matrícula duplicada

### Não Funcionais:
- Verificação do campo de senha (segurança)
- Redirecionamento ao login se não estiver autenticado (segurança)
- Logout funcionando corretamente
- Usabilidade na exclusão de funcionários (confirmação visual, cancelamento, busca)

---

## 🛠️ Tecnologias utilizadas

- Python 3.10+
- Selenium
- Pytest
- WebDriver do Chrome (Chromedriver)
