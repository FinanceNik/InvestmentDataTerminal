#!/usr/bin/env python

import pandas as pd
import numpy as np
import pandas_datareader.data as web 
from datetime import date, timedelta
from time import sleep
from tabulate import tabulate


def main():
    today = date.today()
    file1 = open('config.txt', 'r')
    lines = file1.readlines()

    assets = []
    for line in lines[2:]:
        assets.append(line.strip())

    tableData = []
    # tableData.append(['Name', 'Adj. Close', 'Volume'])
    # tableData.append(['-------------------', '-------------------', '-------------------'])
    for asset in assets:
        rowData = []
        data = web.get_data_yahoo(asset, start=today - timedelta(1), end=today)[-1:]
        assetName = str(asset)
        adjClose = round(float(data['Adj Close']), 2)
        volume = int(data['Volume'])
        rowData.append(assetName)
        rowData.append(adjClose)
        rowData.append(volume)
        tableData.append(rowData)

    # for row in tableData:
    # print("{: >20} {: >20} {: >20}".format(*row), end="\r")

    print(tabulate(tableData, headers=['Name', 'Adj. Close', 'Volume']), end='\r')


if __name__=='__main__':
    while True:
        main()
