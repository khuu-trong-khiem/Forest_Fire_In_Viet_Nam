import pandas as pd

def parseHead(table):
    columns = []
    head_content = table.find('thead')
    tr_content = head_content.find_all('tr')
    for tr in tr_content:
        th_content = tr.find_all('th')
        for th in th_content:
            columns.append(th.text)
    return columns

def parseBody(table):
    list_rows = []
    body_content = table.find('tbody')
    tr_content = body_content.find_all('tr')
    for tr in tr_content:
        td_content = tr.find_all('td')
        if(len(td_content) == 0):
            continue
        else:
            row = []
            for td in td_content:
                row.append(td.text)
            list_rows.append(row)
    return list_rows

def parseData(table):
    columns = parseHead(table)
    df = pd.DataFrame(columns=columns)
    list_rows = parseBody(table)
    for row in list_rows:
        df.loc[len(df)] = row
    return df

def parseSelect(soup, strId):
    select_content = soup.find('div', attrs={'id': strId})
    label_content = select_content.find('div', attrs={'class': 'slabel'})
    title = label_content.text
    dict_years = {}
    list_content = select_content.find_all('a')
    for item in list_content:
        dict_years[item['v']] = item.text
    return title, dict_years

def setAttribute(browser, strId, select):
    browser.execute_script("document.getElementById('{}').setAttribute('v','{}');".format(strId, select))