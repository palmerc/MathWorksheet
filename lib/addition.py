import random

from pylatex import Tabularx, Command
from pylatex.base_classes import Arguments
from pylatex.basic import LineBreak, NewLine
from pylatex.position import VerticalSpace
from pylatex.utils import NoEscape

from .math_commands import Addition, AdditionAnswer
from .worksheet import Worksheet


class AdditionWorksheet(Worksheet):
    _instructions = 'Find the sum.'

    def __init__(self, range, rows=5, columns=6, answers=False):
        self._title = f'Addition {range.start} to {range.stop}'
        self._range = range
        self._rows = rows
        self._columns = columns
        self._show_answers = answers

        super().__init__()
        self.append(Command('LARGE'))
        if self._show_answers:
            self.append(AdditionAnswer.command())
        else:
            self.append(Addition.command())

    @staticmethod
    def _problems(r, count):
        problems = []
        for n in range(count):
            i = random.randint(r.start, r.stop)
            j = random.randint(r.start, r.stop)
            k = i + j
            problems.append((i, j, k))
        return problems

    def fill_document(self):
        problems = self._rows * self._columns

        index = 0
        row = []
        for i, j, k in self._problems(self._range, count=problems):
            if len(str(i)) < len(str(j)):
                i, j = j, i
            if self._show_answers:
                add = AdditionAnswer(arguments=Arguments(i, j, k))
            else:
                add = Addition(arguments=Arguments(i, j))
            row.append(add)
            index += 1

            column_number = index % self._columns
            row_number = abs(index / self._columns)
            if column_number == 0 and index > 0:
                with self.create(Tabularx(self._columns * 'X', width_argument=NoEscape(r'\linewidth'))) as tx:
                    tx.add_row(row)
                if row_number < self._rows:
                    self.extend([LineBreak(), VerticalSpace('2cm'), NewLine()])
                row = []
