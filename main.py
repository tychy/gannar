from state import *
from connect import *
from parser import *
from alert import AlertHandle
from parser import *

def main():
    t_spl = session()
    # 開始前なら終了
    if(checkState(t_spl) == State.WAIT):
        print("WAIT")
        return
    handler = AlertHandle()
    handler.health = checkHealth(t_spl)
    return 

if __name__ == "__main__":
    main()

