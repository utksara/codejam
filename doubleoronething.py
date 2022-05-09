N = int(input())

class pattern_detector():
    def __init__(self):
        self.start = 0
        self.detected = False
        self.temp_repeatables = []
        self.total_repeatables = []
    
    def detect(self, x, i):
        if i > 0:
            if x[i] > x[i-1]:
                self.detected = False
                self.total_repeatables += self.temp_repeatables
                self.temp_repeatables = []
                self.total_repeatables.append({
                    "letter" : x[i-1],
                    "position" : i-1,
                })
                
            if x[i] == x[i-1]:
                self.temp_repeatables.append({
                    "letter" : x[i-1],
                    "position" : i-1,
                })
            if x[i] < x[i-1]:
                self.detected = False
                self.temp_repeatables = []
        return self.total_repeatables

def doublesomthing(words):

    p = pattern_detector()
    for i in range(0, len(words)):
        p.detect(words, i)

    x = p.total_repeatables
    new_str = words
    shift = 0
    for elem in x:
        i = elem["position"]
        new_str = new_str[0:i+shift] + words[i] + new_str[i+shift:]
        shift+=1
    return new_str

words_data = []
string_data = ''
for i in range(1, N+1):
    words_data.append( input())

for i in range(0, len(words_data)):
    words = words_data[i]
    print("Case #"+ str(i+1) + ":", doublesomthing(words))
    # string_data = "Case #"+ str(i+1) + ": " + str(doublesomthing(words)) + '\n'

    # with open('doubleoutput.txt', 'a') as f:
    #     f.write(string_data)