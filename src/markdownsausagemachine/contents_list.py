import textwrap
from collections.abc import Collection

from markdownsausagemachine.document import SectionContent


class UnorderedList(SectionContent):
    def __init__(self, items: Collection[str]) -> None:
        self.items = items

    def get_markdown(self) -> str:
        markdown = ""
        for i, item in enumerate(self.items):
            wrapped_item = textwrap.fill(
                item,
                width=78,
                break_long_words=False,
                tabsize=4,
                subsequent_indent="  ",
            )
            markdown += f"* {wrapped_item}"
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
            wrapped_item = textwrap.fill(
                item,
                width=78,
                break_long_words=False,
                tabsize=4,
                subsequent_indent="  ",
            )
            markdown += f"{i+1}. {wrapped_item}"
            # Add some separation between items
            if i != len(self.items) - 1:
                markdown += "\n"
        return markdown
