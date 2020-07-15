#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import rundates

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Given a text file with dates in format "Y-m-d", this program computes next date')
    parser.add_argument('-f','--file', default='' ,help='Input file to process')

    args = parser.parse_args()

    if args.file!='':
        rundates.run(args.file)
    else:
        print("No input file was given")


# TAREA: MODIFICAR ESTE PROGRAMA PARA QUE ACEPTE UN ARGUMENTO LLAMADO
# -o FILE | --output FILE
# y si tiene un valor distinto del x defecto
# ENTONCES USAR ESE NOMBRE DE ARCHIVO PARA GUARDAR LA SALIDA DEL PROGRAMA DE FECHAS

# TIPS:
# open(FILENAME,'wt')
# Crear una funcion basada en rundates.run que acepte un nombre de archivo de salida
# y guarde los datos en ese archivo de salida
# def run_and_save(input_file, output_file):
#     #####
