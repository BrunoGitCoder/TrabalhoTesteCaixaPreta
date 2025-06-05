from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from funcoes import cadastrar_funcionario

def test_registro_valido(browser, conta_valida, funcionario_valido):
    cadastrar_funcionario(browser, conta_valida["login"], conta_valida["senha"], funcionario_valido["nome"], funcionario_valido["meio"], funcionario_valido["sobrenome"], funcionario_valido["matricula"])

    WebDriverWait(browser, 5).until(
        EC.url_contains("viewPersonalDetails")
    )
    assert "viewpersonaldetails" in browser.current_url.lower()

def test_registro_invalido_sem_sobrenome(browser, conta_valida, funcionario_sem_sobrenome):
    cadastrar_funcionario(browser, conta_valida["login"], conta_valida["senha"], funcionario_sem_sobrenome["nome"], funcionario_sem_sobrenome["meio"], funcionario_sem_sobrenome["sobrenome"], funcionario_sem_sobrenome["matricula"])

    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "oxd-input-field-error-message"))
    )
    mensagem_erro = browser.find_element(By.CLASS_NAME, "oxd-input-field-error-message").text
    assert "required" in mensagem_erro.lower()

def test_registro_invalido_matricula_repetida(browser, conta_valida, funcionario_matricula_repetida):
    cadastrar_funcionario(browser, conta_valida["login"], conta_valida["senha"], funcionario_matricula_repetida["nome"], funcionario_matricula_repetida["meio"], funcionario_matricula_repetida["sobrenome"], funcionario_matricula_repetida["matricula"])

    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "oxd-input-field-error-message"))
        )
    mensagem_erro = browser.find_element(By.CLASS_NAME, "oxd-input-field-error-message").text
    assert "exists" in mensagem_erro.lower()