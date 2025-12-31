from htmlnode import HTMLNode
from textnode import TextNode, TextType


def main():
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    html_node = HTMLNode("p", None, "this is a paragraph", {"custom-tag": "true"})

    print(html_node)


if __name__ == '__main__':
    main()

