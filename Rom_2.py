import math

number_dictionary = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "10": "A",
    "11": "B",
    "12": "C",
    "13": "D",
    "14": "E",
    "15": "F",
    "16": "G",
    "17": "H",
    "18": "I",
    "19": "J",
    "20": "K",
    "21": "L",
    "22": "M",
    "23": "N",
    "24": "O",
    "25": "P",
    "26": "Q",
    "27": "R",
    "28": "S",
    "29": "T",
    "30": "U",
    "31": "V",
    "32": "W",
    "33": "X",
    "34": "Y",
    "35": "Z",
}

number_dictionary_swap = {v: k for k, v in number_dictionary.items()}

sign = ""

def isValid(q, R):
    if R.startswith("-"): R_temp = R[1:]
    else: R_temp = R
    for i in R_temp:
        if i != "." and int(number_dictionary_swap[i]) >= q: 
            print("Число " + R + " не є частиною системи " + str(q))
            return False
    return True

def toDecimal(q, R):
    R_temp = R.split(".")
    if R.startswith("-"): 
        R_dec = R_temp[0][1:]
        global sign
        sign = "-"
    else: R_dec = R_temp[0]
    if len(R_temp) != 1:
        R_float = R_temp[1]
        if len(R_float) > 3: 
            print("Повинно бути не більше 3 знаків після крапки")
            return None
    else: R_float = 0
    if q == 10: return float(R)
    sum = 0
    for i in range(0, len(R_dec)):
        sum += int(number_dictionary_swap[R_dec[i]])*(q**(len(R_dec) - i - 1))
    if R_float != 0:
        for i in range(0, len(R_float)):
            sum += float(number_dictionary_swap[R_float[i]])*(q**(-1 - i))
    return sum
    
def Converting(q, R, k):
    if k == 10: return sign + str(toDecimal(q, R))
    if q == k: return R
    decimal = toDecimal(q, R)

    R_dec = math.floor(decimal)
    if R_dec != decimal: 
        temp = str(decimal)[len(str(R_dec)) + 1:]
        R_float = float(temp)/(10**len(temp))
    else: R_float = 0
    
    number_list = []
    while True:
        if R_dec >= k:
            number_list.append(number_dictionary[str(int(R_dec % k))])
            R_dec = R_dec//k
        else:
            number_list.append(number_dictionary[str(R_dec)])
            break
    number = sign + "".join(number_list[::-1])
    
    if R_float != 0:
        number_list_float = []
        for i in range(0, len(str(R_float))):
            R_float = R_float*k
            floor = math.floor(R_float)
            number_list_float.append(number_dictionary[str(floor)])
            R_float = R_float - floor
        number += "." + "".join(number_list_float[:])

    return number



convert = False

try:
    q = int(input("Система, з якої потрібно перевести число (від 2 до 36): "))
except:
    print("Ви ввели неправильне числове значення")
else:
    if q > 36 or q < 2: print("Числове значення не підходить")
    else: convert = True

if convert == True:
    R = input("Саме число (дробову частину писати через крапку): ")
    try:
        if isValid(q, R): 
            if toDecimal(q, R) >= 10 ** 9: 
                print("Числове значення не підходить")
                convert = False
            else:
                R = str(R)
        else: convert = False
    except:
        print("Ви ввели неправильне числове значення")
        convert = False

if convert == True:
    try:
        k = int(input("Система, в яку потрібно перевести число (від 2 до 36): "))
    except:
        print("Ви ввели неправильне числове значення")
        convert = False
    else:
        if k > 36 or k < 2: 
            print("Числове значення не підходить")
            convert = False
        else: convert = True

if(convert and isValid(q, R)): 
    print(Converting(q, R, k))
