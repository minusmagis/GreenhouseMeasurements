#
# Pure Crap :3
#
# resistance_list_top = list()
# resistance_list_bot = list()
#
# mid_value = 60
# max = 300
# min = 0.05
# point_number = 200
# half_point_number = int(point_number/2)
# multiplier = 100000
# scale_factor_top = (max-mid_value)**(2/(point_number))
# scale_factor_bot = (mid_value-min)**(2/(point_number))
# spread = 0.1
# mean = 60
#
# previous_value = mid_value
# for i in range(half_point_number):
#   interval = 0.4-1/(spread*(2*3.141592)**0.5) * 2.71828**((-(i-mean)**2)/(2*spread**2))
#   resistance_list_top.append(previous_value+interval)
#   previous_value = previous_value+interval
#
# resistance_list_top.pop(0)
#
# for i in range(half_point_number):
#   resistance_list_bot.append(mid_value-scale_factor_bot**(i))
#
# resistance_list_bot.append(min)
# resistance_list_bot.reverse()
#
# print(resistance_list_top)
# print(resistance_list_bot)
#
# resistance_list = resistance_list_bot+resistance_list_top
#
# # print(resistance_list)