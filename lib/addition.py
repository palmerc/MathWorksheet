from pylatex.base_classes import Arguments
from pylatex.basic import HFill, LineBreak
from pylatex.position import VerticalSpace

from .math_commands import Addition
from .worksheet import Worksheet

import random


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

            column = index % 10 + 1
            if column == 10:
                self.append(VerticalSpace('1cm'))
                self.append(LineBreak())
            else:
                self.append(HFill())

            index += 1
