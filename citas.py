#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import dates


def fun00():
    fecha0 = input("")
    try:
        fecha1 = dates.make_a_date(fecha0)
    except:
        fecha1 = ''

    print(f"{fecha0}\t{fecha1}")


def fun01(filename2):
    fecha0 = input("")
    try:
        fecha1 = dates.make_a_date(fecha0)
    except:
        fecha1 = ''

    with open(filename2, 'wt') as f:
        f.write(f"{fecha0}\t{fecha1}")


def fun10():
    None


def fun11(input, output):
    None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Procesa fechas de citas')
    parser.add_argument('-i', '--input', default='', help='Archivo de entrada con fechas en formato Y-m-d')
    parser.add_argument('-o', '--output', default='',
                        help='Archivo de salida con fechas de entrada y de salida en formato Y-m-d')

    args = parser.parse_args()

    if args.input == '' and args.output == '':
        fun00()
    elif args.input == '' and args.output != '':
        fun01(args.output)
    elif args.input != '' and args.output == '':
        fun10()
    elif args.input != '' and args.output != '':
        fun11(args.input, args.output)
    else:
        print("ALERTA!!! Esta opcion nunca deberia de ejecutarse")
        exit(1)
        # TIP: exit(0) es el estandar para terminar cualquier programa
        #     exit(1), exit(2),.... significa que el programa termino con un valor de error
