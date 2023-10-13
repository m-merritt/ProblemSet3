#%% Task 1 - Edit code to print as requested
#/*-PS3: Code Block 1--*/

mountain = "Denali"
nickname = 'Mt. McKinley'
elevation = 20322 

print (str(mountain) + ', formerly \nknown as "' + str(nickname) + '",')
print ("is {}' above sea level.".format(elevation))

#%% Task 2 - Lists and Iteration

data_format = r'W:\859_data\triangle'
data_list = ['streams.shp', 'stream_types.csv', 'naip_imagery.tif']
user_item = 'roads.shp'

data_list.append(user_item)

for data in data_list:
    print(data_format + "\\" + data)

#%% Task 3 - Lists and Iteration

user_numbers = []

for x in range(3):
    guess = input("Enter an integer: ")
    user_numbers.append(int(guess))
user_numbers.sort()
print(user_numbers[2])
    
# %% Task 3 - Challenge

user_numbers = []

for x in range(3):
    guess = input("Enter an integer: ")
    user_numbers.append(int(guess))
user_numbers.sort(reverse=True)
print(user_numbers)