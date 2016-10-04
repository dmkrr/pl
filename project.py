import sys
import os
import random

class calculator:
    __result_list = [0,0]
    __anz_result = 0

    def __init__(self):
        __result_list = [0]
        __anz_result = 0

    def sum(self, a, b) :
        self.__result_list[self.__anz_result] = a + b
        self.__anz_result += 1
        return self.__result_list[self.__anz_result - 1]

    def get_last_reult(self, number):
        if number > __anz_result :
            return self.__result_list[0]
        else :
            return self.__result_list[number]



c = 10
d = 13


cal = calculator()

print(cal.sum(c,d))
print(cal.sum(1,2))
print(cal.sum(2,3))
print(cal.sum(5,6))



