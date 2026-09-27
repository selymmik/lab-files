#for incompatible encoding - big5 taiwanese and gb2321 - simplified chinese use try/except if cant encode w/gb2312 then 

def load_chinese_file(filename):
    #open in binary mode ('b"): reading raw bytes, no encoding yet
    f = open(filename, 'br')
    bs = f.read()
    try:
        text = bs.decode('gb2312')
        print('gb2312')
    except UnicodeDecodeError:
        text = bs.decode('big5')
        print('big5')
    return text
f = open('part2/secret_message.txt', encoding = 'cp500')  

with open('secret_message.utf8', 'w', encoding='utf-8') as file:
    file.write(f.read())