Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd  # Import library
>>> product_quantity = pd.read_excel(r'C:\Users\Aravind S\Downloads\ProductA.xlsx')
>>> google_clicks = pd.read_excel(r'C:\Users\Aravind S\Downloads\ProductA_google_clicks.xlsx')
>>> facebook_impressions = pd.read_excel(r'C:\Users\Aravind S\Downloads\ProductA_fb_impressions.xlsx')
>>> merged_dataset = google_clicks.merge(facebook_impressions, on="Day Index").merge(product_quantity, on="Day Index")
>>> print(merged_dataset.head())
   Day Index  Clicks  Impressions  Quantity
0 2021-12-01     445          620        14
1 2021-12-02     433          890        10
2 2021-12-03     424          851        13
3 2021-12-04     427          881        22
4 2021-12-05     451          678        33
>>> print(merged_dataset.info())
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 212 entries, 0 to 211
Data columns (total 4 columns):
 #   Column       Non-Null Count  Dtype         
---  ------       --------------  -----         
 0   Day Index    212 non-null    datetime64[ns]
 1   Clicks       212 non-null    int64         
 2   Impressions  212 non-null    int64         
 3   Quantity     212 non-null    int64         
dtypes: datetime64[ns](1), int64(3)
memory usage: 6.8 KB
None
>>> merged_dataset.to_excel(r'C:\Users\Aravind S\Downloads\merged_dataset.xlsx', index=False)
