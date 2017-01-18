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

    def _add_temperature(self, value):
        self.cpu_temp += value
        if self.cpu_temp > 85:
            raise ProcessorOverheat("CPU_TEMP reached " + str(self.cpu_temp) + "C.")
        elif self.cpu_temp > 60:
            return self.cpu_temp

    def _gen_load_msg(self, message):
        for i in range(4):
            time.sleep(0.5)
            yield message + "." * i
        time.sleep(0.5)
        yield self.loading_msg[message]

    def turn_on(self):
        if not self.is_power_on:
            self.is_power_on = True
            self.cpu_temp = 45
            self.battery_level = 0.4
            for message in self._gen_load_msg("Loading"):
                os.system("clear")
                print(message)
            self._run_REPL()

    def turn_off(self):
        if self.is_power_on:
            self.is_power_on = False
            self.cpu_temp = 0
            for message in self._gen_load_msg("Shutdown"):
                os.system("clear")
                print(message)

    def _run_code(self, code):
        result = eval(code)
        temperature = self._add_temperature(10)
        if temperature:
            print("Warning: cpu temp " + str(temperature) + "C")
        if result:
            print(result)

    def _run_REPL(self):
        print('''
Python 3.6 (default, Sep 16 2015, 09:25:04)
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
''', end="")
        while True:
            code = input(">>> ")
            if code == "quit()":
                self.turn_off()
            self._run_code(code)


laptop = Laptop()
laptop.turn_on()
