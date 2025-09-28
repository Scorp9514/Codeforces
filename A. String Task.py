text = input()
new = []
text = text.lower()
#print(text)
for w in text:
    if w == "a" or w == "o" or w == "y" or w=="e" or w == "u" or w =="i":
        pass
    else:
        new.append(w)

print("."+".".join(new))