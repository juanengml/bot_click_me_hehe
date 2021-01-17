from time import sleep
from random import choice 
from pyautogui import hotkey, typewrite
from console_logging.console import Console
from faker import Faker
console = Console()
fake = Faker()


site = "http://www.brasil-sufocado.bonde.org/"

ddd = ['11', '12', '13', '14', '15', '16', '17', '18', '19', '21', '22', '24', '27', '28', '31', '32', '33', '34', '35', '37', '38', '41', '42', '43', '44', '45', '46', '47', '48', '49', '51', '53', '54', '55', '61', '62', '63', '64', '65', '66', '67', '68', '69', '71', '73', '74', '75', '77', '79', '81', '82', '83', '84', '85', '86', '87', '88', '89', '91', '92', '93', '94', '95', '96', '97', '98', '99']
provider = ["gmail.com","outlook.com","yahoo.com","de.com","localweb.com","live.com"]

def openfirefox():
  console.log("ABRINDO FIREFOX")
  comandos = ['ctrl','alt','t']
  app = " firefox "
  hotkey('ctrl','alt','t') # open terminal
  console.log("ABRINDO TERMINAL")
  sleep(1)        # wait terminal opened
  typewrite(app+site+" ;exit",interval=0.04) 
  console.log("open FIREFOX WITH SITE")
  hotkey("enter")  

def dados():
   
   nome_completo_lista = fake.name().split()   
   nome = nome_completo_lista[0]
   sobrenome = nome_completo_lista[1]
   email = nome.lower()+"_"+sobrenome.lower()+"@"+choice(provider)
   number_ = "{}{}{}{} {}{}{}{}".format(choice(range(9)),choice(range(9)),choice(range(9)),choice(range(9)),
                                                       choice(range(9)),choice(range(9)),choice(range(9)),choice(range(9)))
   numero = "("+choice(ddd)+") 9"+number_
   return [email,nome,sobrenome, numero]

def spaces(numbers):
# 3 tab tab tab = email 4 tab tab tab tab = nome 5 tab tab tab tab tab = 13 Brazil  6 tab tab tab tab tab tab = CEP 7 tab tab tab tab tab tab tab = CIDADE 8 tab tab tab tab tab tab tab tab = Pq isso ser importante 9 tab tab tab tab tab tab tab tab tab = assine
  for p in range(numbers):
     hotkey("tab")
     console.info(str(p)+" TABS")
     sleep(0.1)

def write(text):
     console.info(text)
     typewrite(text,interval=0.02)


def main():
 openfirefox()
 [sleep(1) for p in range(10)]
 spaces(5)
 for p in  range(100):
  console.log(" REQUEST - "+str(p))  
  email,nome,sobrenome, numero = dados()
  write(email)
  hotkey("tab")
  write(nome)
  hotkey("tab")
  write(sobrenome)
  hotkey("tab")
  hotkey("tab")
  hotkey("enter")
  sleep(15)
  hotkey('ctrl','w')
  openfirefox()
  [sleep(1) for p in range(10)]
  spaces(5)

if __name__ == "__main__":
    main()

  
  



