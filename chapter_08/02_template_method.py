from abc import ABCMeta, abstractmethod

class AbstractClass(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass

    def template_method(self):
        self.operation1()
        self.operation2()

class ConcreateClass(AbstractClass):
    def __init__(self):
        pass

    def operation1(self):
        print("operation1")

    def operation2(self):
        print("operation2")

class Client:
    def main(self):
        concreate_class = ConcreateClass()
        concreate_class.template_method()

client = Client()
client.main()
