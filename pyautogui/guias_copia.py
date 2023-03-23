#segunda parte de guias, copia e cola

import pyautogui, time

pyautogui.alert("Bote na parte da guia para ele colar diretamente da pagina e fechar todas as abas.")
time.sleep(3)

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

#data de autorização
pyautogui.tripleClick(808,472)
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
pyautogui.tripleClick(548,541)
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')
pyautogui.click(1033,337)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('alt', 'tab')

# mover a pagina de posição
pyautogui.click(1355, 700, clicks=12, interval=0.10) 

#carteirinha
pyautogui.doubleClick(320,159)
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')
pyautogui.click(286,417)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('alt', 'tab')


#nome
pyautogui.tripleClick(334,227)
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')
pyautogui.click(281,448)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('alt', 'tab')

#codigo
pyautogui.tripleClick(286,380)
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')
pyautogui.click(286,529)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('alt', 'tab')

#codigo
pyautogui.tripleClick(524,381)
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')
pyautogui.click(523,527)
pyautogui.hotkey('ctrl', 'v')

#conselho, digitação
pyautogui.click(714,569)
pyautogui.write('6022')

#UF
pyautogui.click(838,567)
pyautogui.write('R')
pyautogui.click(838,567)
pyautogui.hotkey('alt', 'tab')

#indicação clinica
pyautogui.doubleClick(303,698)
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')
pyautogui.click(618,665)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('alt', 'tab')

#CNES
pyautogui.doubleClick(905,367)
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')

# mover a pagina de posição
pyautogui.click(1355, 700, clicks=6, interval=0.10) 

pyautogui.click(627,551)
pyautogui.hotkey('ctrl', 'v')

#atendimento
pyautogui.click(307,626)
pyautogui.write('TT')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.write('9')
pyautogui.click(838,567)
pyautogui.hotkey('tab')

#data/hora atendimento
pyautogui.click(744,122)
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(371,443)
pyautogui.hotkey('ctrl', 'v')
pyautogui.write('1000000')

#procedimentos
pyautogui.click(417,376)
pyautogui.click(704,530)
time.sleep(2)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)


# mover a pagina de posição
pyautogui.click(1355, 700, clicks=5, interval=0.10) 

pyautogui.doubleClick(357,556)
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')

#dentro de procedimentos
pyautogui.click(88,163)
pyautogui.hotkey('ctrl', 'v')
pyautogui.click(1241,160) #buscar
time.sleep(1)
pyautogui.click(1233,242) #setinha verde ok 

pyautogui.click(1022,571) #clicar valor 
pyautogui.write('2640') #lembrar que esse valor é do intercambio

time.sleep(0.5)

#data
pyautogui.doubleClick(751,186)
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(281,536)
pyautogui.hotkey('ctrl', 'v')


pyautogui.click(1272,607) #adicionar

time.sleep(1)

#clicar no boneco merda 
pyautogui.click(1277,651)


#dentro do boneco merda 
pyautogui.click(650,209)
pyautogui.hotkey('alt', 'tab')
pyautogui.doubleClick(318,279)
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')
pyautogui.click(620,211)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')

#verificar qual é o nome
time.sleep(10)

pyautogui.click(1235,327)





