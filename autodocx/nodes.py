class Node():
    def __init__(self, type, value, consumed):
        self.type = type
        self.value = value
        self.consumed = consumed

    def __str__(self):
        return(f"<type: {self.type}, value: {self.value}, Consumed: {self.consumed}>")


class nullNode():
    def __init__(self):
        self.type = None
        self.consumed = 1

    def __str__(self):
        return(f"<type: {self.type}, value: {self.value}, Consumed: {self.consumed}>")


class BodyNode():
    def __init__(self, paragraphs, consumed):
        self.paragraphs = paragraphs
        self.consumed = consumed

    def __str__(self):
        return(f"<Paragprphs: {str(self.paragraphs)}, Consumed: {self.consumed}>")


class ParagraphNode():
    def __init__(self, sentences, consumed):
        self.sentences = sentences
        self.consumed = consumed

    def __str__(self):
        return(f"<sentences: {str(self.sentences)}, Consumed: {self.consumed}>")


class ListNode():
    def __init__(self, sentences, consumed):
        self.sentences = sentences
        self.consumed = consumed

    def __str__(self):
        return(f"<sentences: {str(self.sentences)}, Consumed: {self.consumed}>")


class CodeNode():
    def __init__(self, sentences, consumed):
        self.sentences = sentences
        self.consumed = consumed

    def __str__(self):
        return(f"<sentences: {str(self.sentences)}, Consumed: {self.consumed}>")


class HeadNode():
    def __init__(self, type, value, consumed):
        self.type = type
        self.value = value
        self.consumed = consumed

    def __str__(self):
        return(f"<type: {self.type}, value: {self.value}, Consumed: {self.consumed}>")
