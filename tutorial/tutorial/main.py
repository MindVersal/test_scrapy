import os
import subprocess
from tutorial.tutorial.avito_test_clear import clear_avito_json


def clear_old_avito_json():
    if os.path.exists('data/avito.json'):
        path_avito_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data/avito.json')
        os.remove(path_avito_file)
        print('Old avito.json removed.')


if __name__ == '__main__':
    file_name = 'avito'
    # command = 'scrapy runspider ./spiders/avito.py -o ./data/avito.json'
    command = 'avito.bat'
    clear_old_avito_json()
    subprocess.call([command])
    clear_avito_json(file_name)
