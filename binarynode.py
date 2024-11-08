class BinaryNode:
    def __init__(self, entry):
        self.entry = entry
        self.left = None
        self.right = None
    
    def __gt__(self, other):
        return self.entry > other.entry
    
    def __lt__(self, other):
        return self.entry < other.entry
    
    def __eq__(self, other):
        return self.entry == other.entry