#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json


def print_forecast(city_code):
    url_head = "http://weather.livedoor.com/forecast/webservice/json/v1?city="
    forecast_json = requests.get(url_head + str(city_code))
    forecast_dict = forecast_json.json()
    print(forecast_dict["description"]["text"])


city_code = input("city_code:")
print_forecast(city_code)
