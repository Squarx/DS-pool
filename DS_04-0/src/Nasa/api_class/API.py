from typing import Dict
from PIL import Image
from collections import OrderedDict
from io import BytesIO
import IPython
import requests
import html_to_json
import numpy as np

from datetime import datetime


class Api_Nasa:

    def __init__(self, date_str="", concept_tags=False, hd=True, count="", start_date="", end_date="",
                 thumbs=True):
        self.__params = dict(api_key='yWCsjyyPOTXtzHhqbC8SxWatYIsxCBZfdpmum5xy',
                             date=self.valid(date_str),
                             concept_tags=concept_tags,
                             hd=hd,
                             count=self.valid_int(count),
                             start_date=self.valid(start_date),
                             end_date=self.valid(end_date),
                             thumbs=thumbs
                             )
        self.__response = self.get_response()

    def print_dict(self):
        print(type(self.__params['date']))

    def validtor(self):
        tt = datetime.strptime(self.__params['date'], "%Y-%m-%d").date()
        date_min = datetime.strptime("1995-06-16", "%Y-%m-%d").date()
        count = self.__params['count']
        start_date = self.__params['start_date']
        end_date = self.__params['end_date']
        if tt < date_min:
            return 1
        elif self.__params['date'] != "":
            self.__params['count'] = ""
            self.__params['start_date'] = ""
            self.__params['end_date'] = ""
        return 0

    def get_response(self):
        url = 'https://api.nasa.gov/planetary/apod'
        response = requests.get(url, params=self.__params)
        return response.json()

    def get_img_url(self):
        lst_links = []
        for i in range(0, len(self.__response) - 1):
            lst_links.append(self.__response[i]['hdurl'])
        return lst_links
        # на выходе будет такой список ссылок
        # https://apod.nasa.gov/apod/image/2301/PaleBlueDotOrig_Voyager1_960.jpg
        # https://apod.nasa.gov/apod/image/2301/AllPlanets_Tezel_1680_annotated.jpg
        # https://apod.nasa.gov/apod/image/2301/KembleCascade_Lease_3668.jpg
        # https://apod.nasa.gov/apod/image/2301/cg4_selby_5430.jpg
        # https://apod.nasa.gov/apod/image/2301/M_45_Plejarden_Stefan_Thrun_klein4096.jpg
        # https://apod.nasa.gov/apod/image/2301/MoonOClock.jpg
        # https://apod.nasa.gov/apod/image/2301/ISS_TIANHE_FINAL_4_APOD.jpg

    def valid(self, arg):
        tt = ""
        date_min = datetime.strptime("1995-06-16", "%Y-%m-%d").date()
        try:
            tt = datetime.strptime(arg, "%Y-%m-%d").date()
            date_min = datetime.strptime("1995-06-16", "%Y-%m-%d").date()
            if tt < date_min:
                tt = date_min
        except ValueError:
            tt = ""
        return str(tt)

    def valid_int(self, arg):
        ret_val = ""
        try:
            ret_val = int(arg)
            # print(ret_val)
            if ret_val > 100 or ret_val < 0:
                ret_val = ""
        except ValueError:
            ret_val = ""
            # print("WTF")
            # print(str(ret_val))
        return str(ret_val)