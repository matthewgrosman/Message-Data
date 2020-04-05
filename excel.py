# excel.py
# This module contains the function to write data to an excel spreadsheet


import xlsxwriter


def write_to_excel(d: dict, data: str, name: str):
    """ Writes dictionary data to an excel spreadsheet """
    workbook = xlsxwriter.Workbook(f'C:\\message_data\\{name}\\{name}_{data}.xlsx')
    worksheet = workbook.add_worksheet()

    for i, (key, value) in enumerate(d.items()):
        worksheet.write(0, i, key)
        worksheet.write(1, i, value)

    workbook.close()
