class vehicle:
    def start(self):
        print("Vehicle started")
    def stop(self):
        print("vehicle stopped")
class car(vehicle):
    def start(self):
        print("car started")
    def stop(self):
        print("car stopped")
class motorcycle(vehicle):
    def start(self):
        print("motorcycle started")
    def stop(self):
        print("motorcycle stopeed")

car1 = car()
car1.start()
car1.stop()
bike1 = motorcycle()
bike1.start()
bike1.stop()
