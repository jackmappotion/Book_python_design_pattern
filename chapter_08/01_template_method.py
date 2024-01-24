from abc import ABCMeta, abstractmethod


class Compiler(metaclass=ABCMeta):
    """
    템플릿 메소드를 정의하는 클래스
    """

    @abstractmethod
    def collectSource(self):
        pass

    @abstractmethod
    def compileToObject(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def compileAndRun(self):
        self.collectSource()
        self.compileToObject()
        self.run()


class iOSCompiler(Compiler):
    """
    템플릿 메소드를 구현하는 클래스
    """

    def collectSource(self):
        print("Collecting Swift Source Code")

    def compileToObject(self):
        print("Compiling Swift code to LLVM bitcode")

    def run(self):
        print("Program runing on runtime environment")


if __name__ == "__main__":
    ios = iOSCompiler()
    ios.compileAndRun()
