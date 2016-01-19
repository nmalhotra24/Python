""" Write code using find() to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out. """

text = "X-DSPAM-Confidence:    0.8475";
# find the space
space = text.find(" ")
number = text[space::1]
result = float(number)
print result 