import json
import os 

File="employees.json"

def load_data():
    if not os.path.exists(File):
        return[]
    with open(File,"r") as f:
        try:
            return json.load(f)
        except:
            return[]
        