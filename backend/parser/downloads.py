import re

from .parser import Parser

class Downloads(Parser):
    
    @classmethod
    def list(cls) -> list:
        list = []
        downloads_section = False
        
        with open(cls.file, 'r') as file:
            for line in file:
                line = line
                
                if line.startswith("downloads {"):
                    downloads_section = True
                elif line.startswith("}"):
                    downloads_section = False
                elif downloads_section and line:
                    url = line.split()[0]
                    ignore = '!ignore' in line
                    
                    list.append({
                        'url': url, 
                        'ignore': ignore
                    })
                    
        return {
            'downloads': list,
            'total': len(list),
            'path': cls.get_path(),
        }
        