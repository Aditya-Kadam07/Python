# def gen_prime(a, b): return [n for n in range(a,b+1) if 0 not in [n%i for i in range(2, n//2+1)]]

# print(gen_prime(1,200))

# print("Hallo")

# print([n for n in range(2,201) if 0 not in [n%i for i in range(2, n//2+1)]])


# morse_To_English = {
#     ".-":"A",    "-...":"B",    "-.-.":"C",    "-..":"D",    ".":"E",    "..-.":"F",    "--.":"G",    "....":"H",    "..":"I",    ".---":"J",    "-.-":"K", 
#     ".-..":"L",  "--":"M",      "-.":"N",      "---":"O",    ".--.":"P", "--.-":"Q",    ".-.":"R",    "...":"S",     "-":"T",     "..-":"U",     "...-":"V",
#     ".--":"W",   "-..-":"X",    "-.--":"Y",    "--..":"Z",   
#     "/":" ",
#     ".----":"1", "..---":"2", "...--":"3", "....-":"4", ".....":"5", "-....":"6", "--...":"7", "---..":"8", "----.":"9", "-----":"0",  
#     "..--..":"?", "-.-.--":"!", ".-.-.-":".", "--..--":",", "-.-.-.":";", "---...":":", ".-.-.":"+", "-....-":"8", "-..-.":"/", "-...-":"="
# }

# english_To_Morse = {
#     "A":".-",    "B":"-...",    "C":"-.-.",    "D":"-..",    "E":".",    "F":"..-.",    "G":"--.",      "H":"....",      "I":"..",      "J":".---",    "K":"-.-", 
#     "L":".-..",    "M":"--",    "N":"-.",     "O":"---",    "P":".--.",    "Q":"--.-",     "R":".-.",      "S":"...",      "T":"-",        "U":"..-",      "V":"...-",
#     "W":".--",      "X":"-..-",     "Y":"-.--",     "Z":"--..",   
#     " ":"/",   
#     "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....", "6":"-....", "7":"--...", "8":"---..", "9":"----.", "0":"-----",
#     "?":"..--..", "!":"-.-.--", ".":".-.-.-",",":"--..--", ";":"-.-.-.",":":"---...","+":".-.-.", "*":"-....-", "/":"-..-.", "=":"-...-"
#     }



# Choice = int(input("\n1. Morse to English \n2. English to Morse \n3. Exit \nYour Choice : "))
# while Choice != 3:
#     if Choice == 1:
#         print("####\n")
#         print("Note : use / for space between words \n")
#         Morse_String = input("Type in Morse Code : ")
#         print("Morse : ",Morse_String,"\n")

#         Morse_List = Morse_String.split()
#         English_Converted = []
#         for i in Morse_List:
#             English_Converted.append(morse_To_English[i])

#         Final_English_Conversion = "".join(English_Converted)
#         print("English : ",Final_English_Conversion,"\n")
#         exit()
#     if Choice == 2:
#         print("####\n")
#         English_String = input("Type in English : ").upper()
#         print("English : ",English_String,"\n")

#         Morse_List = [*English_String]
#         Morse_Converted = []
#         for i in Morse_List:
#             Morse_Converted.append(english_To_Morse[i])

#         Final_Morse_Conversion = " ".join(Morse_Converted)
#         print("Morse : ",Final_Morse_Conversion,"\n")
#         exit()
# print("Bye!!")



def data_morse():
    morse_To_English = {
        ".-":"A",    "-...":"B",    "-.-.":"C",    "-..":"D",    ".":"E",    "..-.":"F",    "--.":"G",    "....":"H",    "..":"I",    ".---":"J",    "-.-":"K", 
        ".-..":"L",  "--":"M",      "-.":"N",      "---":"O",    ".--.":"P", "--.-":"Q",    ".-.":"R",    "...":"S",     "-":"T",     "..-":"U",     "...-":"V",
        ".--":"W",   "-..-":"X",    "-.--":"Y",    "--..":"Z",   
        "/":" ",
        ".----":"1", "..---":"2", "...--":"3", "....-":"4", ".....":"5", "-....":"6", "--...":"7", "---..":"8", "----.":"9", "-----":"0",  
        "..--..":"?", "-.-.--":"!", ".-.-.-":".", "--..--":",", "-.-.-.":";", "---...":":", ".-.-.":"+", "-....-":"8", "-..-.":"/", "-...-":"="
    }    
    
    english_To_Morse = {
    "A":".-",    "B":"-...",    "C":"-.-.",    "D":"-..",    "E":".",    "F":"..-.",    "G":"--.",      "H":"....",      "I":"..",      "J":".---",    "K":"-.-", 
    "L":".-..",    "M":"--",    "N":"-.",     "O":"---",    "P":".--.",    "Q":"--.-",     "R":".-.",      "S":"...",      "T":"-",        "U":"..-",      "V":"...-",
    "W":".--",      "X":"-..-",     "Y":"-.--",     "Z":"--..",   
    " ":"/",   
    "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....", "6":"-....", "7":"--...", "8":"---..", "9":"----.", "0":"-----",
    "?":"..--..", "!":"-.-.--", ".":".-.-.-",",":"--..--", ";":"-.-.-.",":":"---...","+":".-.-.", "*":"-....-", "/":"-..-.", "=":"-...-"
    }
    return morse_To_English, english_To_Morse

def M2E():
    morse_To_English, english_To_Morse = data_morse()
    Morse_String = input("Type in Morse Code : ")
    print("Morse : ",Morse_String,"\n")

    Morse_List = Morse_String.split()
    English_Converted = []
    for i in Morse_List:
        English_Converted.append(morse_To_English[i])

    Final_English_Conversion = "".join(English_Converted)
    # print("English : ",Final_English_Conversion,"\n")
    return Final_English_Conversion


def E2M():
    morse_To_English, english_To_Morse = data_morse()
    English_String = input("Type in English : ").upper()
    print("English : ",English_String,"\n")

    Morse_List = [*English_String]
    Morse_Converted = []
    for i in Morse_List:
        Morse_Converted.append(english_To_Morse[i])

    Final_Morse_Conversion = " ".join(Morse_Converted)
    # print("Morse : ",Final_Morse_Conversion,"\n")
    return Final_Morse_Conversion
    

print(M2E())
print(E2M())