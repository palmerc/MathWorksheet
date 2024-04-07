#!/usr/bin/env python3
import argparse

from pylatex import Document
from pylatex.base_classes import Arguments, Command, Environment
from pylatex.basic import HFill, LineBreak, NewLine
from pylatex.package import Package
from pylatex.position import VerticalSpace, HorizontalSpace, Center
from math_commands import Multiplication, Division, Addition, Subtraction
import random


class Framed(Environment):
    packages = [Package('framed')]


class Worksheet(Document):
    _title = None
    _instructions = None

    def __init__(self):
        super().__init__(indent=False, geometry_options={'lmargin': '2cm', 'rmargin': '2cm'})
        self.change_document_style('empty') # No page number please
        self._add_header()

    def _add_header(self):
        with self.create(Framed()) as e:
            with e.create(Center()) as f:
                f.append(Command('LARGE'))
                f.append(Command('textbf', self._title))

        self.append(VerticalSpace('.5cm'))

        self.extend(['Name:', Command('underline', HorizontalSpace('4cm')), HFill()])
        self.extend(['Date:', Command('underline', HorizontalSpace('4cm')), HFill()])
        self.extend(['Score:', Command('underline', HorizontalSpace('1cm')), '/100'])
        self.append(NewLine())

        with self.create(Center()) as e:
            e.append(self._instructions)


class MultiplicationWorksheet(Worksheet):
    _title = 'Multiply by 1 to 9'
    _instructions = 'Calculate each product.'

    def __init__(self):
        super().__init__()
        self.append(Multiplication.command())

    @staticmethod
    def _problems(r, count):
        m = [(i, j, i*j) for i in r for j in r]
        random.shuffle(m)
        if len(m) > count:
            m = m[:count]
        return m

    def fill_document(self):
        index = 0
        for i, j, _ in self._problems(range(1, 10), count=80):
            self.append(Multiplication(arguments=Arguments(i, j)))

            row = int(index / 10) + 1
            column = index % 10 + 1
            if column == 10:
                self.append(VerticalSpace('1cm'))
                self.append(LineBreak())
            else:
                self.append(HFill())

            index += 1


class DivisionWorksheet(Worksheet):
    _title = 'Division 1 to 9'
    _instructions = 'Find the quotient.'

    def __init__(self):
        super().__init__()
        self.append(Division.command())

    @staticmethod
    def _problems(r, count):
        m = [(i, j, i*j) for i in r for j in r]
        random.shuffle(m)
        if len(m) > count:
            m = m[:count]
        return m

    def fill_document(self):
        index = 0
        for i, _, k in self._problems(range(1, 10), count=80):
            self.append(Division(arguments=Arguments(k, i)))

            row = int(index / 10) + 1
            column = index % 10 + 1
            if column == 10:
                self.append(VerticalSpace('1cm'))
                self.append(LineBreak())
            else:
                self.append(HFill())

            index += 1


class AdditionWorksheet(Worksheet):
    _title = 'Addition 0 to 10'
    _instructions = 'Find the sum.'

    def __init__(self):
        super().__init__()
        self.append(Addition.command())

    @staticmethod
    def _problems(r, count):
        m = [(i, j, i+j) for i in r for j in r]
        random.shuffle(m)
        if len(m) > count:
            m = m[:count]
        return m

    def fill_document(self):
        index = 0
        for i, j, _ in self._problems(range(0, 11), count=80):
            self.append(Addition(arguments=Arguments(i, j)))

            row = int(index / 10) + 1
            column = index % 10 + 1
            if column == 10:
                self.append(VerticalSpace('1cm'))
                self.append(LineBreak())
            else:
                self.append(HFill())

            index += 1


class SubtractionWorksheet(Worksheet):
    _title = 'Positive Subtraction 0 to 10'
    _instructions = 'Find the difference.'

    def __init__(self):
        super().__init__()
        self.append(Subtraction.command())

    @staticmethod
    def _problems(r, count):
        m = []
        for i in range(count):
            i, j = random.choice(r), random.choice(r)
            if i < j:
                i, j = j, i
            m.append((i, j, i-j))
        random.shuffle(m)
        if len(m) > count:
            m = m[:count]
        return m

    def fill_document(self):
        index = 0
        for i, j, _ in self._problems(range(0, 11), count=80):
            self.append(Subtraction(arguments=Arguments(i, j)))

            row = int(index / 10) + 1
            column = index % 10 + 1
            if column == 10:
                self.append(VerticalSpace('1cm'))
                self.append(LineBreak())
            else:
                self.append(HFill())

            index += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate worksheets for practicing math facts.')
    parser.add_argument('--type', '-t', choices=['multiplication', 'division', 'addition', 'subtraction'],
                        default='multiplication', help='Choose a worksheet type')
    parser.add_argument('--answers', '-a', action='store_true',
                        help='Generate an answer key')
    parser.add_argument('--count', '-c', type=int, default=1,
                        help='Number of worksheets to generate')
    args = parser.parse_args()

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

    for _ in range(args.count):
        ws.fill_document()
        ws.generate_pdf('worksheet', clean_tex=False)
        tex = ws.dumps()
