# Google

## Instalar o gerenciador de ambiente virtual

```bash
apt install python3.10-venv
```

## Criar o ambiente virtual

```bash
python3 -m venv ./venv && source venv/bin/activate
```

## Instalar PIP

```bash
sudo apt install python3-pip
```

## Verificar a versão

```bash
pip3 --version

pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)
```

## Instalando o Selenium

```bash
pip install selenium
```

## Instalando o webdriver-manager 

```bash
pip install webdriver-manager 
```

## Instalando o google-chrome

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
sudo apt install ./google-chrome-stable_current_amd64.deb && \
google-chrome --version
```

## Verifique a instalação:

```bash
google-chrome --version

Google Chrome 129.0.6668.58
```

## Instalando o chromedriver

Baixe o pacote `.deb` do Google Chrome:

```bash
wget https://storage.googleapis.com/chrome-for-testing-public/129.0.6668.58/linux64/chromedriver-linux64.zip
```

Descompacte

```bash
unzip chromedriver-linux64.zip
```

Permissão para execução

```bash
chmod +x chromedriver
```

Copiar o chromedriver para o path

```bash
sudo cp chromedriver /usr/bin/
```

Se o local do seu driver ainda não estiver em um diretório listado, você pode adicionar um novo diretório ao PATH:

```bash
echo 'export PATH=$PATH:/usr/bin/chromedriver' >> ~/.zshenv
```

Atualizar o MYOHZSH

```bash
source ~/.zshenv
```

Você pode testar se ele foi adicionado corretamente verificando a versão do driver:

```bash
chromedriver --version

ChromeDriver 129.0.6668.58 (81a06fb873a9b386848719cf9f93e59579fb5d4b-refs/branch-heads/6668@{#1318})
```

OBS.: Tanto o `google-chrome` quanto o `chromedriver` precisam estar na mesma versão !!!

## Verificando as bibliotecas que foram instaladas

```bash
pip list

Package             Version
------------------- -------------

```

Esse passo é importante, por causa das versões.

Podemos salvar essas informações em um arquivo

```bash
pip freeze > requirements.txt
```

Próximos passos... [Exemplo de código](../docs/codigo-google.md)