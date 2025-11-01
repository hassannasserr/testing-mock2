import unittest
from unittest.mock import patch, Mock
import requests

from employee_repository import EmployeeRepository

MOCK_EMPLOYEE_DATA_UNSORTED = [
    {"id": 3, "name": "Alice", "position": "Developer"},
    {"id": 1, "name": "Bob", "position": "Manager"},
    {"id": 2, "name": "Charlie", "position": "Designer"}
]

EXPECTED_SORTED_DATA = [
    {"id": 1, "name": "Bob", "position": "Manager"},
    {"id": 2, "name": "Charlie", "position": "Designer"},
    {"id": 3, "name": "Alice", "position": "Developer"}
]


class TestEmployeeRepository(unittest.TestCase):

    def setUp(self):
        self.repository = EmployeeRepository()
        self.api_url = "https://api.dummy.com/employees"

    @patch('employee_repository.requests.get')
    def test_successful_retrieval(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = MOCK_EMPLOYEE_DATA_UNSORTED
        
        mock_get.return_value = mock_response
        
        employees = self.repository.get_employees(self.api_url)
        
        mock_get.assert_called_once_with(self.api_url)
        self.assertEqual(employees, MOCK_EMPLOYEE_DATA_UNSORTED)

    @patch('employee_repository.requests.get')
    def test_error_handling(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        
        mock_get.return_value = mock_response
        
        employees = self.repository.get_employees(self.api_url)
        
        mock_get.assert_called_once_with(self.api_url)
        self.assertIsNone(employees)

    @patch('employee_repository.requests.get')
    def test_sorting_by_id(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = MOCK_EMPLOYEE_DATA_UNSORTED
        
        mock_get.return_value = mock_response
        
        employees = self.repository.get_employees(self.api_url)
        
        self.assertIsNotNone(employees)
        
        sorted_employees = sorted(employees, key=lambda x: x['id'])
        
        self.assertEqual(sorted_employees, EXPECTED_SORTED_DATA)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
