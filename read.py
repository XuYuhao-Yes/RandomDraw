import csv
import json


class Read:
    def __init__(self):
        self.config_path = "./data/config.json"
        self.config = self.read_json()

    def read_json(self):
        with open(self.config_path, 'r', encoding='utf-8') as config_file:
            config = json.load(config_file)
        return config

    def read_csv(self):
        name = []
        with open(self.config["csv_path"], encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for i in reader:
                name.append(i[0])
        return name

    def write_json(self):
        with open(self.config_path, "w", encoding="utf-8") as config_file:
            json.dump(self.config, config_file)
