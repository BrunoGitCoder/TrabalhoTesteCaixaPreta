import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Edge()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()

@pytest.fixture
def browser_pagina_interna():
    driver = webdriver.Edge()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    yield driver
    driver.quit()

@pytest.fixture
def conta_valida():
    return {"login": "Admin", "senha": "admin123"}

@pytest.fixture
def conta_invalida():
    return {"login": "Admin", "senha": "123"}

@pytest.fixture
def funcionario_valido():
    return {"nome": "Paulo", "meio": "Henrique", "sobrenome": "de Castro", "matricula": "Uni348"}

@pytest.fixture
def funcionario_sem_sobrenome():
    return {"nome": "Anna", "meio": "", "sobrenome": "", "matricula": "Uni985"}

@pytest.fixture
def funcionario_matricula_repetida():
    return {"nome": "Igor", "meio": "Gomes", "sobrenome": "de Andrade", "matricula": "Uni348"}
