import os
import sys
from state import State, Alert, Health
from connect import session
from parser import checkState, checkHealth, checkGamma
from alert import AlertHandle
from fileio import load, gen

    
def routine():
    data = session()
    handler = AlertHandle(data)
    handler.run_assert()
    return 

def main():
    args = sys.argv
    if(args[1] == "run"):
        routine()
    elif(args[1] == "test"):
        os.system('python test.py')
    elif(args[1] == "gen"):
        if(args[2] == ""):
            raise Exception("第2引数がありません")
        else:
            gen(args[2])
    else:
        raise Exception("定義されていない引数です")
    return 


if __name__ == "__main__":
    main()

