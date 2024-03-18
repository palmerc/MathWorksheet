#!/usr/bin/env python3

from pylatex import Document
from pylatex.base_classes import Arguments, Command, Environment
from pylatex.basic import HFill, LineBreak, NewLine
from pylatex.package import Package
from pylatex.position import VerticalSpace, HorizontalSpace, Center
from math_commands import Multiplication
import random


class Framed(Environment):
    packages = [Package('framed')]


class Worksheet(Document):
    _title = None
    _instructions = None

    def __init__(self):
        super().__init__(indent=False, geometry_options={'lmargin': '2cm', 'rmargin': '2cm'})
        self.change_document_style('empty') # No page number please

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


if __name__ == '__main__':
    ws = MultiplicationWorksheet()
    ws.fill_document()

    ws.generate_pdf('worksheet', clean_tex=False)
    tex = ws.dumps()  # The document as string in LaTeX syntax
