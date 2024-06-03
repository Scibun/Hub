import requests

class Files:
    
    @classmethod
    def read_remote_file(cls, url):
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.text
        
        return None
