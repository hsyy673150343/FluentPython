#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/22 17:11
# @Author   : 洪松
# @File     : example3_1.py
'''字典推导的应用'''
DIAL_CODES = [
        (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        (7, 'Russia'),
        (81, 'Japan'),
    ]
country_code = {country: code for code, country in DIAL_CODES}
print(country_code)

country_code = {code: country.upper() for country, code in country_code.items() if code < 60}
print(country_code)

