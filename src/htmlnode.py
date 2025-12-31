class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return ""

        html_props = []
        for (name, value) in self.props.items():
            html_prop = f' {name}="{value}"'
            html_props.append(html_prop)

        return "".join(html_props)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

    # def to_html_example(self):
    #     def create_tag(tag, html_props, children, value):
    #         value = f' value="{value}"' if value else ""
    #         children = f"{children}" if children else ""
    #
    #         if tag is None:
    #             return ""
    #         return f"<{self.tag}{html_props}{value}>{children}</{self.tag}>"
    #
    #     return create_tag(self.tag, self.props_to_html(), self.children, self.value)