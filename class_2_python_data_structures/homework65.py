str = "X-DSPAM-Confidence:  0.8475"

x = str.find(":")

y = str.find("5")

z = str[x+2:y+1]
print(float(z))