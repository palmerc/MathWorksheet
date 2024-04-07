from pylatex.base_classes import Arguments
from pylatex.basic import HFill, LineBreak
from pylatex.position import VerticalSpace

from .math_commands import Multiplication
from .worksheet import Worksheet

import random


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

            column = index % 10 + 1
            if column == 10:
                self.append(VerticalSpace('1cm'))
                self.append(LineBreak())
            else:
                self.append(HFill())

            index += 1
