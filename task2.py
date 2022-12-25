from time import sleep


class TrafficMetaClass(type):
    a = None

    def __call__(cls, *args, **kwargs):
        if cls.a is None:
            cls.a = super(TrafficMetaClass, cls).__call__(*args, **kwargs)
        return cls.a


class TrafficLight(metaclass=TrafficMetaClass):

    def __init__(self):
        self.__color = None

    def running(self):
        while True:
            self.__color = "red"
            print(self.__color)
            sleep(7)
            self.__color = "yellow"
            print(self.__color)
            sleep(2)
            self.__color = "green"
            print(self.__color)
            sleep(5)


t1 = TrafficLight()
t2 = TrafficLight()
print(f"t1 is t2 = {t1 is t2}")
