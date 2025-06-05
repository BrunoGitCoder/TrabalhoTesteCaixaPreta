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

## ▶️ Como executar os testes

Para executar os testes automatizados deste projeto, primeiro clone este repositório com `git clone https://github.com/seu-usuario/seu-repositorio.git` e entre na pasta com `cd seu-repositorio`. Recomenda-se criar um ambiente virtual com `python -m venv venv` e ativá-lo com `venv\Scripts\activate` no Windows ou `source venv/bin/activate` no Linux/macOS. Em seguida, instale as dependências com `pip install -r requirements.txt`. Com tudo pronto, execute os testes com `pytest`. Para rodar um teste específico, utilize `pytest nome_do_arquivo.py`, como por exemplo `pytest test_login.py`.

