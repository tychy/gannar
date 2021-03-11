from state import State, Alert, Health
from connect import session
from parser import checkState, checkHealth, checkGamma
from alert import AlertHandle

def main():
    data = session()
    # 開始前なら終了
    if(checkState(data) == State.WAIT):
        print("WAIT")
        return
    handler = AlertHandle()
    handler.health = checkHealth(data)
    return 

if __name__ == "__main__":
    main()

