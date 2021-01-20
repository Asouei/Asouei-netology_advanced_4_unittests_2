import unittest
import requests

from unittest import TestCase
from unittest.mock import patch

from main import *

# Для обработки всех ошибок я написал декоратор, который выдает пройденный тест если папка создана и
# подходящую ошибку если тест не пройден

def mock_folder_creation():
    response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                            headers={'Authorization': TOKEN}, params={'path': FOLDER_NAME})

    code = response.status_code

    if code == 403:
        return 'Ошибка Api'
    if code == 401:
        return 'Ошибка "Не авторизован"'
    if code == 409:
        return f'Ресурс "{FOLDER_NAME}" уже существует.'
    if code == 423:
        return 'Ресурс заблокирован. Возможно, над ним выполняется другая операция.'
    if code == 503:
        return '503'

    if code == 201:
        return True


class TestFolderCreation(TestCase):

    @patch('main.folder_creation', side_effect=mock_folder_creation)
    def test_folder_creation(self, folder_creation):
        self.assertEqual(folder_creation(), True)


