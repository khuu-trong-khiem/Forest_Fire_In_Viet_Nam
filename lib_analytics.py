from IPython.display import display_html
import random 

def showInfoDataFrame(df):
    print(df.shape)
    display(df.head(3))
    
def displaySideBySide(dict_table):
    style = 'style="color: black; text-align: center; font-size: 14px; font-weight: bold;"'
    html_str=''
    for name, df in dict_table.items():
        html_str += df.to_html().replace(
            '<table border="1" class="dataframe">',
            '<table border="1" class="dataframe"> <caption ' + style + '>' + name + '</caption>'
        )
    display_html(html_str.replace('table','table style="display:inline"'),raw=True)
    
def showComponentOfColumn(df):
    for column in df.columns:
        print(column, ' - ', df[[column]].groupby(column).sum().index.tolist())
        print(' ')