
import yaml
import json

def process_yaml_to_dict(file):
    with open(file, "r") as stream:
        with open('data.json', 'w') as f:
            # print(yaml.safe_load(stream))
            json.dump(yaml.safe_load(stream), f)
            
process_yaml_to_dict("server.yaml")