# Exemplo de código para o firefox

## Primeiro Exemplo

```bash 
from selenium import webdriver
 
driver = webdriver.Firefox()
driver.get("https://google.com")
```

## Segundo Exemplo

```bash 
import unittest
from selenium import webdriver

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_page_title(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)

```