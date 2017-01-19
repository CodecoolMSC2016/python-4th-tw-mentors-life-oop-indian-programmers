import time
import os
from cpu_temp import ProcessorOverheatError


class Laptop:
    loading_msg = {"Loading": "Welcome!", "Shutdown": "Goodbye!"}

    def __init__(self):
        self.is_power_on = False
        self.battery_level = 0.0
        self.cpu_temp = 0

    def charge_battery(self, duration):
        duration /= 60
        self.battery_level += duration * 0.35
        if self.battery_level < 100:
            self.battery_level = 100

    def add_temperature(self, value):
        self.cpu_temp += value
        if self.cpu_temp > 85:
            raise ProcessorOverheatError("Fatal Error! CPU_TEMP reached " + str(self.cpu_temp) + "C.")
        elif self.cpu_temp > 60:
            return self.cpu_temp

    def gen_load_msg(self, message):
        for i in range(4):
            time.sleep(0.5)
            yield message + "." * i
        time.sleep(0.5)
        yield self.loading_msg[message]

    def turn_on(self):
        if not self.is_power_on:
            self.is_power_on = True
            self.cpu_temp = 45
            return self.gen_load_msg("Loading")

    def turn_off(self):
        if self.is_power_on:
            self.is_power_on = True
            self.cpu_temp = 0
            return self.gen_load_msg("Shutdown")

    def run_code(self):
        yield "Running Python Code"
        while True:
            try:
                self.add_temperature(12)
                time.sleep(0.5)
                yield "Current CPU_TEMP: " + str(self.cpu_temp) + "C"
            except ProcessorOverheatError as msg:
                yield msg
                break


def main():
    laptop = Laptop()
    for msg in laptop.turn_on():
        os.system("clear")
        print(msg)
    os.system("clear")
    for msg in laptop.run_code():
        print(msg)

if __name__ == '__main__':
    main()
