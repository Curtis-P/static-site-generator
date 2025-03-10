from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag == None:
            raise ValueError("Parent nodes must have a tag")
        if children == None:
            raise ValueError("Parent nodes must have children")
        super().__init__(tag=tag,children=children, props=props)
        del self.value

    def to_html(self):        
        retstring = f'<{self.tag}{super().props_to_html()}>'
        for childnode in self.children:
            retstring = retstring + childnode.to_html()
        retstring = retstring + f'</{self.tag}>'
        return retstring