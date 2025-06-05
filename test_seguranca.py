from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from funcoes import fazer_login

def test_verifica_campo_senha(browser):
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.NAME, "password"))
    )
    campo_password = browser.find_element(By.NAME, "password")
    tipo = campo_password.get_attribute("type")
    assert tipo == "password"

def test_redireciona_para_login_se_nao_logado(browser_pagina_interna):
    WebDriverWait(browser_pagina_interna, 5).until(
        EC.visibility_of_element_located((By.NAME, "username"))
    )
    assert "login" in browser_pagina_interna.current_url.lower()

def test_logout(browser, conta_valida):
    fazer_login(browser, conta_valida["login"], conta_valida["senha"])
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "oxd-userdropdown-tab"))
    ).click()
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))
    ).click()
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    WebDriverWait(browser, 5).until(EC.url_contains("login"))
    assert "login" in browser.current_url.lower()