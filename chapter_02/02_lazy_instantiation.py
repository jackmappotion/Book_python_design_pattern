class Singleton:
    __instance = None

    def __init__(self) -> None:
        if not Singleton.__instance:
            print("__init__ method called")
        else:
            print("Instance already created: ", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s = Singleton() ## 클래스를 생성하면서 __init__ 메소드가 호출됨 / 클래스를 초기화 했지만 객체는 생성하지 않음
print("Object created: ", Singleton.getInstance()) ## 객체를 생성
s1 = Singleton() ## 객체가 이미 생성
