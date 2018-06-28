from pyautogui import hotkey, typewrite
from time import sleep

site = "https://secure.avaaz.org/po/petition/MEC_PIBID_sem_cortes_e_sem_interrupcao/?zisyymb"
file = open("emails").read().split('\n')
n = len(file)-1
a = 6856
p = range(74900001,74906857)
localidade = "Aparecida de Goiania"

def openfirefox():
  comandos = ['ctrl','alt','t']
  print comandos
  app = "firefox "
  print app
  hotkey('ctrl','alt','t') # open terminal
  print "open terminal"
  sleep(0.5)        # wait terminal opened
  typewrite(app+site,interval=0.01) 
  print "open firefox with site "
  hotkey("enter")  

def dados(item):
   nome = file[item].split('@')[0]
   email = file[item]
   localidade = "Aparecida"
   return [email,nome,localidade]

def spaces(numbers):
# 3 tab tab tab = email 4 tab tab tab tab = nome 5 tab tab tab tab tab = 13 Brazil  6 tab tab tab tab tab tab = CEP 7 tab tab tab tab tab tab tab = CIDADE 8 tab tab tab tab tab tab tab tab = Pq isso ser importante 9 tab tab tab tab tab tab tab tab tab = assine
  for p in range(numbers):
     hotkey("tab")
     print p,'tab'
     sleep(0.1)

def write(text):
     typewrite(text,interval=0.02)


def main():
 for p in  range(a):
  print "VOTO: ",p
  openfirefox()
  sleep(5)
  spaces(8)
  email,name,localidade = dados(p)
  write(email)
  spaces(4)
  hotkey('space')
  spaces(27)
  hotkey("enter")
  sleep(10) 
  for p in range(6):
   hotkey("ctrl","w")
   sleep(0.5)
  for p in range(4):
   hotkey("ctrl","d")   
  


while 1:
   main()


