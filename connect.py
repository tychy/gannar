import os
import requests
import re

def sendLineNotify(notification_message):
    line_notify_token= os.environ.get('LINE_TOKEN')
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'message: {notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)

def session(mode=1):
    gurl = "http://cgi1.plala.or.jp/~ssdi/gannar.cgi"
    gid = os.environ.get('GANNAR_ID')
    gkey = os.environ.get('GANNAR_KEY')

    cert = {
        'gnm':gid,
        'gpw':gkey,
        'mode':mode
    }
    s = requests.Session()
    r = s.post(gurl, data = cert)
    r.raise_for_status()
    r.encoding = 'shift_jis'
    data = re.split('\n|<BR>|<TD COLSPAN=2>', r.text)
    return data

