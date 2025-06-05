from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def fazer_login(browser, usuario, senha):
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.NAME, "username"))
    )
    campo_username = browser.find_element(By.NAME, "username")
    campo_username.clear()
    campo_username.send_keys(usuario)

    campo_password = browser.find_element(By.NAME, "password")
    campo_password.clear()
    campo_password.send_keys(senha)
    
    browser.find_element(By.TAG_NAME, "button").click()

def cadastrar_funcionario(browser, usuario, senha, nome, meio, sobrenome, matricula):
    fazer_login(browser, usuario, senha)
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "PIM"))
    ).click()
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Add Employee"))
    ).click()
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.NAME, "firstName"))
    ).send_keys(nome)
    browser.find_element(By.NAME, "middleName").send_keys(meio)
    browser.find_element(By.NAME, "lastName").send_keys(sobrenome)
    id = browser.find_elements(By.CLASS_NAME, "oxd-input")[-1]
    id.send_keys(Keys.CONTROL, "a")
    id.send_keys(matricula)
    browser.find_elements(By.TAG_NAME, "button")[-1].click()