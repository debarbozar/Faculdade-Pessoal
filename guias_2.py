#segunda parte de guias, copia e cola

import pyautogui, time

pyautogui.alert("Bote na parte da guia para ele colar diretamente da pagina e fechar todas as abas.")
time.sleep(0.5)

#guia principal
pyautogui.doubleClick(1289,550)
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')
pyautogui.click(856,449)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('alt', 'tab')

#data de autorização
pyautogui.tripleClick(1154,637)
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')
pyautogui.click(1060,451)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('alt', 'tab')

#senha
pyautogui.doubleClick(415,730)
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')
pyautogui.click(1266,448)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('alt', 'tab')

#validade senha 
pyautogui.tripleClick(789,727)
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')
pyautogui.click(1505,449)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('alt', 'tab')

# mover a pagina de posição
pyautogui.click(1907,998, clicks=14, interval=0.10) 

#carteirinha
pyautogui.doubleClick(449,161)
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')
pyautogui.click(485,550)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('alt', 'tab')


#nome
pyautogui.tripleClick(500,254)
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')
pyautogui.click(524,598)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('alt', 'tab')

#codigo
pyautogui.tripleClick(419,459)
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')
pyautogui.click(431,703)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('alt', 'tab')

#nome do contratado
pyautogui.tripleClick(738,463)
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')
pyautogui.click(788,705)
pyautogui.hotkey('ctrl', 'v')

#conselho, digitação
pyautogui.click(1048,758)
pyautogui.write('6022')

#UF
pyautogui.click(1202,759)
pyautogui.write('R')
pyautogui.click(1203,762)
pyautogui.hotkey('alt', 'tab')

#indicação clinica
pyautogui.doubleClick(428,904)
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')
pyautogui.click(922,880)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('alt', 'tab')

#CNES
pyautogui.doubleClick(1230,459)
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')

# mover a pagina de posição
pyautogui.click(1909,1017, clicks=5, interval=0.10) 

pyautogui.click(883,798)
pyautogui.hotkey('ctrl', 'v')

#atendimento
pyautogui.click(433,899)
pyautogui.write('TT')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.write('9')
pyautogui.click(756,895)
pyautogui.hotkey('tab')

#data/hora atendimento
pyautogui.click(1046,224)
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(386,654)
pyautogui.hotkey('ctrl', 'v')
pyautogui.write('1000000')

#clicar procedimentos
pyautogui.click(549,573)
pyautogui.click(983,766) #clicar lupa
time.sleep(2)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)


# mover a pagina de posição
#pyautogui.click(1355, 700, clicks=5, interval=0.10) 

pyautogui.doubleClick(483,979)
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')

#dentro de procedimentos
pyautogui.click(67,231)
pyautogui.hotkey('ctrl', 'v')
pyautogui.click(1750,226) #buscar
time.sleep(1)
pyautogui.click(1736,340) #setinha verde ok 

pyautogui.click(1472,821) #clicar valor 
pyautogui.write('2640') #lembrar que esse valor é do intercambio

time.sleep(0.5)

#data
pyautogui.doubleClick(1055,307)
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(361,769)
pyautogui.hotkey('ctrl', 'v')


pyautogui.click(1788,867) #adicionar

time.sleep(1)

#clicar no boneco merda 
pyautogui.click(1797,925)


#dentro do boneco merda 
pyautogui.click(923,294)
pyautogui.hotkey('alt', 'tab')
pyautogui.doubleClick(433,463)
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')
pyautogui.click(935,293)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')

#verificar qual é o nome
time.sleep(8)

pyautogui.click(1755,445)
pyautogui.click(1890,162)