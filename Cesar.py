alphavit = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
key = int(input('Key:'))
str1 = input()
res = ''

for i in str1:
    if i == ' ':
        res+=' '
        continue
    
    res += alphavit[(alphavit.find(i) + (key + 1)) % len(alphavit)]
    
print('Result: "' + res + '"')

