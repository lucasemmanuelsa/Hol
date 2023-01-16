import pyautogui
import pyperclip
import time
import pandas


#baixar base de dados
pyautogui.hotkey("win")
time.sleep(2)
pyautogui.write("opera")
pyautogui.hotkey("enter")
time.sleep(5)
pyperclip.copy("https://drive.google.com/drive/u/0/folders/1bqxRDqJGhfVYWUav4vJ31pTV_jxjFPLL")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")
time.sleep(5)

pyautogui.click(x=692, y=433, clicks=2)
time.sleep(2)
pyautogui.click(x=770, y=534)
time.sleep(2)
pyautogui.click(x=2211, y=245)
time.sleep(2)
pyautogui.click(x=1798, y=957)

time.sleep(8)


#read excel data
tabela = pandas.read_excel(r"C:\Users\lucas\Downloads\Vendas - Dez.xlsx")

print(tabela)

quantidade = tabela["Quantidade"].sum()
totalValue = tabela["Valor Final"].sum()

#send email
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://mail.google.com/mail/u/3/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")
time.sleep(4)
pyautogui.click(x=119, y=197)
time.sleep(2)
pyautogui.write("king")
time.sleep(2)
pyautogui.hotkey("tab")
time.sleep(1)
pyautogui.hotkey("tab")
pyautogui.write("Teste de automacao")
pyautogui.hotkey("tab")
time.sleep(2)
texto = f"""
Olá, boa tarde!
O faturamento de ontem foi de R${totalValue},00
A quantidade de itens vendidos: {quantidade}

Abs
Lucas"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl", "enter")

time.sleep(4)

#delete archive
pyautogui.hotkey("win")
time.sleep(3)
pyautogui.write("Expl")
time.sleep(2)
pyautogui.hotkey("enter")
time.sleep(3)
pyperclip.copy(r"C:\Users\lucas\Downloads")
time.sleep(2)
pyautogui.click(x=1476, y=233)
time.sleep(2)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.hotkey("enter")
time.sleep(2)
pyautogui.hotkey("ctrl", "f")
time.sleep(2)
pyautogui.write("vendas")
time.sleep(2)
pyautogui.hotkey("enter")
time.sleep(2)
pyautogui.click(x=1941, y=541)
time.sleep(1)
pyautogui.hotkey("v")
pyautogui.hotkey("del")
