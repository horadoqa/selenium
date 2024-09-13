from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('http://127.0.0.1:5500/projetos/horadoqa/site/index.html')

# Encontre o elemento que deseja clicar
elemento = driver.find_element(By.XPATH, "//*[contains(text(), 'Informações Financeiras')]")
elemento.click
time.sleep(5)

elemento2 = driver.find_element(By.XPATH, "//*[contains(text(), 'Planilha de Resultado')]")
elemento2.click
time.sleep(5)

elemento3 = driver.find_element(By.XPATH, "//*[contains(text(), 'Planilha de Resultados Trimestrais')]")
elemento3.click()
time.sleep(5)

# Feche o navegador
driver.quit()