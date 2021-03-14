import re
from state import State, Health

def checkState(data):
    pattern = re.compile('に開始します。')
    for idx, t in enumerate(reversed(data)):
        m = pattern.search(t)
        if not m:
            continue
        else:
            return State.WAIT
    return State.RUN

def checkHealth(data):
    pattern = re.compile('移動力')
    health = 0
    maxhealth = 0
    for idx, t in enumerate(reversed(data)):
        m = pattern.search(t)
        if not m:
            continue
        idx = 0
        while(idx < len(t)):
            if t[idx] >='1' and t[idx] <= '2': 
                if(t[idx+1] == '/'):
                    health = int(t[idx:idx+1])
                    idx = idx + 2
                else:
                    health = int(t[idx:idx+2])
                    idx = idx + 3
                maxhealth = int(t[idx:idx+2])
                if(health == maxhealth and health > 0 and maxhealth > 0):
                    return Health.FULL
                else:
                    return Health.NOFULL
            idx += 1 
    raise Expection('Healthが見つけられませんでした')
    return Health.NOFULL

def checkOcc(data):
    # 自分の場所ー＞ログ解析
    x = -1
    y = -1
    pattern = re.compile('現在地.*(\d{1,2}).(\d{1,2})\)')
    for idx, t in enumerate(reversed(data)):
        m = pattern.search(t)
        if not m:
            continue
        idx = 0
        print(t)
        while(idx < len(t)):
            if t[idx] >='1' and t[idx] <= '2': 
                if(t[idx+1] == '.'):
                    x = int(t[idx:idx+1])
                    idx = idx + 2
                else:
                    x = int(t[idx:idx+2])
                    idx = idx + 3
                y = int(t[idx:idx+2])
                break;
            idx += 1 
    if(x == -1 and y == -1):
        raise Exception('座標が取得できませんでした')
    print(x)
    print(y)
     
def checkGamma(data):
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

