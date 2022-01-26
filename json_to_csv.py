import pandas as pd
df = pd.read_json ('trf/trf/spiders/refeito.json')
df.to_csv (r'C:/Users/Andra/Desktop/jajas.csv', index = None)