def extractor(input):
    split_string = input.split(' ')
    feet = float(split_string[0])
    inches = float(split_string[1])
    print(feet,inches)
    return {'feet': feet, 'inches': inches}