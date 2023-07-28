# # This is a sample Python script.
#
# # Press ⌃R to execute it or replace it with your code.
# # class SuperList(list):
# #     def __len__(self):
# #         return 1000
# #
# # super_list1 = SuperList();
# #
# # print(len(super_list1))
# # super_list1.append(5)
# # print(super_list1[0])
# #     #super_list1[5]
#
# # my_list = [1,2,3]
# # your_list = [2,3,4]
# #
# # print(list(zip(my_list,your_list)))
#
# #LAMBDA ONE TIME ANONYMOUS FUNCTIONS YOU DON'T NEED MORE THAN ONCE.THEY DON'T NEED A NAME SINCE THEY ARE ONLY USED ONCE.
#
# from functools import reduce
# #
# my_list = [5,4,3]
#
# #create a lambda expression that will create a squared list.
# # item*2
# # my_list = [5,4,3]
# # squared_list = [num**2 for num in my_list]
# # print(squared_list)
# #
# # # I got it!
# #
# # # squared_list = [num **2 for num in my_list]
# # print((lambda:squared_list))
#
# #list sorting list with tuples
#
# #my_list = [(0, 2), (4, 3), (9, 9), (10, -1)]
#
# #list what you want, here it is to retrieve the second item.
#
# #second_items = [item[1] for item in my_list]
# #print(second_items)  # Output: [2, 3, 9, -1]
#
# # using map and lambda
# my_list = [5,4,3]
#
# new_list = list(map(lambda num: num**2, my_list))
# print(new_list)
#
# #List Sorting
#
# a = [(0, 2), (4, 3), (9, 9), (10, -1)]
#
# a.sort(key=lambda x: x[1])
# lamda practice


exponenter= lambda x: x**2
result = exponenter(11)
print(result)