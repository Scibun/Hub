import re

from .parser import Parser

from backend.utils.files import Files

class Checksum(Parser):
            
    @classmethod
    def get_checksum_content(cls, link:str) -> dict:
        files = []
        content = Files.read_remote_file(link)
        
        for line in content.split('\n'):
            parts = line.split(maxsplit=1)
            
            if len(parts) == 2:
                hash_value, filename = parts
                
                files.append({
                    'file': filename,
                    'hash': hash_value
                })
        
        return {
            'link': link,
            'json': files,
            'plain': content,
            'hashes_total': len(files),
            'ref_file': link.split('/')[-1] 
        }
            
    @classmethod
    def get(cls):
        with open(cls.file, 'r') as file:
            config_data = file.read()

        match = re.search(
            r'checksum\s*=\s*"([^"]+)"', config_data
        )
        
        if match:
            return cls.get_checksum_content(
                match.group(1)
            )
