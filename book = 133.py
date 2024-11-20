books = 133
people = 6                               #برنامج
rate = books//people                      #توزيع 133 كتاب على 6 اشخاص و كم سيتبقى من الكتب
residual =books%people
print(f" every body take {rate} books and remainder {residual} book.")
print()

people = 147
rooms = 35                                #  توزيع 147 شخص على 35غرفة وكم سيبقى بدون غرف
rate = people//rooms
residual_out =people%rooms
print(f"every {rate} people take 1 room and remainder {residual_out} people out rooms .")
print()

salary = 5000
tax = 700
reward = ((salary+1000)*3) -tax          #مكافئ لموظف تساوى 1000+ راتبه5000*3 نخصم 700جنيه ضريبه

print(f"functionary reward  {reward}.")
