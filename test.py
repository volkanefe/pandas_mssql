from conn import *

sorgu = '''

SELECT sto_kod, sto_isim, bar_kodu, sfiyat_fiyati FROM STOKLAR 
INNER JOIN BARKOD_TANIMLARI ON sto_kod = bar_stokkodu
INNER JOIN STOK_SATIS_FIYAT_LISTELERI ON sto_kod = sfiyat_stokkod
WHERE sto_isim LIKE 'ARIEL%'

'''

sorgu1 = '''

SELECT sto_kod, sto_isim, bar_kodu, sfiyat_fiyati FROM STOKLAR 
INNER JOIN BARKOD_TANIMLARI ON sto_kod = bar_stokkodu
INNER JOIN STOK_SATIS_FIYAT_LISTELERI ON sto_kod = sfiyat_stokkod
WHERE sto_isim LIKE 'ARIEL%' and sfiyat_fiyati < 100

'''

with engine.connect() as connection:
    result = connection.execute(text(sorgu))
    for row in result:
        print(row)

