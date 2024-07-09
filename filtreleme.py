import pandas as pd
from conn import *


pd.options.display.max_columns = None
pd.options.display.colheader_justify = 'left'
pd.options.display.width = 0


sorgu = '''
    SELECT 
    sto_kod, 
    sto_isim, 
    bar_kodu, 
    sfiyat_fiyati,
    [1.Depo],
    [2.Depo],
    [3.Depo],
    [4.Depo],
    [5.Depo],
    [6.Depo],
    [TOPLAM MIKTAR]
FROM 
    STOKLAR 
    INNER JOIN BARKOD_TANIMLARI ON sto_kod = bar_stokkodu
    INNER JOIN STOK_SATIS_FIYAT_LISTELERI ON sto_kod = sfiyat_stokkod
    INNER JOIN STOKLAR_CHOOSE_3 ON sto_kod = msg_S_0078
WHERE
    sto_isim LIKE 'ARIEL%'


'''

with engine.connect() as connection:
    df = pd.read_sql_query(sorgu, connection)


result = df[["sto_isim", "bar_kodu"]]
result = df
result = df.columns
result = df.head()
result = df.head(10)
result = df.tail()
result = df.tail(10)
result = df.sto_isim.head()
result = df.bar_kodu.head(10)
result = df[['sto_isim', 'bar_kodu']].head()
result = df[['sto_isim', 'bar_kodu']].head(10)
result = df[['sto_isim', 'bar_kodu']].tail()
result = df[['sto_isim', 'bar_kodu']].tail(10)
result = df[5:15][['sto_isim', 'bar_kodu', 'sfiyat_fiyati']].head()
result = df[5:15][['sto_isim', 'bar_kodu',
                   'sfiyat_fiyati', 'TOPLAM MIKTAR']].tail()
result = df[df['TOPLAM MIKTAR'] == 0]
result = df[['sto_isim', 'bar_kodu', 'TOPLAM MIKTAR']
            ][df['TOPLAM MIKTAR'] > 10]
result = df[['sto_isim', 'bar_kodu', 'sfiyat_fiyati', 'TOPLAM MIKTAR']][(
    df['sfiyat_fiyati'] > 50) & (df['TOPLAM MIKTAR'] > 50)]

print(result)

# print(df.columns)
