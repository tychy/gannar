import os
import requests
from bs4 import BeautifulSoup
import re
from enum import Enum

class Alert(Enum):
    ATTACK  = 6
    GAMMA = 5
    BETA = 4
    HOME = 3
    OCC = 2
    HEALTH = 1

    

def send_line_notify(notification_message):
    line_notify_token= os.environ.get('LINE_TOKEN')
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'message: {notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)

def session():
    gurl = "http://cgi1.plala.or.jp/~ssdi/gannar.cgi"
    gid = os.environ.get('GANNAR_ID')
    gkey = os.environ.get('GANNAR_KEY')

    cert = {
        'gnm':gid,
        'gpw':gkey
    }
    s = requests.Session()
    r = s.post(gurl, data = cert)
    r.raise_for_status()
    r.encoding = 'shift_jis'
    t_spl = re.split('\n|<BR>|<TD COLSPAN=2>', r.text)
    return t_spl

def main():
    t_spl = session()
    date_pattern = re.compile('(\d{1,2})/(\d{1,2}).*が.*しました。')
    gamma = re.compile(r'雪|榊|ryuu')

    for idx, t in enumerate(reversed(t_spl)):
        m = date_pattern.search(t)
        if not m:
            continue
        if(gamma.search(t)):
            #インシデント
            print(t)
            #send_line_notify(t)

if __name__ == "__main__":
    main()
