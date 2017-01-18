from PIL import Image
import time
import os


class Laptop:

    def __init__(self):
        self.is_power_on = False
        self.__memory_usage = 0.0
        self.__battery_level = 0.0
        self.__cpu_temp = 0

    def gen_load_msg(self):
        for i in range(4):
            time.sleep(0.5)
            yield "Loading" + "." * i
        time.sleep(0.5)
        yield "\nWelcome!"

    def gen_shutdown_msg(self):
        for i in range(4):
            time.sleep(0.5)
            yield "Shutdown" + "." * i
        time.sleep(0.5)
        yield "\nGoodbye!"

    def turn_on(self):
        if not self.is_power_on:
            self.__is_power_on = True
            self.__memory_usage = 0.4
            self.__cpu_temp = 45
            self.__battery_level = 0.4
            return self.gen_load_msg()

    def turn_off(self):
        if self.is_power_on:
            self.__is_power_on = False
            self.__memory_usage = 0.0
            self.__cpu_temp = 0
            return self.gen_shutdown_msg()

    def charge(self, duration):
        duration /= 60
        self.battery_level += duration * 0.35

    def run_code(self, code):
        result = eval(code)
        if result:
            print(result)
        self.__cpu_temp += 5
        self.__memory_usage += 0.07


laptop = Laptop()
for message in laptop.turn_on():
    os.system("clear")
    print(message)

while True:
    code = input(">>> ")
    if code == "quit()":
        break
    laptop.run_code(code)

for message in laptop.turn_off():
    os.system("clear")
    print(message)
