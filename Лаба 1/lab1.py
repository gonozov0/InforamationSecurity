# part1

bias = 2

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def incode_char(char):
    index = alphabet.find(char)
    if index == -1:
        return char
    else:
        return alphabet[index + bias - len(alphabet)]

def incode_file(file):
    incoded_file = open('incoded_file.txt', 'w') 
    for line in file:
        prom = ''
        for char in line.lower():
            prom += incode_char(char)
        incoded_file.write(prom)
    incoded_file.close()

file = open('usual_file.txt')
incode_file(file)
file.close()

# part2

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def analize(file):
    statistic = {}
    for line in file:
        for char in line.lower():
            if char in alphabet:
                if char not in statistic:
                    statistic[char] = 0
                statistic[char] += 1
    list_1 = list(statistic.items())
    list_1.sort(key = lambda i: i[1], reverse=True)
    return list_1

def decode_file(all_text_file, incoded_file):
    sort_incoded_analize_list = analize(incoded_file)
    sort_all_text_analize_list = analize(all_text_file)
    decoded_file = open('decoded_file.txt', 'w')
    
    for line in incoded_file:
        prom = ''
        for char in line.lower():
            for i in range(len(sort_incoded_analize_list)):
                if sort_incoded_analize_list[i][0] == char:
                    prom += sort_all_text_analize_list[i][0]
                    break
            else:
                prom += char
        decoded_file.write(prom)
    decoded_file.close()

file_1 = open('War.txt')
file_2 = open('incoded_file.txt')
#print(file_2.readlines())
decode_file(file_1.readlines(), file_2.readlines())
file_1.close()
file_2.close()