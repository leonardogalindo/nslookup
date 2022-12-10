# Ambiente Virtual 

## virtualenv - uma ferramenta muito útil para ajudar a manter o ambiente de trabalho no nosso computador organizado.
O *virtualenv* isolará seu código Python em um ambiente organizado por projetos. Isso significa que as alterações que você fizer em um projeto não afetarão os outros projetos que você estiver desenvolvendo ao mesmo tempo.

Tudo o que você precisa fazer é encontrar o diretório/criar em que você quer criar o virtualenv; seu diretório Home, por exemplo. No Windows, pode aparecer como C:\Users\Name (onde Nome é seu usuário de login).

## Virtual environment: Linux and OS X - instalação
`python3 -m venv myvenv`

## Virtual environment: Windows
Para criar um novo virtualenv, você deve abrir o terminal e executar `python -m venv myvenv`. Deve ficar assim:
*C:\Users\Name\projeto> python -m venv myvenv*

## Obs:
myvenv é o nome do seu virtualenv. Você pode usar qualquer outro nome, mas use sempre letras minúsculas e não use espaços entre as palavras. Também é uma boa ideia manter o nome curto pois você vai escrevê-lo muitas vezes!

*Observação: Em algumas versões do Debian/Ubuntu, você pode receber o seguinte erro:*
**The virtual environment was not created successfully because ensurepip is not available.  On Debian/Ubuntu systems, you need to install the python3-venv package using the following command.**
apt install python3-venv
You may need to use sudo with that command.  After installing the python3-venv package, recreate your virtual environment.

Caso você receba esse erro, siga as instruções acima e instale o pacote python3-venv: 
`sudo apt install python3-venv`

## Trabalhando com o virtualenv - ativando
Linux and OS X - terminal: `source myvenv/bin/activate`  
Windows:
CMD/PowerShell: `myvenv\Scripts\activate`  
Visual Studio Code: `. myvenv\Scripts\activate.ps1`  

Lembre-se de substituir myvenv pelo nome que você escolheu para o virtualenv!

*Observação*: às vezes source pode não estar disponível. Nesses casos, tente fazer isso: . myvenv/bin/activate

## Desativando o ambiente virtual
`deactivate`

## PIP - instalação - utilizar comando com ambient virtual ativado
`python -m pip install --upgrade pip`

#### Ambiente Virtual - end 