import json

def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.loads(f.read())

def write_json(data, file_path):
    jsonified = json.dumps(data)
    with open(file_path, 'w') as f:
        f.write(jsonified)

