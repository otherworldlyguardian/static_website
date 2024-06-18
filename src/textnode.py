class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, comparer):
        if (
            self.text == comparer.text
            and self.text_type == comparer.text_type
            and self.url == comparer.url
        ):
            return True
        else:
            return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"