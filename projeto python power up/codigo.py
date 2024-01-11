# passo a passo do projeto

# Passo 1 - Entrar no sistema da empresa
    ##https://dlp.hashtagtreinamentos.com/python/intensivao/login

#pyautogui - RPA - automação bot
import pyautogui
import time

# clicar -> pyautogui.click
# escrever -> pyautogui.white
# apertar uma tecla -> pyautogui.press
# apertar -> pyautogui.hotkey ("ctrl", "C") da um control
# scroll (rolar a pagina) -> pyautogui.scroll

pyautogui.PAUSE = 1
# apertar a tecla do windows
pyautogui.press("win")
# digita o nome do programa Minhasenha123 (chrome)
pyautogui.write("chrome")
# aperta enter
pyautogui.press("enter")
time.sleep(3)
# digitar o link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

# apertar enter
pyautogui.press("enter")

# espera 5 segundos
time.sleep(2)

# Passo 2 - Fazer login
pyautogui.click(x=719, y=508)

# Digitar o email
pyautogui.write("juanfanpoli@gmail.com")  
# passar para o campo de senha
pyautogui.press("tab")

# digitar a senha
pyautogui.write("Minhasenha123")
#clicar em logar
pyautogui.click(x=935, y=704)
#time.sleep(1)


# Passo 3 - Importar a base de dados
# pip install pandas numpy openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

#cadastrar os produtos e cada linha da tabela
for linha in tabela.index:

    # Passo 4 - Cadastrar um produto
    pyautogui.click(x=694, y=364)
    # codigo 
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")
    # marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # preco
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")
    # enviar o produto
    pyautogui.press("enter")
    pyautogui.scroll(5000)




# Passo 5 - Repetir isso até acabar a base de dados