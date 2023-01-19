import pyautogui
import pyperclip
import time
import pandas

pyautogui.PAUSE = 1

#baixar base de dados
pyautogui.hotkey("win")
pyautogui.write("opera")
pyautogui.hotkey("enter")
time.sleep(5)
pyperclip.copy("https://drive.google.com/drive/u/0/folders/1bqxRDqJGhfVYWUav4vJ31pTV_jxjFPLL")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")
time.sleep(5)

pyautogui.click(x=692, y=433, clicks=2)
pyautogui.click(x=770, y=534)
pyautogui.click(x=2211, y=245)
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
pyautogui.write("king")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.write("Teste de automacao")
pyautogui.hotkey("tab")

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
pyautogui.write("Expl")
pyautogui.hotkey("enter")
pyperclip.copy(r"C:\Users\lucas\Downloads")
pyautogui.click(x=1476, y=233)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")
pyautogui.hotkey("ctrl", "f")
pyautogui.write("vendas")
pyautogui.hotkey("enter")
pyautogui.click(x=1941, y=541)
pyautogui.hotkey("v")
pyautogui.hotkey("del")
