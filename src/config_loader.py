import yaml

def load_config(path="/Users/kishorekumar/Desktop/carpriceprd/config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

