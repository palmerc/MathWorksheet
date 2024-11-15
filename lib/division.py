from pylatex.base_classes import Arguments
from pylatex.basic import HFill, LineBreak
from pylatex.position import VerticalSpace

from .math_commands import Division
from .worksheet import Worksheet

import random


class LongDivisionWorksheet(Worksheet):
    _title = 'Long Division'
    _instructions = 'Find the quotient.'

    def __init__(self):
        super().__init__()
        self.append(Division.command())

    @staticmethod
    def _problems(r, count):
        m = [(i, j, k, i*j*k) for i in r for j in r for k in r if i*j*k >= 100 and i*j*k < 1000]
        random.shuffle(m)
        if len(m) > count:
            m = m[:count]
        return m

    def fill_document(self):
        index = 0
        for i, _, _, l in self._problems(range(1, 10), count=80):
            self.append(Division(arguments=Arguments(l, i)))

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
