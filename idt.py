import time
from datetime import date
import pandas_datareader.data as web 
from datetime import date, timedelta
from rich.live import Live
from rich.table import Table


def generate_table() -> Table:
    table = Table()
    table.add_column("Name")
    table.add_column("Adj Close")
    table.add_column("Daily Change")
    table.add_column("Volume")

    today = date.today()
    file1 = open('config.txt', 'r')
    lines = file1.readlines()

    assets = []
    for line in lines[2:]:
        assets.append(line.strip())

    colors = []
    tableData = []
    for asset in assets:
        try:
            rowData = []
            data = web.get_data_yahoo(asset, start=today - timedelta(1), end=today)
            dataCurr = data[-1:]
            dataPrev = data[-2:-1]
            assetName = str(asset)
            adjClose = round(float(dataCurr['Adj Close']), 4)
            dailyChange = round((int(dataCurr['Adj Close']) - int(dataPrev['Adj Close'])) / int(dataPrev['Adj Close']) * 100, 4)
            dailyChangeStr = f"{round((int(dataCurr['Adj Close']) - int(dataPrev['Adj Close'])) / int(dataPrev['Adj Close']) * 100, 4)}%"
            volume = int(dataCurr['Volume'])
            rowData.append(assetName)
            rowData.append(adjClose)
            rowData.append(dailyChangeStr)
            rowData.append(volume)
            tableData.append(rowData)
            if dailyChange > 0.0:
                colors.append('green')
            else:
                colors.append('red')
        except:
            pass


    for i, row in enumerate(tableData):
        table.add_row(
            f"{tableData[i][0]}", f"{tableData[i][1]}", f"[{colors[i]}]{tableData[i][2]}", f"{tableData[i][3]}"
        )
    return table


with Live(generate_table(), refresh_per_second=4) as live:
    for _ in range(99999999999999999):
        time.sleep(0.4)
        live.update(generate_table())