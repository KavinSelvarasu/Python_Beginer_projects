# import tkinter
#
# from covid import Covid
# import json
#
# from tkinter import *
#
# window = tkinter.TK()
#
# window.title("GUI")
#
# lable = tkinter.lable(window, text="Helloworld").pack()
#
# window.mainloop()

# covid = Covid(source='worldometers')
#
# data = covid.get_data()
# countries = covid.get_status_by_country_name('india')
#
# print(countries)
#
# stirnjs = json.dumps(countries)
# print(stirnjs)


s = (input("Enter your name: "))
print(s[::-1])