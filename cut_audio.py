from pydub import AudioSegment
import os


files = os.listdir(path=f"{os.path.join(os.getcwd(), 'music')}")
for i, el in enumerate(files):
    t1 = 0  # Works in milliseconds
    t2 = 5000
    flag = 1
    counter = 1
    try:
        newAudio = AudioSegment.from_wav(f"{os.path.join(os.getcwd(), 'music', el)}")
        while flag:
            if t2 > len(newAudio):
                flag = 0
            else:
                if not os.path.isdir(os.path.join(os.getcwd(), 'Newfile', el)):
                    os.mkdir(os.path.join(os.getcwd(), 'Newfile', el))  # making a folder for pieces
                nwAudio = newAudio[t1:t2]
                nwAudio.export(f'{os.path.join(os.getcwd(), "Newfile", el)}//{el[0:len(el) - 4]}-{counter}.wav',
                               format="wav")  # Export audio to a folder
                t1 += 5000
                t2 += 5000
                counter += 1
    except Exception as exc:
        print('next one, cause of ', exc)
        continue


