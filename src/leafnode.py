from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value == None:
            raise ValueError("All leafnodes must have a value error")
        super().__init__(tag= tag, value=value, props=props)
        del self.children

    def __eq__(self, other):
        if isinstance(other, LeafNode):
            return self.__dict__ == other.__dict__
        return False
        
    def to_html(self):
        props_to_html = super().props_to_html()
        if self.tag == None:
            return f"{self.value}"
        else:
            return f'<{self.tag}{props_to_html}>{self.value}</{self.tag}>'