#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime as dt
import re


def make_a_date(from_date="", until_hour=""):
    day_names = ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"]

    today = dt.datetime.now()
    y = today.year
    m = today.month
    d = today.day
    w = today.weekday()

    if from_date != "":
        # separa texto en base a un texto
        # "\s" significa cualquier espacio, tabulador ....

        # obtiene anio, mes y dia en formato string
        ys, ms, ds = re.split("-", from_date)
        # convierte string a int
        y = int(ys)
        m = int(ms)
        d = int(ds)

        # construye la fecha y dia de la semana
        fecha = dt.datetime(y, m, d)
        w = fecha.weekday()

    offset = 1
    if day_names[w] in ["Vie", "Sab"]:
        if day_names[w] == "Vie":
            offset = 3
        else:
            offset = 2

    try:
        new_date = dt.datetime(y, m, d + offset)
    except:
        if m + 1 <= 12:
            x=1
            while True:
                new_date = dt.datetime(y, m + 1, x)
                if not new_date.weekday() in [0,1,2,3,4]:
                    x=x+1
                    continue
                else:
                    break

        else:
            x=1
            while True:
                new_date = dt.datetime(y+1, 1, x)
                if not new_date.weekday() in [0,1,2,3,4]:
                    x=x+1
                    continue
                else:
                    break

    ny = new_date.year
    nm = new_date.month
    nd = new_date.day
    nw = new_date.weekday()

    text = new_date.strftime("%Y-%m-%d")
    wday = day_names[nw]

    text_return = f"{text} ({wday})"
    return text_return


if __name__ == '__main__':
    dates = ['', '2020-07-09', '2020-07-10', '2020-07-11', '2020-07-12']
    for d in dates:
        c = make_a_date(d)
        print("From:", d, "To:", c)
