import yaml

def load_config(path=r"/Users/kishorekumar/Desktop/python project/carpriceprd/config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

