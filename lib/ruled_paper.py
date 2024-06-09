import math

from pylatex import NoEscape

from .worksheet import Worksheet
from .math_commands import DashedLine, RuledPaper


class RuledPaperWorksheet(Worksheet):
    def __init__(self):
        super().__init__(skip_header=True)

        definitions = r'''
\newlength\letterheight
\setlength\letterheight{1.2cm}
\def\midpitch{.5}
\def\bottompitch{.3}
\def\toplinethickness{1pt}
\def\baselinethickness{2pt}
\parskip 1cm

\def\stacktype{L}\def\stackalignment{l}
%From morsburg at http://tex.stackexchange.com/questions/12537/
%how-can-i-make-a-horizontal-dashed-line/12553#12553
\def\dashfill{\cleaders\hbox to .6em{-}\hfill}

\def\tophline{\textcolor{Red}{\rule{\textwidth}{\toplinethickness}}}
\def\bottomhline{\textcolor{Black}{\rule{\textwidth}{\baselinethickness}}}
        '''
        self.preamble.append(NoEscape(definitions))
        self.preamble.append(DashedLine.command())
        self.preamble.append(RuledPaper.command())

    def fill_document(self):
        # This math is dubious: Height of A4 minus top and bottom margin divided by the height of a "row"
        count = math.floor((29.7 - 3) / 2.2)
        for _ in range(0, count):
            self.extend([RuledPaper(), NoEscape('\n')])

