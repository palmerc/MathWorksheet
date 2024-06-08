import random

from pylatex import Tabularx, Command
from pylatex.base_classes import Arguments
from pylatex.basic import LineBreak, NewLine, NewPage
from pylatex.position import VerticalSpace
from pylatex.utils import NoEscape

from .math_commands import Clock
from .worksheet import Worksheet


class ClocksWorksheet(Worksheet):
    _instructions = 'Find the time.'

    def __init__(self, rows=3, columns=2, answers=False):
        self._title = f'Clocks'
        self._rows = rows
        self._columns = columns
        self._show_answers = answers

        super().__init__()
        self.append(Clock.command())

    @staticmethod
    def _problems(count):
        problems = []
        for n in range(count):
            minute = random.randint(0, 12) * 5
            hour = random.randint(0, 12)
            problems.append((hour, minute))
        return problems

    def fill_document(self):
        problem_count = self._rows * self._columns

        index = 0
        row = []
        for hour, minute in self._problems(problem_count):
            clock = Clock(arguments=Arguments(hour, minute), options=0.7)
            row.append(clock)
            index += 1

            column_number = index % self._columns
            row_number = abs(index / self._columns)
            if column_number == 0 and index > 0:
                with self.create(Tabularx(self._columns * 'X', width_argument=NoEscape(r'\linewidth'))) as tx:
                    tx.add_row(row)
                if row_number < self._rows:
                    self.extend([LineBreak(), VerticalSpace('2cm'), NewLine()])
                row = []
