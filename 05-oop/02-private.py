class MyClass:
    def __init__(self, public_attr, private_attr):
        self.public_attr = public_attr
        self.__private_attr = private_attr

    def get_public_attr(self):
        return self.public_attr

    def set_public_attr(self, value):
        self.public_attr = value

    def get_private_attr(self):
        return self.__private_attr

    def set_private_attr(self, value):
        self.__private_attr = value

    def __private_method(self):
        return "This is a private method."

    def public_method(self):
        return f"Public attribute: {self.public_attr}\nPrivate attribute: {self.__private_attr}\n{self.__private_method()}"


my_instance = MyClass("PublicValue", "PrivateValue")

print("Public old:", my_instance.public_attr)
my_instance.set_public_attr("NewPublicValue")
print("Public new:", my_instance.public_attr)

print("Private old:", my_instance.get_private_attr())
my_instance.set_private_attr("NewPrivateValue")
print("Private new:", my_instance.get_private_attr())
