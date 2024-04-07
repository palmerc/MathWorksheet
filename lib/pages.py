from pylatex import Document, Package, Command, NoEscape


class Pages(Document):
    def __init__(self, pages):
        super().__init__(indent=False, geometry_options={'lmargin': '2cm', 'rmargin': '2cm'})
        self.change_document_style('empty') # No page number please
        self.packages.append(Package('pdfpages'))

        for page in pages:
            self.append(Command('includepdf', options=NoEscape('pages=-'), arguments=NoEscape(page.as_posix())))
