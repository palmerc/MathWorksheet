from pylatex.base_classes import Arguments
from pylatex.basic import HFill, LineBreak
from pylatex.position import VerticalSpace

from .math_commands import Subtraction
from .worksheet import Worksheet

import random


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

            column = index % 10 + 1
            if column == 10:
                self.append(VerticalSpace('1cm'))
                self.append(LineBreak())
            else:
                self.append(HFill())

            index += 1
