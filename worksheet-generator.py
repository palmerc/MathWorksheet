import random
import pylatex


class Template(object):
    def __init__(self):
        with open('tex-docs/preamble.tex', 'r') as f:
            self._preamble = f.read()
        with open('tex-docs/commands.tex', 'r') as f:
            self._commands = f.read()
        with open('tex-docs/formatting.tex', 'r') as f:
            self._formatting = f.read()
        with open('tex-docs/content.tex', 'r') as f:
            self._content = f.read()


class Worksheet(Template):
    def __init__(self):
        super().__init__()

        self._rows = 10
        self._columns = 10

    def _row_command(self):
        problem_width = 1.0 / self._columns

        minipages = []
        for row in range(self._columns):
            minipages += [f'\\begin{{minipage}}[t]{{{problem_width}\\textwidth}}\\itm #{row + 1} \\end{{minipage}}']
        minipages_inner = ' \hfill\n '.join(minipages)
        return f'''
%---------CUSTOM-COMMANDS-------------------------------------------%%
\\newcommand{{\multiprobs}}[{self._columns}]{{
{minipages_inner}
}} % Fits {self._columns} problems on a line
%-------------------------------------------------------------------%%

'''

    def _multiplication(self, a, b):
        return f'\\mult{{{a}}}{{{b}}}'

    def _problems(self):
        m = []
        for i in range(1, 10):
            m += [(i, j, i * j) for j in range(1, 10)]
        random.shuffle(m)
        return m

    def display_multiplication(self):
        problems_inner = []
        index = 0
        m = []
        for i, j, k in self._problems():
            m += [f'{self._multiplication(i, j)}']

            row = int(index / 10) + 1
            column = index % 10 + 1
            if column == 10:
                problems_inner += [' \\hfill '.join(m)]
                m.clear()
                problems_inner += ['\n\\vspace{1cm}\n']
            if row >= self._rows:
                m.clear()
                break
            index += 1
        print(index)
        problems_inner += [' \\hfill '.join(m)]
        return '\n'.join(problems_inner)

    def latex(self):
        w = self._preamble + \
            self._commands + \
            self._formatting + \
            self._content.format(problems=self.display_multiplication())
        return w


if __name__ == '__main__':
    w = Worksheet()
    l = w.latex()

    with open('output.tex', 'w') as f:
        f.write(l)
