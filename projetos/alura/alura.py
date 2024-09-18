from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    driver.get("https://www.alura.com.br")

    elemento = driver.find_element(By.XPATH, '/html/body/main/section[1]/div/div[2]/nav/div/div[4]/div/a')
    time.sleep(5)
    elemento.click()
    time.sleep(5)

    # Verifica se os resultados estão presentes
    results = driver.find_elements(By.CSS_SELECTOR, "h1")
    assert len(results) > 0, "Nenhum resultado encontrado."

    # Exibe o título da primeira página de resultados
    print("Título da segunda página : ", results[0].text)

finally:
    # Fechar o navegador
    driver.quit()