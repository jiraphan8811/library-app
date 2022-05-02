import justpy as jp
import pandas as pd

# Load data showing percent of women in different majors per year
wm_df = pd.read_csv('library.csv').round(2)
wm_df_search = wm_df.set_index('CODE')

headers = list(wm_df.columns)
table_data = wm_df.to_numpy().tolist()
table_data.insert(0, headers)

           
