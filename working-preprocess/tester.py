import yaml

if __name__ == '__main__' :
    with open('./config_test.yaml', 'r') as f :
        yml = yaml.load(f)
        print(yml)