import pandas as pd

url = "https://raw.githubusercontent.com/Bennunes/magazine-luiza/master/Base-teste-2010_dados.json"
df_2010 = pd.read_json(url)
#df_2010 = df_2010.query('algoritmo_recomendacao != k_2 ')
df_2010

url = "https://raw.githubusercontent.com/Bennunes/magazine-luiza/master/Base-teste-2009_dados.csv"
df_2009 = pd.read_csv(url)
df_2009 = df_2009.drop(['Unnamed: 10','Unnamed: 11','Unnamed: 12','Unnamed: 13','Unnamed: 14','Unnamed: 15','Unnamed: 16','Unnamed: 17','Unnamed: 18','Unnamed: 19','Unnamed: 20','dia'], axis=1)
#df_2009 = df_2009.query("algoritmo_recomendacao=='k_1' & fonte_trafego=='fonte_1'")

df_2009


frames = [df_2009, df_2010]

result = pd.concat(frames, sort=False, ignore_index=True)

result.to_csv(r'C:\Users\PC Gamer\Documents\exercicio-magazina-luiza\data-base-2010-2009.csv', index=None)
