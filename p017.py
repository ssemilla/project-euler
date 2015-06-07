#!/usr/bin/env python

words = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
         'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
words10 = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

def get_word(n):

    num = ''

    if n / 1000:
        num = words[n/1000] + 'Thousand'
    if (n / 100) % 10:
        num = num + words[(n/100) % 10] + 'Hundred' + (n%100 and 'And' or '')

    if n % 100 < len(words):
        num = num + words[n % 100]
    elif (n / 10) % 10:
        num = num + words10[(n / 10) % 10] + words[n%10]
    else:
        num = num + words[n%10]
    return num

sum = 0    
for i in range(1, 1001):
    sum = sum + len(get_word(i))

print sum    
