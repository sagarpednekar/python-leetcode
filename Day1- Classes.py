class Node:
    def __init__(self, color):
        self.color = color

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color


blue_node = Node('green')

print('First Node is ',blue_node.get_color().upper())   


