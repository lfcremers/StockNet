## this approach works
import os
os.chdir('/')


os.chdir('Users/lcremers/phone_sync/test')


recordings=os.listdir()
#other improvements:
#only recordings in the directory in case there's other stuff


if not os.path.exists('./new_recs'):
    os.mkdir("new_recs")
if not os.path.exists('./tried'):
    os.mkdir("tried")



def get_kwds(name):
    name=name.replace(",", " ")#.replace("-"," ")
    name=name.replace("  "," ")
    words = name.split(" ")
    main_words=[]
    for w in words:
        if w[0].isupper():
            main_words.append(w)
    longest_words = sorted(words,key=len)
    if longest_words[-1] in main_words:
        del main_words[main_words.index(longest_words[-1])]
    if len(main_words)<3 and len(words)>4:
        for i in range(2,5):
            if longest_words[-i] not in main_words:
                main_words.append(longest_words[-i])
    return main_words



def dir_proof(string):
    string=list(string)
    for i in range(len(string)):
        if string[i]==" ":
            string[i]=r'\ '
        if string[i]=="&":
            string[i]=r'\&'
        if string[i]=="'":
            string[i]=r'\''
        if string[i]=="(":
            string[i]=r'\('
        if string[i]==")":
            string[i]=r'\)'
    string = "".join(string)
    return string


def filter_recordings(recordings):
    i=0
    while i < len(recordings):
        if recordings[i][0]=='.' or '.' not in recordings[i]:
            recordings.remove(recordings[i])
            continue
        i=i+1
    return recordings

for mp3 in filter_recordings(recordings):
    new_title="_".join(get_kwds(mp3))+".mp3"
    os.system("sox old_mp3 new_title tempo 1.4".replace("old_mp3",dir_proof(mp3)).replace("new_title",dir_proof(new_title)))
    os.system("mv old_mp3 ./tried".replace("old_mp3",dir_proof(mp3)))
    os.system("mv new_title ./new_recs".replace("new_title",dir_proof(new_title)))


