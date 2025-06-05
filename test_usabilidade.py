from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from funcoes import fazer_login

def test_usabilidade_deletar_funcionario(browser, conta_valida, funcionario_valido):
    fazer_login(browser, conta_valida["login"], conta_valida["senha"])
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "PIM"))
    ).click()
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "oxd-table-filter-title"))
    )
    browser.find_elements(By.TAG_NAME, "input")[2].send_keys(funcionario_valido["matricula"])
    browser.find_element(By.XPATH, "//button[contains(., 'Search')]").click()

    # Verifica se o funcionario esta sendo mostrado na lista"
    assert WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.XPATH, f"//div[text() = '{funcionario_valido["matricula"]}']"))
    )

    botao_delete = browser.find_element(By.CLASS_NAME, "bi-trash")
    botao_delete.click()

    # Verifica se mostra a mensagem de aviso de deletar funcionario
    assert WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(., 'permanently deleted')]"))
    )

    botao_cancelar = browser.find_element(By.XPATH, "//button[contains(., 'Cancel')]")
    botao_cancelar.click()

    # Verifica se o funcionario continua na lista
    assert WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.XPATH, f"//div[text() = '{funcionario_valido["matricula"]}']"))
    )

    botao_delete.click()
    
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//button[contains(., 'Delete')]"))
    ).click()

    # Verifica se foi mostrado a mensagem de exclusao do funcionario
    assert WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.XPATH, f"//div[contains(., 'Success')]"))
    )

    browser.find_element(By.XPATH, "//button[contains(., 'Search')]").click()

    # Verifica se o funcionario foi removido da lista
    assert WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.XPATH, f"//p[contains(., 'No Records')]"))
    )