import textwrap

from markdownsausagemachine.document import SectionContent


class Paragraph(SectionContent):
    def __init__(self, text: str) -> None:
        self.contents = text

    def get_markdown(self) -> str:
        return textwrap.fill(self.contents, width=80, break_long_words=False, tabsize=4)
