import numpy as np

# Function that returns a list with non-uniformly distributed values, with a higher density in the center.
def custom_resistance_list(min,max,point_number,mid_value,spread=10):

    resistance_list_top = list()
    resistance_list_bot = list()
    half_point_number = int(point_number / 2)

    scale_factor_top = (max - mid_value) ** (2 / point_number)
    scale_factor_bot = (mid_value - min) ** (2 / point_number)

    for i in range(half_point_number):
        resistance_list_top.append(mid_value - 1 + scale_factor_top ** i)

    resistance_list_top.append(max)
    resistance_list_top.pop(0)

    for i in range(half_point_number):
        resistance_list_bot.append(mid_value + 1 - scale_factor_bot ** i)

    resistance_list_bot.append(min)
    resistance_list_bot.reverse()

    # print(resistance_list_top)
    # print(resistance_list_bot)

    resistance_list = resistance_list_bot + resistance_list_top

    # print(resistance_list)

    return resistance_list





if __name__ == '__main__':
    print(custom_resistance_list(0.05, 300, 100, 50))
