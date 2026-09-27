import random
import datetime
geneSet="abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ!@#$%^&*(),.-_=+1234567890 "
password = "#cALNs!&6Kw%nd9"

def generar_padre(longitud):
  genes=[]
  while len(genes)<longitud:
    tamanhoMuestral=min(longitud-len(genes), len(geneSet))
    genes.extend(random.sample(geneSet, tamanhoMuestral))
  return''.join(genes)

def obtener_fitness(guess):
  return sum(1 for expected, actual in zip(password, guess) if expected==actual)
  
def mutar(padre):
  indice=random.randrange(0,len(padre))
  genes_Ninho=list(padre)
  nuevoGen, alterno=random.sample(geneSet,2)
  genes_Ninho[indice]=alterno if nuevoGen==genes_Ninho[indice] else nuevoGen
  return ''.join(genes_Ninho)

def mostrar(conjetura):
  diferencia=(datetime.datetime.now()-horaInicio).total_seconds()
  aptitud=obtener_fitness(conjetura)
  print("{}\t{}\t{}".format(conjetura,aptitud,diferencia))
  
random.seed()
horaInicio=datetime.datetime.now()
mejorPadre=generar_padre(len(password))
mejorAptitud=obtener_fitness(mejorPadre)
mostrar(mejorPadre)

while True:
  ninho=mutar(mejorPadre)
  ninhoAptitud=obtener_fitness(ninho)
  if mejorAptitud>=ninhoAptitud:
    continue
  mostrar(ninho)
  if ninhoAptitud>=len(mejorPadre):
    break
  mejorAptitud=ninhoAptitud
  mejorPadre=ninho
