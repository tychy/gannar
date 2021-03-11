import sys
import os
import pickle
from connect import session

def gen(name):
    data = session()
    with open(os.path.join("test", name+".pickle"), "wb") as f:
        pickle.dump(data, f)

def main():
    args = sys.argv
    if(args[1] == "gen"):
        if(args[2] == ""):
            raise Exception("第2引数がありません")
        else:
            gen(args[2])
    else:
        raise Exception("定義されていない引数です")
    return 

if __name__ == "__main__":
    main()

