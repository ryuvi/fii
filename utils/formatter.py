
from pandas import DataFrame


def formatter(header, body):
    _data_frame = DataFrame(data=body, columns=header)
    _data_frame.to_excel('src/FII_Table.xlsx',
                         sheet_name='Tabela', index=False)


def to_float_percentage(number):
    return float(('%.2f' % number.replace('%', '')))/100
