class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = [] if children is None or not isinstance(children, list)else children
        self.props = {} if props is None or not isinstance(props, dict) else props
    
    def __repr__(self):
        return f"Tag:{self.tag}, Value:{self.value}, Children:{self.children}, Props:{self.props}"
        pass

    def to_html(self):
        #raise NotImplementedError
        if self.tag is None:
            return self.value or ""

        attributes_html = ""
        if self.props:
            for attr, value in self.props.items():
                attributes_html += f' {attr}="{value}"'

        if self.children:
            children_html = ""
            for child in self.children:
                children_html += child.to_html()
            return f"<{self.tag}{attributes_html}>{children_html}</{self.tag}>"
        else:
            # Handle leaf nodes that might have a value
            return f"<{self.tag}{attributes_html}>{self.value or ''}</{self.tag}>"
            pass
        
    def props_to_html(self):
        retstring = ''
        for key, value in self.props.items():
            retstring = retstring +" "+ key + "=" + f'"{value}"'
        return retstring
        pass
    