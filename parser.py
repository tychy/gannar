import re
from state import State, Health

def checkState(data):
    pattern = re.compile(r'に開始します。')
    for idx, t in enumerate(reversed(data)):
        m = pattern.search(t)
        if not m:
            continue
        else:
            return State.WAIT
    return State.RUN

def checkHealth(data):
    pattern = re.compile(r'移動力')
    health = 0
    maxhealth = 0
    for idx, t in enumerate(reversed(data)):
        m = pattern.search(t)
        if not m:
            continue
        idx = 0
        while(idx < len(t)):
            if t[idx] >='1' and t[idx] <= '2': 
                health = int(t[idx:idx+2])
                maxhealth = int(t[idx+3:idx+5])
                if(health == maxhealth and health > 0 and maxhealth > 0):
                    return Health.FULL
                else:
                    return Health.NOFULL
            idx += 1 
    raise Expection('Healthが見つけられませんでした')
    return Health.NOFULL

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

