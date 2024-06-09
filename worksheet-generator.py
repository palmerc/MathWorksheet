#!/usr/bin/env python3

import argparse
import pathlib
import re
import tempfile

from lib.multiplication import MultiplicationWorksheet
from lib.division import DivisionWorksheet
from lib.addition import AdditionWorksheet
from lib.subtraction import SubtractionWorksheet
from lib.clocks import ClocksWorksheet
from lib.ruled_paper import RuledPaperWorksheet
from lib.pages import Pages


def parse_range(string):
    m = re.match(r'(?P<start>\d+)[,-]{1}(?P<end>\d+)?$', string)
    if not m:
        raise argparse.ArgumentTypeError(f'"{string}" is not a range of number. Expected forms like "0-5" or "0,5"')
    return range(int(m.group('start'), 10), int(m.group('end'), 10))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate worksheets for practicing math facts.')
    parser.add_argument('--type', '-t', choices=['multiplication', 'division',
                                                 'addition', 'subtraction', 'clocks', 'ruled-paper'],
                        default='multiplication', help='Choose a worksheet type')
    parser.add_argument('--answers', '-a', action='store_true',
                        help='Generate an answer key')
    parser.add_argument('--count', '-c', type=int, default=1,
                        help='Number of worksheets to generate')
    parser.add_argument('--range', type=parse_range)
    parser.add_argument('--debug', action='store_true', help=argparse.SUPPRESS)
    args = parser.parse_args()

    with tempfile.TemporaryDirectory() as tempdir:
        pages = []
        for i in range(args.count):
            if args.type == 'multiplication':
                ws = MultiplicationWorksheet()
            elif args.type == 'division':
                ws = DivisionWorksheet()
            elif args.type == 'addition':
                ws = AdditionWorksheet(args.range, answers=args.answers)
            elif args.type == 'subtraction':
                ws = SubtractionWorksheet()
            elif args.type == 'clocks':
                ws = ClocksWorksheet()
            elif args.type == 'ruled-paper':
                ws = RuledPaperWorksheet()
            else:
                raise ValueError('Invalid worksheet type')

            ws.fill_document()
            if args.debug:
                print(ws.dumps())

            tempfile_path = pathlib.Path(tempdir) / f'worksheet_{i}.pdf'
            ws.generate_pdf(tempfile_path, clean_tex=True)
            pages.append(tempfile_path)
        p = Pages(pages)
        p.generate_pdf('worksheet', clean_tex=True)

