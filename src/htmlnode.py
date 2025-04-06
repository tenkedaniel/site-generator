class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props_string = ""
        for key in self.props:
            key_string = f" {key}=\"{self.props[key]}\""
            props_string.append(key_string)
        return props_string
            

