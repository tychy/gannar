import os
import pickle
from connect import session

def gen(name):
    data = session()
    with open(os.path.join("test", name+".pickle"), "wb") as f:
        pickle.dump(data, f)

def load(name):
    data_path = os.path.join("test", name + ".pickle")
    if not os.path.exists(data_path):
        raise Exception("ファイルがありません")
    with open(data_path, "rb") as f:
        data = pickle.load(f)
    return data


