
from utils.scraper import scrap
from utils.formatter import formatter, filter_table
from tkinter import Tk, Label, Entry, Button

root = Tk()
# root.geometry('800x600')

dividend_yield = 0
vacancy = 0
pvpa_minimun = 0
pvpa_maximun = 0


def submit():
    global dividend_yield, vacancy, pvpa_maximun, pvpa_minimun
    dividend_yield = dy_input.get()
    vacancy = vc_input.get()
    pvpa_minimun = pmin_input.get()
    pvpa_maximun = pmax_input.get()

    filter_table(dividend_yield, vacancy, pvpa_minimun, pvpa_maximun)


# LAYOUT
title = Label(master=root, text='Filtrador de FII')
title.grid(row=0, column=0, columnspan=2)

dy_label = Label(master=root, text='Dividend Yield:').grid(row=1, column=0)
dy_input = Entry(master=root).grid(row=2, column=0)

vc_label = Label(master=root, text='Taxa de Vacancia:').grid(row=1, column=1)
vc_input = Entry(master=root).grid(row=2, column=1)

pmin_label = Label(master=root, text='PVPA Minimo:').grid(row=3, column=0)
pmax_label = Label(master=root, text='PVPA Maximo:').grid(row=3, column=1)
pmin_input, pmax_input = Entry(master=root).grid(
    row=4, column=0), Entry(master=root).grid(row=4, column=1)


submit_btn = Button(master=root, text='Filtrar', command=submit)

root.mainloop()
headers, bodys = scrap()
formatter(headers, bodys)
