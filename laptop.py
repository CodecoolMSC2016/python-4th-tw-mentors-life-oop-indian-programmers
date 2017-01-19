import time
import os
from temperature import ProcessorOverheat


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
            raise ProcessorOverheat("CPU_TEMP reached " + str(self.cpu_temp) + "C.")
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
            return self.gen_load_msg("Loading")

    def turn_off(self):
        if self.is_power_on:
            self.is_power_on = True
            return self.gen_load_msg("Shutdown")


laptop = Laptop()
for msg in laptop.turn_on():
    os.system("clear")
    print(msg)
for msg in laptop.turn_off():
    os.system("clear")
    print(msg)
