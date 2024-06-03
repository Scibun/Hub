import re

class Parser:
    
    @classmethod
    def __init__(cls, params:dict):
        cls.file = params['file']
    
    @classmethod
    def get_path(cls):
        with open(cls.file, 'r') as file:
            config_data = file.read()

        match = re.search(
            r'path\s*=\s*"([^"]+)"', config_data
        )
        
        if match:
            return match.group(1)
        
    @classmethod
    def get_readme(cls):
        with open(cls.file, 'r') as file:
            config_data = file.read()

        match = re.search(
            r'readme\s*=\s*"([^"]+)"', config_data
        )
        
        if match:
            return match.group(1)
  