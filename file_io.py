# jabber = open("sample.txt", 'r')
#
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')
#
# jabber.close()


# with open("sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')


# with open("sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end = '')
#         line = jabber.readline()


# with open("sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
# for line in lines:
#     print(line, end='')


# with open("sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
# for line in lines[::-1]:
#     print(line, end='')
#
#
#
# with open("sample.txt", 'r') as jabber:
#     lines = jabber.read()
#
# for line in lines[::-1]:
#     print(line, end='')



# ##### WRITING to A FILE IN PYTHON


# cities = ["Adelaide", "Alice springs", "Darwin", "Melbourne", "sydney"]
#
# with open("cities.txt", 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file)



# cities = []
# with open("cities.txt", 'r') as city_file:
#     for city in city_file:
#         cities.append(city.strip('\n'))
#
# print(cities)
# for city in cities:
#     print(city)



# imelda = "more mayhem", "imelda may", "2011",(
#     (1, "pulling the rug"), (2, "psycho"), (3, "mayhem"), (4, "kentish town waltz"))
# with open("imelda3.txt", 'w') as imelda_file:
#     print(imelda, file=imelda_file)



# with open("imelda3.txt", 'r') as imelda_file:
#     contents = imelda_file.readline()
#
# imelda = eval(contents)
#
# print(imelda)
# title, artist, year, tracks = imelda
# print(title)
# print(artist)
# print(year)

# with open("sample1.txt", 'a') as tables:
#     for i in range(2, 13):
#         for j in range(1, 13):
#             print("{1:>2} times {0} is {2}".format(i, j, i*j), file=tables)
#         print("-" * 20, file=tables)


# import shelve
# books = shelve.open("book")
# books["recipes"] = {"blt": ["bacon", "lettuce", "tomato", "bread"],
#                      "beans_on_toast": ["beans", "bread"],
#                      "scrambled eggs": ["eggs", "butter", "milk"],
#                      "soup": ["tin of soup"],
#                      "pasta": ["pasta", "cheese"]}
# books["maintenance"] = {"stuck": ["oil"], "loose":["gaffer tape"]}
#
#
# print(books["recipes"])
# # print(books["recipes"]["scrambled eggs"])
# #
# # print(books["maintenance"]["loose"])





