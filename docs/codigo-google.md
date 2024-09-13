# Projeto 

Criar um arquivo: main.py

```bash
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service)

try:
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.pinterest.com/ideas/")

    # Esperar para ver o resultado
    time.sleep(10)

finally:
    # Fechar o navegador
    driver.quit()
```

## Executando

```bash
python main.py
```

O Browser do Google irá abrir com o conteúdo da pesquisa
