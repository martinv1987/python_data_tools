import pandas
import sys

try:
  archivo = sys.argv[1]
except:
  print("No ha asignado un ID SAP")
  sys. exit()  

print("Procesando id: " + archivo)

df1 = pandas.read_csv(r'csv/' + archivo + '.csv', sep=';')
datafinal = ''
counter = 0

f = open('xml/' + archivo + '.XML', "w")

cabecera = '<headerFooter>\n'
pie = '</headerFooter> \n'

data = """\n<Registro>
        <num_id>{numid}</num_id>
        
        </Registro>\n"""


for i in df1.index:
  counter = counter + 1

  data_p = data

  numero_tx = str(df1['numid'][i])
  numero_tx = numero_tx.replace(".","")
        
  data_p = data_p.replace("{numid}", str(numero_tx))
  
  datafinal = datafinal + data_p

"""datafinal = datafinal.replace('>nan<','><')"""
documento = cabecera + datafinal + pie
f.write(documento)
f.close()

print("Registros procesados: " +  str(counter))
