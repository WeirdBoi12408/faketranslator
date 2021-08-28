#language
# ᔧᔨᔩᔪᔫᔬᔭᔮᔯᔰᔱᔲᔳᔴᔵᔶᔷᔸᔹᔺᔻᔼᔽ

engdict = list(open('engdict.txt',encoding='utf-8'))
fakedict = list(open('fakedict.txt',encoding='utf-8'))
engalphabet = "abcdefghijklmnopqrstuvwxyz.,?!"
fakealphabet = "ᐁᐃᐯᐱᐳᐸᐊᐅᑐᑕᑌᑎᑭᑯᑲᑫᓀᓄᓇᓂᕈᕊᕄᕂᓬᕒᐠᐟᐦᐥ"
#fakealphabet = "ᐯᐰᐱᐲᐳᐴᐵᐶᐷᐸᐹᐺᐻᐼᐽᐾᐿᑀᑁᑂᑃᑄᑅᑆᑇᑈᐠᐟᐦᐥ"
engpunctuation = ".,?!"
fakepunctuation = "ᐠᐟᐦᐥ"
numbers = "0123456789"
fakenumbers = "ᒣᒤᒥᒦᒧᒨᒩᒪᒫᒬᒭᒮᒽ"

# remove the stupid newlines from the dicts
for n in range(0,len(engdict)):
    engdict[n] = engdict[n].strip("\n")
for n in range(0,len(fakedict)):
    fakedict[n] = fakedict[n].strip("\n")

def translatenumbertofake(num):
    global fakenumbers

    try:
        number = float(num)
    except ValueError:
        number = 1
    d = 0
    if number != round(number):
        while number != round(number):
            d = d + 1
            number = number * 12

    output = ""
    while number >= 12:
        o = number % 12
        output = fakenumbers[int(o)] + output
        number = (number - o) / 12
    output = fakenumbers[int(number)] + output
    if d != 0:
        output = list(output)
        output.insert(len(output) - d,"ᒽ")
        ao = ""
        for n in range(0,len(output)):
            ao = ao + output[n]
        return ao
    return output

def translatewordtofake(text):
    global engdict
    global fakedict
    global numbers
    puncts = [".",",","?","!"]
    fakepunct = ["ᐠ","ᐟ","ᐦ","ᐥ"]
    fakepuncts = []
    containspunctuation = False
    text = list(text)
    n = 0
    while n < len(text):
        if text[n] in puncts:
            fakepuncts.append(fakepunct[puncts.index(text[n])])
            text.pop(n)
        else:
            n = n + 1
    output = ""
    for n in range(0,len(text)):
        output = output + text[n]
    text = output
    if text.lower() in engdict:
        output = fakedict[engdict.index(text.lower())]
        if len(fakepuncts) != 0:
            p = ""
            for z in range(0,len(fakepuncts)):
                p = p + fakepuncts[z]
            output = output + p
        return output
    else:
        txt = list((text + "a").lower())
        n = 0
        while n < len(text):
            try:
                txt[n] = fakealphabet[engalphabet.index(txt[n])]
            except ValueError:
                if txt[n] in numbers:
                    num = ""
                    prevn = n
                    removals = 0
                    while txt[n] in numbers:
                        num = num + txt[n]
                        removals = removals + 1
                        n = n + 1
                    for q in range(0,removals):

                        txt.pop(prevn)
                    txt.insert(prevn,translatenumbertofake(num))
            n = n + 1
        output = ""
        for n in range(0,len(txt) - 1):
            output = output + txt[n]
        if len(fakepuncts) != 0:
            p = ""
            for z in range(0,len(fakepuncts)):
                p = p + fakepuncts[z]
            output = output + p
        return(output)



def translatetofake(text):
    global engalphabet
    global fakealphabet
    global numbers
    n = 0
    txt = []
    word = ""
    while n < len(text):
        if text[n] != " ":
            word = word + text[n]
        else:
            txt.append(translatewordtofake(word))
            word = ""
        n = n + 1
    txt.append(translatewordtofake(word))
    output = ""
    for n in range(0,len(txt)):
        output = output + txt[n] + " "
    return output

def translatefaketoword(fake):
    global engdict, fakedict, numbers
    puncts = [".",",","?","!"]
    fakepunct = ["ᐠ","ᐟ","ᐦ","ᐥ"]
    fakepuncts = []
    containspunctuation = False
    text = list(fake)
    n = 0
    while n < len(text):
        if text[n] in puncts:
            fakepuncts.append(puncts[fakepunct.index(text[n])])
            text.pop(n)
        else:
            n = n + 1
    output = ""
    for n in range(0,len(text)):
        output = output + text[n]
    text = output
    if text in fakedict:
        output = engdict[fakedict.index(text.lower())]
        if len(fakepuncts) != 0:
            p = ""
            for z in range(0,len(fakepuncts)):
                p = p + fakepuncts[z]
            output = output + p
        return output
    else:
        txt = list((text + "a"))
        n = 0
        while n < len(text):
            try:
                txt[n] = engalphabet[fakealphabet.index(txt[n])]
            except ValueError:
                if txt[n] in numbers:
                    num = ""
                    prevn = n
                    removals = 0
                    while txt[n] in numbers:
                        num = num + txt[n]
                        removals = removals + 1
                        n = n + 1
                    for q in range(0,removals):

                        txt.pop(prevn)
                    txt.insert(prevn,translatenumbertofake(num))
            n = n + 1
        output = ""
        for n in range(0,len(txt) - 1):
            output = output + txt[n]
        if len(fakepuncts) != 0:
            p = ""
            for z in range(0,len(fakepuncts)):
                p = p + fakepuncts[z]
            output = output + p
        return(output)

def translatetoeng(text):
    global engalphabet
    global fakealphabet
    global numbers
    n = 0
    txt = []
    word = ""
    while n < len(text):
        if text[n] != " ":
            word = word + text[n]
        else:
            txt.append(translatefaketoword(word))
            word = ""
        n = n + 1
    txt.append(translatefaketoword(word))
    output = ""
    for n in range(0,len(txt)):
        output = output + txt[n] + " "
    return output

if input('which') == '0':
    print(translatetoeng(input('input')))
else:
    print(translatetofake(input('input')))
