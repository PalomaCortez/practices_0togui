## C10 Inheritance and Polymorphism
# EX6 Display clock

from tkinter import *
import math
from datetime import datetime

# ver depois uma forma de dinamizar o código com hora acompanhando minuto e seg

class StillClock(Canvas):
    def __init__(self, container):
        super().__init__(container)
        self.set_current_time()

    def get_hour(self):
        return self.__hour

    def set_hour(self, hour):
        self.__hour = hour
        self.delete("clock")
        self.draw_clock()

    def get_minute(self):
        return self.__minute

    def set_minute(self, minute):
        self.__minute = minute
        self.delete("clock")
        self.draw_clock()

    def get_second(self):
        return self.__second

    def set_second(self, second):
        self.__second = second
        self.delete("clock")
        self.draw_clock()

    def set_current_time(self):
        d = datetime.now()
        self.__hour = d.hour
        self.__minute = d.minute
        self.__second = d.second
        self.delete("clock")
        self.draw_clock()

    def draw_clock(self):
        width = float(self["width"])
        height = float(self["height"])
        radius = min(width, height) / 2.4
        second_hand_length = radius * 0.8
        minute_hand_length = radius * 0.65
        hour_hand_length = radius * 0.5
        x_center = width / 2
        y_center = height / 2

        self.create_oval(x_center - radius, y_center - radius,
                         x_center + radius, y_center + radius, tags="clock")
        self.create_text(x_center - radius + 5, y_center,
                         text="9", tags="clock")
        self.create_text(x_center + radius - 5, y_center,
                         text="3", tags="clock")
        self.create_text(x_center, y_center - radius + 5,
                         text="12", tags="clock")
        self.create_text(x_center, y_center + radius - 5,
                         text="6", tags="clock")

        second = self.__second
        x_second = x_center + second_hand_length \
                    * math.sin(second * (2 * math.pi / 60))
        y_second = y_center - second_hand_length \
                    * math.cos(second * (2 * math.pi / 60))
        self.create_line(x_center, y_center, x_second, y_second,
                         fill="red", tags="clock")

        minute = self.__minute
        x_minute = x_center + minute_hand_length \
                   * math.sin(minute * (2 * math.pi / 60))
        y_minute = y_center - minute_hand_length \
                   * math.cos(minute * (2 * math.pi / 60))
        self.create_line(x_center, y_center, x_minute, y_minute,
                         fill="blue", tags="clock")

        hour = self.__hour % 12
        x_hour = x_center + hour_hand_length \
                   * math.sin(hour * (2 * math.pi / 12))
        y_hour = y_center - hour_hand_length \
                   * math.cos(hour * (2 * math.pi / 12))
        self.create_line(x_center, y_center, x_hour, y_hour,
                         fill="green", tags="clock")

        timestr = str(hour) + ":" + str(minute) + ":" + str(second)
        self.create_text(x_center, y_center + radius + 10,
                         text=timestr, tags="clock")
