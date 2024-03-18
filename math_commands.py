from pylatex import UnsafeCommand
from pylatex.base_classes import CommandBase
from pylatex.package import Package


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


class Addition(CommandBase):
    _latex_name = 'addi'

    _latex = r'''
    $\begin{array}{rr}
     & #1 \\
     + & #2 \\ \hline
     \end{array}$
    '''

    @classmethod
    def command(cls):
        return UnsafeCommand('newcommand', f'\\{cls._latex_name}', options=2, extra_arguments=cls._latex)


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

    _latex = r'''
    $#1 \: \begin{array}{|l}
     \hline #2
     \end{array}$    
    '''

    @classmethod
    def command(cls):
        return UnsafeCommand('newcommand', f'\\{cls._latex_name}', options=2, extra_arguments=cls._latex)