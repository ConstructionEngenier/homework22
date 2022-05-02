from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Boat(Transport):
    def start_engine(self):
        print("Катер громко затарахтел")

    def stop_engine(self):
        print("Двигатель катера чихнул напоследок и заглох")

    def move(self):
        print("Катер быстро набирает скорость")

    def stop(self):
        print("Катер остановился")


class Car(Transport):
    def start_engine(self):
        print("Машина заурчала двигателем")

    def stop_engine(self):
        print("Машина стоит с заглушенным двигателем")

    def move(self):
        print("Машина едет к цели назначения")

    def stop(self):
        print("Машина остановилась")


class Electroscooter(Transport):
    def start_engine(self):
        print("Светодиоды электроскутера загорелись")

    def stop_engine(self):
        print("Светодиоды электроскутера погасли")

    def move(self):
        print("Электроскутер начал движение")

    def stop(self):
        print("Электроскутер остановился")


class Person():
    def use_transport(self, transport: Transport):
        transport.start_engine()
        transport.stop_engine()
        transport.move()
        transport.stop()


if __name__ == '__main__':
    boat = Boat()
    car = Car()
    kamikadze = Electroscooter()

    person = Person()
    person.use_transport(boat)
    print('=' * 10)
    person.use_transport(car)
    print('=' * 10)
    person.use_transport(kamikadze)
