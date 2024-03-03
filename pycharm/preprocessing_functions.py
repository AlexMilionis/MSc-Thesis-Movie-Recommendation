import json

def open_json(json_file:json) -> list:
    json_list = []
    with open(json_file, 'r') as file:
        for line in file:
            try:
                json_list.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON from line: {line}")
                print(e)
    return json_list

def remove_carriage_return(json_list:json) -> list:
    for i in range(len(json_list)):
        json_list[i]['txt'] = json_list[i]['txt'].replace('\r', '')
    return json_list