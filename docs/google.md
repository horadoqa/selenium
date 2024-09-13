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

## Instalando o Google-Chrome

Baixe o pacote `.deb` do Google Chrome:

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```

Instale o pacote `.deb`:

```bash
sudo apt install ./google-chrome-stable_current_amd64.deb
```

Verifique a instalação:

Após a instalação, você pode verificar se o Google Chrome está disponível executando:

```bash
google-chrome --version

Google Chrome 126.0.6478.126
```

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