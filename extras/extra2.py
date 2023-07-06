#def average():
    #with open('../files/extra2.txt','r') as file:
        #temperatures = file.readlines()
        #temperatures.pop(0)
        #new_array = [int(i.strip('\n')) for i in temperatures]
        #sum = 0
        #for element in new_array:
            #sum = sum + element
        #print(sum)
        #return sum/len(new_array)

#temperature_array = average()
#print(temperature_array)

#with two arguments
#def converter(inches,feet):
    #inches_to_meter = float(inches) * 0.30408
    #feet_to_meter = float(feet) * 2.54 / 100
    #return inches_to_meter+feet_to_meter

#feet_inches = input('Enter feet and inches:')
#split_list = feet_inches.split(' ')
#result = converter(inches= split_list[0], feet = split_list[1])
#print(f"Your result in meters is: {result} m")

#decoupling every function should do one thing we need one extractor and one convertor function


from modules import converter,parser

feet_inches = input('Enter feet and inches:')
extracted_dictionary = parser.extractor(feet_inches)
conversion = converter.converter(extracted_dictionary['feet'],extracted_dictionary['inches'])
if conversion < 1:
    print(f"you are too short. Your height is:{conversion} m")
if conversion > 1:
    print(f"you are tall. Your height is:{conversion} m")



