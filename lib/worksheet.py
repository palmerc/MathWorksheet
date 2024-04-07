from pylatex import Document
from pylatex.base_classes import Command, Environment
from pylatex.basic import HFill, NewLine
from pylatex.package import Package
from pylatex.position import VerticalSpace, HorizontalSpace, Center


class Framed(Environment):
    packages = [Package('framed')]


class Worksheet(Document):
    _title = None
    _instructions = None

    def __init__(self):
        super().__init__(indent=False, geometry_options={'lmargin': '2cm', 'rmargin': '2cm'})
        self.change_document_style('empty') # No page number please
        self._add_header()

    def _add_header(self):
        with self.create(Framed()) as e:
            with e.create(Center()) as f:
                f.append(Command('LARGE'))
                f.append(Command('textbf', self._title))

        self.append(VerticalSpace('.5cm'))

        self.extend(['Name:', Command('underline', HorizontalSpace('4cm')), HFill()])
        self.extend(['Date:', Command('underline', HorizontalSpace('4cm')), HFill()])
        self.extend(['Score:', Command('underline', HorizontalSpace('1cm')), '/100'])
        self.append(NewLine())

        with self.create(Center()) as e:
            e.append(self._instructions)