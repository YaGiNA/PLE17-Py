#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json


def print_forecast(city_code, day):
    if not(day):
        day = 0
    url_head = "http://weather.livedoor.com/forecast/webservice/json/v1?city="
    forecast_dict = requests.get(url_head + str(city_code)).json()
    if(int(day) > 2):
        print("Wrong letter.")
        return 1
    location_d = forecast_dict["location"]
    location = " ".join(
        [
            location_d["area"],
            location_d["prefecture"],
            location_d["city"],
        ]
    )
    forecast_d = forecast_dict["forecasts"][int(day)]
    title = forecast_d["telop"]
    forecast_words = [
        location, "の", forecast_d["dateLabel"], "の天気は",
        title, "です"
    ]
    print("".join([forecast_word for forecast_word in forecast_words]))
    return 0


city_code = input("city_code: ")
day = input("Today: 0,  Tommorow: 1, Day after tomorrow: 2 (default: today): ")
print_forecast(city_code, day)
