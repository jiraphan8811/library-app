import justpy as jp
import pandas as pd

# Load data showing percent of women in different majors per year
wm_df = pd.read_csv('library.csv').round(2)
wm_df['TITLE'] = wm_df['TITLE'].astype('str')
headers = list(wm_df.columns)
table_data = wm_df.to_numpy().tolist()
table_data.insert(0, headers)


def grid_test():
    wp = jp.WebPage()
    d = jp.Div(classes='w-7/8 m-2 p-3 border rounded-lg ', a=wp)
    wm_df.jp.ag_grid(a=d)  # a=wp adds the grid to WebPage wp
    
    return wp

jp.justpy(grid_test)