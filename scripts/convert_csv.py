import os
import sys
import pandas as pd
import re
from unidecode import unidecode

def convert_csv():
  upload_files = os.listdir('upload')
  for file in upload_files:
    read_file = pd.read_excel (f'upload/{file}')
    columns = read_file.columns
    new_columns = []
    for column in columns:
      new_columns.append(snake_small_case(column))
    csv_name = file.split('.xlsx')[0]
    #import ipdb; ipdb.set_trace(context=10)
    read_file.columns=new_columns
    read_file.to_csv (f'data/{csv_name}.csv', index = None, header=True, sep = ';', decimal = ',', encoding = 'utf-8-sig', na_rep = "")

def snake_small_case(column):
  column_lower = column.lower()
  column_unidecode = unidecode(column_lower)
  column_alphanumeric = re.sub('[^A-Za-z0-9]+', ' ', column_unidecode)
  column_split = column_alphanumeric.split(' ')
  column_empty = [x for x in column_split if x != '']
  column = '_'.join(column_empty)
  return column

if __name__ == '__main__':
  convert_csv()
#  feminicidio = pd.read_excel('upload/.xlsx')
 # feminicidio.rename(columns = {'TENTADO/CONSUMADO':'TENTADO_CONSUMADO','DATA DO FATO':'DATA_FATO','MÊS':'MES','ANO DO FATO':'ANO_FATO','MUNICÍPIO DO FATO':'MUNICIPIO_FATO','QTD DE VÍTIMAS':'QTD_VITIMAS'}, inplace=True)
 # feminicidio = pd.read_excel('http://www.seguranca.mg.gov.br/images/2023/Janeiro/Modelo_Sesp_Feminicdio.Jan20_Dez22.xlsx', sheet_name='Dados', names=feminicidio.columns, header=0)
 # feminicidio.to_csv (f'data/feminicidio-2020-2022.csv', index = None, header=True, sep = ';', decimal = ',', encoding = 'utf-8-sig', na_rep = "")
 # violencia = pd.read_excel('http://www.seguranca.mg.gov.br/images/2023/Janeiro/Modelo_Sesp_Violencia%20Domestica%20e%20Familiar%20contra%20a%20Mulher.Jan20_Dez22.xlsx', sheet_name='Dados')
 # violencia.rename(columns = {'MUNICÍPIO-CÓD':'MUNICIPIO_COD','MUNICÍPIO':'MUNICIPIO','DATA FATO':'DATA_FATO','MÊS':'MES','QUANT. VÍTIMAS VIOL.DOMÉSTICA':'QUANT_VITIMAS_VIOL.DOMESTICA'}, inplace=True)
 # violencia = pd.read_excel('http://www.seguranca.mg.gov.br/images/2023/Janeiro/Modelo_Sesp_Violencia%20Domestica%20e%20Familiar%20contra%20a%20Mulher.Jan20_Dez22.xlsx', sheet_name='Dados', names=violencia.columns, header=0)
 # violencia.to_csv (f'data/violencia-contra-mulher-2020-2022.csv', index = None, header=True, sep = ';', decimal = ',', encoding = 'utf-8-sig', na_rep = "")