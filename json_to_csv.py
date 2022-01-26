import pandas as pd

df = pd.read_json ('trf/trf/spiders/scrap.json')
df.to_csv (r'C:/Users/{}/Desktop/{}.csv', index = None) #nesta parte você coloca o path onde deseja salvar o .csv convertido de json
