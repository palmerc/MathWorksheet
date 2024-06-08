from pylatex import Document
from pylatex.base_classes import Command, Environment
from pylatex.basic import HFill, LineBreak
from pylatex.package import Package
from pylatex.position import HorizontalSpace, Center


class Framed(Environment):
    packages = [Package('framed'), Package('extsizes'), Package('tikz'), Package('amsmath')]


class Worksheet(Document):
    _title = None
    _instructions = None

    def __init__(self):
        super().__init__(indent=False,
                         documentclass='extarticle', document_options=['12pt'])
        self.preamble.append(Package('geometry', options=['a4paper', 'margin=1cm']))
        self.preamble.append(Package('xcolor', options=['dvipsnames']))
        self.preamble.append(Command('usetikzlibrary', 'arrows.meta'))
        self.change_document_style('empty') # No page number please
        self._add_header()

    def _add_header(self):
        with self.create(Framed()) as e:
            with e.create(Center()) as f:
                f.append(Command('LARGE'))
                f.append(Command('textbf', self._title))

        self.extend(['Name:', Command('underline', HorizontalSpace('4cm')), HFill()])
        self.extend(['Date:', Command('underline', HorizontalSpace('4cm')), HFill()])
        self.extend(['Score:', Command('underline', HorizontalSpace('1cm')), '/100'])
        with self.create(Center()) as e:
            e.append(self._instructions)
            e.append(LineBreak())