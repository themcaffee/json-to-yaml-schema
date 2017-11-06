import argparse
from collections import OrderedDict
import json
import yaml

"""
Simple tool to convert response JSON into OpenAPI Schema YAML.
"""


def setup_yaml():
  """ https://stackoverflow.com/a/8661021 """
  represent_dict_order = lambda self, data:  self.represent_mapping('tag:yaml.org,2002:map', data.items())
  yaml.add_representer(OrderedDict, represent_dict_order)


def parse_properties(property_obj):
    properties = {}
    for i in property_obj:
        properties[i] = {}
        prop_type = ''
        # Get correct type of this item
        if type(property_obj[i]) == str:
            prop_type = 'string'
        elif type(property_obj[i] == int):
            prop_type = 'number'
        properties[i]['type'] = prop_type
    return properties


if __name__ == '__main__':
    # Get and parse arguments
    parser = argparse.ArgumentParser(description="Turn json into openapi yaml schemas")
    parser.add_argument('json', help='The json response')
    args = parser.parse_args()
    parsed_json = json.loads(args.json)

    # Use an OrderedDict to preserve the key ordering
    yaml_schema = OrderedDict()

    # Create the yaml schema we want
    if type(parsed_json) == list:
        yaml_schema['type'] = 'array'
        yaml_schema['items'] = OrderedDict()
        yaml_schema['items']['type'] = 'object'

        # Handle all properties of this list
        yaml_schema['items']['properties'] = parse_properties(parsed_json[0])
    elif type(parsed_json) == dict:
        yaml_schema['type'] = 'object'
        yaml_schema['properties'] = parse_properties(parsed_json)

    # Dump out the yaml
    setup_yaml()
    yaml_output = yaml.dump(yaml_schema, default_flow_style=False)
    print(yaml_output)
