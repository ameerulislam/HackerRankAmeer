class CategoryTree:

    def __init__(self):
        self.childlist = []

    
    def add_category(self, category, parent):
        self.category = category
        self.parent = parent
        

        if (parent != None):
            self.childlist.append([parent, category])
            

    def get_children(self, parent):
        self.parent = parent
        self.anotherchildlist =[]
        for i in self.childlist:
            if i[0]==self.parent:
                self.anotherchildlist.append(i[1])

        return self.anotherchildlist

if __name__ == "__main__":
    c = CategoryTree()
    c.add_category('A', None)
    c.add_category('B', 'A')
    c.add_category('C', 'A')
    print(','.join(c.get_children('B') or ['nothing']))

# =======================

# def find_max_sum(numbers):
#     a = max(numbers)
#     numbers.remove(a)
#     b = max(numbers)
#     return a+b
    
# if __name__ == "__main__":
#     print(find_max_sum([5, 9, 7, 11]))