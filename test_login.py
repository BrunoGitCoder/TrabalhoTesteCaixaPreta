from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from funcoes import fazer_login

def test_login_invalido(browser, conta_invalida):
    fazer_login(browser, conta_invalida["login"], conta_invalida["senha"])

    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "oxd-alert-content-text")))
    mensagem = browser.find_element(By.CLASS_NAME, "oxd-alert-content-text").text
    assert "invalid" in mensagem.lower()

def test_login_valido(browser, conta_valida):
    fazer_login(browser, conta_valida["login"], conta_valida["senha"])

    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "oxd-userdropdown-tab")))
    assert "dashboard" in browser.current_url.lower()