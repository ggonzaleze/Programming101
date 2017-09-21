path = 'C:/Users/georg/Documents/python/cars.txt'
file_path = open(path,'r')
lines = file_path.readlines()
lines = lines[0::2]
accumulation_city = 0
accumulation_highway = 0
accumulation_price = 0
string = ""
for element in lines:
    string = element[52] + element[53]
    accumulation_city = accumulation_city + int(string)
    string = element[55] + element[56]
    accumulation_highway = accumulation_highway + int(string)
    string = element[42] + element[43] + element[44] + element[45]
    accumulation_price = accumulation_price + float(string)
average_cityMPG = accumulation_city / len(lines)
average_highwayMPG = accumulation_highway / len(lines)
average_price = accumulation_price / len(lines)
file_path.close()
print("The average gas mileage in city is: ",average_cityMPG)
print("The average gas mileage on highway is: ",average_highwayMPG)
print("The average midrange price is: ",average_price)
