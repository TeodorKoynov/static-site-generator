from htmlnode import HTMLNode, LeafNode
from textnode import TextNode, TextType


def main():
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    html_node = HTMLNode("p", None, "this is a paragraph", {"custom-tag": "true"})
    leaf_node = LeafNode("p", "Hello, world!", {"custom-tag": "true"})

    print(leaf_node.to_html())


if __name__ == '__main__':
    main()

