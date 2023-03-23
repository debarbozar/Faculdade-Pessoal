#segunda parte de guias, copia e cola

import pyautogui, time

pyautogui.alert("Bote na parte da guia para ele colar diretamente da pagina e fechar todas as abas.")
time.sleep(5)

#guia principal
pyautogui.doubleClick(926,419)
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')
pyautogui.click(571,336)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('alt', 'tab')

#data de autorização
pyautogui.leftClick(808,472)
pyautogui.keyDown('shift')
pyautogui.leftClick(872,475)
pyautogui.keyUp('shift')
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')
pyautogui.click(727,344)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('alt', 'tab')

#senha
pyautogui.doubleClick(309,543)
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')
pyautogui.click(868,341)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('alt', 'tab')

#validade senha 
pyautogui.leftClick(548,541)
pyautogui.keyDown('shift')
pyautogui.leftClick(613,541)
pyautogui.keyUp('shift')
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')
pyautogui.click(1033,337)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('alt', 'tab')

#carteirinha
pyautogui.doubleClick(321,641)
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')
pyautogui.click(282,4144)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('alt', 'tab')


# mover a pagina de posição

pyautogui.click(clicks=12)  # double-click the left mouse button



#nome
pyautogui.leftClick(281,507)
pyautogui.keyDown('shift')
pyautogui.leftClick(457,505)
pyautogui.keyUp('shift')
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')
pyautogui.click(412,458)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('alt', 'tab')