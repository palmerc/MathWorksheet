from pylatex import UnsafeCommand
from pylatex.base_classes import CommandBase, SpecialOptions
from pylatex.package import Package
from pylatex.tikz import TikZ


class Multiplication(CommandBase):
    _latex_name = 'mult'

    packages = [Package('xcolor')]

    _latex = r'''
    $\begin{array}{rr}
     & #1 \\
     \times & #2 \\ \hline
     \end{array}$
     '''

    @classmethod
    def command(cls):
        return UnsafeCommand('newcommand', f'\\{cls._latex_name}', options=2, extra_arguments=cls._latex)


class AdditionAnswer(CommandBase):
    _latex_name = 'AdditionAnswer'

    _latex = r'''
    $\begin{array}{rrr}
       & #1 \\
     + & #2 \\ 
     \hline%
       & \textcolor{red}{#3}
     \end{array}$
    '''

    @classmethod
    def command(cls):
        return UnsafeCommand('newcommand', f'\\{cls._latex_name}',
                             options=3,
                             extra_arguments=cls._latex)


class Addition(CommandBase):
    _latex_name = 'Addition'

    _latex = r'''
    $\begin{array}{rr}
       & #1 \\
     + & #2 \\
     \hline \\
     \end{array}$
    '''

    @classmethod
    def command(cls):
        return UnsafeCommand('newcommand', f'\\{cls._latex_name}',
                             options=2,
                             extra_arguments=cls._latex)


class Subtraction(CommandBase):
    _latex_name = 'subt'

    _latex = r'''
    $\begin{array}{rr}
     & #1 \\
     - & #2 \\ \hline
     \end{array}$    
    '''

    @classmethod
    def command(cls):
        return UnsafeCommand('newcommand', f'\\{cls._latex_name}', options=2, extra_arguments=cls._latex)


class Division(CommandBase):
    _latex_name = 'divi'

    packages = [Package('xcolor')]

    _latex = r'''
       $\begin{array}{rr}
        & #1 \\
        \div & #2 \\ \hline
        \end{array}$
        '''

    @classmethod
    def command(cls):
        return UnsafeCommand('newcommand', f'\\{cls._latex_name}', options=2, extra_arguments=cls._latex)


class Clock(CommandBase):
    _latex_name = 'clock'

    _latex = r'''
\begin{tikzpicture}[scale=#1,line cap=line width=#1*3pt]
  \filldraw [fill=White!20] (0,0) circle (3.6cm);
  \filldraw [fill=White!20] (0,0) circle (2.8cm);
    
  \foreach \angle / \label in {0/3, 90/12, 180/9, 270/6} {
    \draw [line width = #1*1.8pt] (\angle:2.5cm) -- (\angle:2.8cm);
    \draw (\angle:3.2cm) node[scale=#1]{\Huge $\boldsymbol{\label}$};
  };

  \foreach \angle / \label in {30/2, 60/1, 120/11, 150/10, 210/8, 240/7, 330/4, 300/5} {
    \draw [line width = #1*1.8pt] (\angle:2.5cm) -- (\angle:2.8cm);
    \draw (\angle:3.2cm) node[scale=#1]{\Large $\boldsymbol{\label}$};
  };

  \foreach \x in {0,6,...,360} {
    \draw [line width = #1*1pt] (\x:2.6cm) -- (\x:2.8cm);
  };

  \draw[rotate=90, arrows = -{Latex[length=#1*5mm]}, line width=#1*3pt, line cap=round] (0,0) -- (-#2*30-#3*30/60:2cm); % hours
  \draw[rotate=90, arrows = -{Latex[length=#1*5mm]}, line width=#1*2pt, line cap=round] (0,0) -- (-#3*6:2.5cm); % minutes
  \filldraw (0,0) circle (1mm);
  %
\end{tikzpicture}%
'''

    @classmethod
    def command(cls):
        return UnsafeCommand('newcommand', arguments=f'\\{cls._latex_name}',
                             options=SpecialOptions(3, 2), extra_arguments=cls._latex)


class DashedLine(CommandBase):
    _latex_name = 'dashedline'
    _latex = r'''
  \abovebaseline[-2pt]{\hbox to #1{\dashfill\hfil}}
'''
    @classmethod
    def command(cls):
        return UnsafeCommand('newcommand',
                             arguments=f'\\{cls._latex_name}',
                             options=1,
                             extra_arguments=cls._latex)

class RuledPaper(CommandBase):
    _latex_name = 'blankrow'

    packages = [Package('stackengine', options='usestackEOL'), Package('scalerel')]

    _latex = r'''
  \setstackgap{L}{\the\letterheight}%
  \stackon[\midpitch\letterheight]{%
  \stackon{\smash{\stackunder[\bottompitch\letterheight]{\bottomhline}%
    {\dashedline{\textwidth}}}}{\tophline}}{\dashedline{\textwidth}}%
'''

    @classmethod
    def command(cls):
        return UnsafeCommand('newcommand',
                             arguments=f'\\{cls._latex_name}',
                             extra_arguments=cls._latex)


# clasxxs Division(CommandBase):
#     _latex_name = 'divi'
#
#     _latex = r'''
#     $#1 \: \begin{array}{|l}
#      \hline #2
#      \end{array}$
#     '''
#
#     @classmethod
#     def command(cls):
#         return UnsafeCommand('newcommand', f'\\{cls._latex_name}', options=2, extra_arguments=cls._latex)
