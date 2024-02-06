class MyList:
    def __init__(self):
        self.data = []

    def append(self, value):
        self.data.append(value)

    def __len__(self):
        return len(self.data)

    def __eq__(self, other):
        all_elements_equal = True
        for elem in self.data:
            for elem_two in other.data:
                if elem != elem_two:
                    all_elements_equal = False
                    break
        return len(self) == len(other) and all_elements_equal


my_list = MyList()

my_list.append(1)
my_list.append(2)
my_list.append(3)

length = len(my_list)

print("Custom list:", my_list.data)
print("Length of custom list:", length)

my_other_list = MyList()
my_list.append(1)
my_list.append(2)

print("Equal", my_list == my_other_list)
