cipher = open('ciphertext.txt').read()
def create_key(s):
    count={}
    order = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
    # ignore = ['"', ':', ';', ',', '.', '-', '+', '=', '/', "\\", '|', '[', ']', '{', '}','(',')','*','^','&',' ']
    # for i in ignore:
        # s=s.replace(i,'') #can use isalpha instead    #count the letters
    for letter in s:
        # can add this instead of the s.replace
        if letter.isalpha():
            if letter in count:
                count[letter]+=1
            else:
                count[letter]=1
    count={key: value for key, value in sorted(count.items(), key=lambda item: item[1], reverse=True)}
    # print(count)
    for index, key in enumerate(count):
        if index>= len(order):
            continue
        count[key]=order[index]
    return count
    def decode(s, key):
        r = ""
        for c in s:
            if c not in key:
                r+=str(c)
            else:
                r += str(key[c])    
        return rkey=create_key(cipher)
# print(key)
print(decode(cipher, key))