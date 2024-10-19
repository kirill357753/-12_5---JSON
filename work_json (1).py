import json
from typing import List, Dict

class JSONWorker:
    def __init__(self, data: List[Dict[str, str]]):
        if isinstance(data, list) and len(data) == 3 and all(isinstance(item, dict) for item in data):
            self.data = data
        else:
            self.data = [] 

    def write_to_file(self, filename: str) -> None:
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(self.data, json_file, ensure_ascii=False, indent=4)

    def read_from_file(self, filename: str) -> List[Dict[str, str]]:
        with open(filename, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)

if __name__ == "__main__":

    data = [
        {"name": "Alice", "age": "30"},
        {"name": "Bob", "age": "25"},
        {"name": "Charlie", "age": "35"}
    ]

    worker = JSONWorker(data)

    filename = "data.json"
    worker.write_to_file(filename)
    print(f"Данные записаны в файл: {filename}")

    loaded_data = worker.read_from_file(filename)
    print("Данные, прочитанные из файла:", loaded_data)