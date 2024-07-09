import pandas as pd
from conn import *

sorgu = '''

SELECT sto_kod, sto_isim, bar_kodu, sfiyat_fiyati FROM STOKLAR 
INNER JOIN BARKOD_TANIMLARI ON sto_kod = bar_stokkodu
INNER JOIN STOK_SATIS_FIYAT_LISTELERI ON sto_kod = sfiyat_stokkod
WHERE sto_isim LIKE 'ARIEL%'

'''

with engine.connect() as connection:
    df = pd.read_sql_query(sorgu, connection)

print(df.columns)

sfiyat = df['sfiyat_fiyati']

liste = [row for index, row in df.iterrows() if row['sfiyat_fiyati'] < 100] # list comprehansion kullanılıyor

filtered_df = pd.DataFrame(liste)

print(filtered_df)


