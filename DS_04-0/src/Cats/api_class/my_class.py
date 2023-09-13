from PIL import Image
from collections import OrderedDict
from io import BytesIO
import IPython
import requests
import html_to_json
import numpy as np

# url2 = 'http://jservice.io/api/random?count=1'

class Web1:
    def __init__(self, num=404):
        # print("Создание объекта Person")
        self.__num = num
        self.__url = f'https://http.cat/{self.__num}'
        self.__data = requests.get(self.__url)
        self.__img = Image.open(BytesIO(self.__data.content))
        self.__url_home = 'https://http.cat/'


    # конструктор
    def open_img(self):
        if self.__data.ok:
            self.__img.show()
        else:
            print('No cats')

    def get_num(self):
        return self.__num

    def change_num(self, num=404):
        self.__num = num

    def print_data(self):
        print(self.__data)

    def print_available_list(self):
        output_json = html_to_json.convert(requests.get(self.__url_home).text)
        lst_available_nums = []
        for i in (str((output_json['html'])[0])).split(','):
            if ("\'a\': [{'_attributes': {'href': " in i) and ('https' not in i) and (len(i) == 39):
                lst_available_nums.append(i[-5:-2])
        # print(f'You can choose one of this values :{lst_available_nums}')
        return lst_available_nums

    def get_image(self):
        return self.__img

    def split_lst(self, cols):
        lst = self.print_available_list()
        tt = np.array_split(lst, cols)
        return tt
