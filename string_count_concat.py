# input aabccddddabaa
# output a2b1c2d4a1b1a2

def encode_string(seq):
    count=1
    encoded_str=""
    previous_char=seq[0]
    for i in range(1,len(seq)):
        print(i)
        if seq[i]==previous_char:
            count+=1
        else:
            encoded_str+=previous_char+str(count)
            count=1
            previous_char = seq[i]

    encoded_str += previous_char + str(count)


    return encoded_str


seq="aabccddddabaa"
c=encode_string(seq)
print(c)