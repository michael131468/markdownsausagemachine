from collections.abc import Collection

from markdownsausagemachine.contents_paragraph import Paragraph
from markdownsausagemachine.document import SectionContent


class UnorderedList(SectionContent):
    def __init__(self, items: Collection[str]) -> None:
        self.items = items

    def get_markdown(self) -> str:
        markdown = ""
        for i, item in enumerate(self.items):
            if isinstance(item, str):
                item = Paragraph(item)
                item.initial_indent = f"*   "
                item.subsequent_indent = f"{' '*len(item.initial_indent)}"
                markdown += item.get_markdown()
            else:
                raise ValueError(f"Unsupported list item type: {type(item)}")
            # Add some separation between items
            if i != len(self.items) - 1:
                markdown += "\n"
        return markdown


class OrderedList(SectionContent):
    def __init__(self, items: Collection[str]) -> None:
        self.items = items

    def get_markdown(self) -> str:
        markdown = ""
        for i, item in enumerate(self.items):
            if isinstance(item, str):
                item = Paragraph(item)
                item.initial_indent = f"{i+1}.  "
                item.subsequent_indent = f"{' '*len(item.initial_indent)}"
                markdown += item.get_markdown()
            else:
                raise ValueError(f"Unsupported list item type: {type(item)}")
            # Add some separation between items
            if i != len(self.items) - 1:
                markdown += "\n"
        return markdown
