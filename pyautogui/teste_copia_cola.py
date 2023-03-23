#segunda parte de guias, copia e cola

#um campo não dá direito para fazer um CONTROL C + CONTROL V

import pyautogui, time

pyautogui.alert("Bote na parte da guia para ele colar diretamente da pagina e fechar todas as abas.")
time.sleep(3)


# necesario adicionar a extensão do chrome 
# https://chrome.google.com/webstore/detail/absolute-enable-right-cli/jdocbkpgdakpekjlhemmfcncgdjeiika/related?hl=en

#guia principal copia e cola 
pyautogui.doubleClick(932,413) #tem que mudar o valor do seu pixel 
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')
pyautogui.click(1187,284) # tem que mudar o valor do seu pixel 
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('alt', 'tab')

#guia principal
pyautogui.doubleClick(926,419)
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')
pyautogui.click(571,336)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('alt', 'tab')