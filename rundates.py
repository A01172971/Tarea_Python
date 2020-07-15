#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dates

def run(filename):
    # rt means read-text (read/write)-(text/binary)
    with open(filename,'rt') as f:
        for line in f:
            l = line.strip()
            o = dates.make_a_date(from_date=l)
            out = f"{l}\t{o}"
            print(out)


if __name__ =="__main__":
    run('indates.txt')
