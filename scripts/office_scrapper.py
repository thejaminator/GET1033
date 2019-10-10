import requests
import json
import time
import pandas as pd
import os
import numpy as np

if __name__ == '__main__' :
    mailheaders = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip',
    'Accept-Language': 'en-US',
    'Authorization': input('paste token of webmail authorization'),
    'Client-Request-Id': 'WebSDK/1346633340',
    'Connection': 'keep-alive',
    'Host': 'webpoolsg20f15.infra.lync.com',
    'Referer': 'https://webpoolsg20f15.infra.lync.com/Autodiscover/XFrame/XFrame.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'X-MS-Correlation-Id': '1346633843',
    'X-Ms-Namespace': 'internal',
    'X-Ms-Origin': 'https://outlook.office.com',
    'X-MS-RequiresMinResourceVersion': '2',
    'X-Ms-SDK-Host': 'Exchange',

    'X-Ms-SDK-Version': 'SkypeWeb/0.4.885 master SWX(1.118.30 - Exchange)'
    }


    original = pd.read_csv('table.csv')
    id = np.max(original['id']) + 1
    starturl = 'https://webpoolsg20f15.infra.lync.com/ucwa/oauth/v1/applications/113674770740/people/search?mail=sip%3Ae'
    endurl = '%40u.nus.edu'
    table = []
    errorcount = 0
    while id < 400000:
        fullid = str(id).zfill(7)
        with requests.session() as c:
            queryurl= starturl + fullid + endurl
            while True:
                try:
                    result = c.get(queryurl, headers=mailheaders, timeout = 0.9)
                    data = json.loads(result.text)
                    department = (data['_embedded']['contact'][0]['department'])
                    name = (data['_embedded']['contact'][0]['name'])
                    student_info = [fullid, name, department]
                    table.append(student_info)
                    print (student_info)
                except Exception:
                    errorcount += 1
                    print ('ERROR WITH ' + fullid + ' error count: ' + str(errorcount))
                    df = pd.DataFrame(table, columns=['id','name','department'])
                    with open('table.csv', 'a') as f:
                        df.to_csv(f, header=False, index=False)
                    table = [] #clears table to prevent duplicates
                    time.sleep(120)
                break
        #save every 500 ids
        if id % 500 == 0:
            df = pd.DataFrame(table, columns=['id','name','department'])
            with open('table.csv', 'a') as f:
                df.to_csv(f, header=False, index=False)
            table = [] #clears table to prevent duplicates
        id += 1



                

