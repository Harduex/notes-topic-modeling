import json

with open("data/quotes.json") as data_file:
    original_json = json.load(data_file)

data = original_json['data']
quotes_list = []

for obj in data:
    quotes_list.append(obj['QUOTE'])

def write_data(file, data):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

write_data('output.json', quotes_list)