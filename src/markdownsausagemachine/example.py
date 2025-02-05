#!/usr/bin/env python3

import logging
from pathlib import Path
from typing import Any

from markdownsausagemachine.contents import OrderedList, Paragraph, UnorderedList
from markdownsausagemachine.sausage_machine import SausageMachine
from markdownsausagemachine.sausage_man import IngredientPromise, SausageMan

logger = logging.getLogger(__name__)
logging.basicConfig(encoding="utf-8", level=logging.DEBUG)


def generate_example_one() -> None:
    logger.info("Generating example1...")

    my_sausage_machine = SausageMachine()
    index_doc = my_sausage_machine.add_document("index")
    index_doc.set_header("Index")
    new_section = index_doc.add_section("my-sausage-machine")
    new_section.set_header("My Sausage Machine")
    new_section.add_content(
        Paragraph("P1: How does a sausage machine become a reality")
    )
    new_section.add_content(
        Paragraph("P2: Going back to the start (a brief history of the world)")
    )
    new_section.add_content(
        UnorderedList(["A brief intro", "A confusing middle", "A well deserved end"])
    )
    new_section.add_content(Paragraph("P3: An ordered history of the world"))
    new_section.add_content(
        OrderedList(["A brief intro", "A confusing middle", "A well deserved end"])
    )

    supp_doc = my_sausage_machine.add_document("supplementary-words")
    supp_doc.set_header("Supplementary Words")
    new_section = supp_doc.add_section("my-sausage-machine")
    new_section.add_content(
        Paragraph("P1: Cat Dog Sheep\n\nDog Sheep Cat\n\nSheep Dog Cat")
    )
    new_section.add_content(Paragraph("P2: Up Down Left Right"))
    new_section.add_content(Paragraph("P3: Music Dance Sunshine"))

    output_dir = Path("./example1/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    my_sausage_machine.output_markdown_documents(output_dir)
    logger.info("Done! Output created in: %s", output_dir)


def generate_example_two() -> None:
    example_mystery_meat = {
        "schema": "0.1",
        "documents": {
            "index": {
                "header": "Top-Level Header (Index)",
                "lede": "The root of the problems.",
                "sections": [
                    {
                        "header": "A Section Header",
                        "contents": [
                            {
                                "type": "paragraph",
                                "text": [
                                    "This is a standard paragraph section.",
                                    "Multiple lines can be passed in as an array.",
                                    "Allowing nicely formatted mystery meat.",
                                ],
                            },
                            {
                                "type": "unordered_list",
                                "items": [
                                    "Item 1: Hotdog",
                                    "Item 2: Cabbage",
                                    "Item 3: Broccoli",
                                ],
                            },
                            {
                                "type": "subsection",
                                "header": "A subsection",
                                "contents": [
                                    {
                                        "type": "paragraph",
                                        "text": ["A paragraph in a subsection."],
                                    }
                                ],
                            },
                        ],
                    }
                ],
            },
            "supplementary": {
                "header": "Top-Level Header (Supp)",
                "lede": "Additional problems.",
                "sections": [
                    {
                        "header": "A Section Header",
                        "contents": [
                            {
                                "type": "paragraph",
                                "text": [
                                    "This is a standard paragraph section.",
                                ],
                            },
                            {
                                "type": "ordered_list",
                                "items": [
                                    "Item 1: Random",
                                    "Item 2: Items",
                                    "Item 3: Are not hotdogs",
                                ],
                            },
                        ],
                    }
                ],
            },
        },
    }

    promises: list[IngredientPromise] = []

    my_sausage_man = SausageMan()
    my_sausage_man.give_ingredients(example_mystery_meat)
    my_sausage_man.give_promises(promises)
    promises_met = my_sausage_man.check_promises()
    if not promises_met:
        logger.error("Not all required promises were kept. Ingredients are not good!")

    output_dir = Path("./example2/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    my_sausage_man.get_markdown_files(output_dir)
    logger.info("Done! Output created in: %s", output_dir)


def show_unmet_promise() -> None:
    example_mystery_meat = {
        "schema": "0.1",
        "documents": {
            "index": {
                "header": "Top-Level Header (Main)",
                "lede": "The root of the problems.",
                "sections": [
                    {
                        "header": "Meats",
                        "contents": [
                            {
                                "type": "paragraph",
                                "text": [
                                    "A small paragraph about meats.",
                                ],
                            },
                        ],
                    },
                    {
                        "header": "Salads",
                        "contents": [
                            {
                                "type": "paragraph",
                                "text": [
                                    "A small paragraph about salads.",
                                ],
                            },
                            {
                                "type": "ordered_list",
                                "items": [
                                    "Item 1: Random",
                                    "Item 2: Items",
                                    "Item 3: Are not hotdogs",
                                ],
                            },
                        ],
                    },
                    {
                        "header": "Vegetables",
                        "contents": [
                            {
                                "type": "paragraph",
                                "text": [
                                    "A small paragraph about vegetables.",
                                ],
                            },
                            {
                                "type": "ordered_list",
                                "items": [
                                    "Item 1: Random",
                                    "Item 2: Items",
                                    "Item 3: Are not hotdogs",
                                ],
                            },
                        ],
                    },
                ],
            },
        },
    }

    def check_has_index_doc(ingredients: dict[str, Any]) -> bool:
        """Return True if promise met else False"""
        documents = ingredients.get("documents", {})
        return "index" in documents

    def check_index_doc_has_list_of_salads(ingredients: dict[str, Any]) -> bool:
        """Return True if promise met else False"""
        if not check_has_index_doc(ingredients):
            return False

        documents = ingredients.get("documents", {})
        index_doc = documents.get("index")
        for section in index_doc.get("sections", []):
            header = section.get("header")
            contents = section.get("contents", [])
            if header == "Salads":
                for content in contents:
                    if content.get("type") == "ordered_list":
                        return True

        return False

    def check_index_doc_has_list_of_meats(ingredients: dict[str, Any]) -> bool:
        """Return True if promise met else False"""
        if not check_has_index_doc(ingredients):
            return False

        documents = ingredients.get("documents", {})
        index_doc = documents.get("index")
        for section in index_doc.get("sections", []):
            header = section.get("header")
            contents = section.get("contents", [])
            if header == "Meats":
                for content in contents:
                    if content.get("type") == "ordered_list":
                        return True

        return False

    promises = [
        IngredientPromise("An index document is present.", check_has_index_doc),
        IngredientPromise(
            "Index document has list of salads.", check_index_doc_has_list_of_salads
        ),
        IngredientPromise(
            "Index document has list of meats.", check_index_doc_has_list_of_meats
        ),
    ]

    my_sausage_man = SausageMan()
    my_sausage_man.give_ingredients(example_mystery_meat)
    my_sausage_man.give_promises(promises)
    promises_met = my_sausage_man.check_promises()
    if not promises_met:
        logger.error("Not all required promises were kept. Ingredients are not good!")


if __name__ == "__main__":
    generate_example_one()
    generate_example_two()
    show_unmet_promise()
