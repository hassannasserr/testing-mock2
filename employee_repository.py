import requests

class EmployeeRepository:
    
    def get_employees(self, api_url):
        try:
            response = requests.get(api_url)
            
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except requests.exceptions.RequestException:
            return None
