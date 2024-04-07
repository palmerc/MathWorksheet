#!/usr/bin/env python3

import argparse
import pathlib
import tempfile

from lib.multiplication import MultiplicationWorksheet
from lib.division import DivisionWorksheet
from lib.addition import AdditionWorksheet
from lib.subtraction import SubtractionWorksheet
from lib.pages import Pages


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate worksheets for practicing math facts.')
    parser.add_argument('--type', '-t', choices=['multiplication', 'division', 'addition', 'subtraction'],
                        default='multiplication', help='Choose a worksheet type')
    parser.add_argument('--answers', '-a', action='store_true',
                        help='Generate an answer key')
    parser.add_argument('--count', '-c', type=int, default=1,
                        help='Number of worksheets to generate')
    args = parser.parse_args()

    with tempfile.TemporaryDirectory() as t:
        pages = []
        for i in range(args.count):
            if args.type == 'multiplication':
                ws = MultiplicationWorksheet()
            elif args.type == 'division':
                ws = DivisionWorksheet()
            elif args.type == 'addition':
                ws = AdditionWorksheet()
            elif args.type == 'subtraction':
                ws = SubtractionWorksheet()
            else:
                raise ValueError('Invalid worksheet type')

            tempfile = pathlib.Path(t) / f'worksheet_{i}.pdf'
            ws.fill_document()
            ws.generate_pdf(tempfile, clean_tex=True)
            pages.append(tempfile)
        p = Pages(pages)
        p.generate_pdf('worksheet', clean_tex=True)

