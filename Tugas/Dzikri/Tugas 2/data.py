import json

def writeFile (file, data):
    json_data = json.dumps(data)
    f = open(file, 'w')
    f.write(json_data)
    f.close()
    return True

def readFile (file, mode='r'):
        f = open(file, mode=mode)
        json_data = f.read()
        json_data = json.loads(json_data)
        f.close()
        return json_data