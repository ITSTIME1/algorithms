import pandas as pd
import random
import playsound
from gtts import gTTS
root_file_path = "/Users/itstime/algorithms/python-algo/ToicWordProject/"

def 토익단어_엑셀():
    
    txt_file_path = root_file_path + '토익단어추가장.txt'
    df = pd.read_csv(txt_file_path, delimiter='\t', header=None)
    # excel_frame = pd.DataFrame(list(df[0]), columns=['단어'])
    
    # excel_frame['의미'] = ""
    # excel_frame.to_excel(root_file_path + "토익단어엑셀파일.xlsx")
    
    print("성공")
    return list(df[0])

def 단어장(wordTextName=None):
    txt_file_path = root_file_path + wordTextName
    df = pd.read_csv(txt_file_path, delimiter='\t', header=None)
    result = list(df[0])
    
    word_dic = {}
    for i in result:
        a = i.split(", ")
        word_dic[a[0]] = a[1]

    
    return word_dic


def 랜덤단어뽑기_단어뜻맞추기(word_dic=None):
    chosen_number = int(input("선택 : 1 or 2 \n1 = 단어뜻까지 쓰기, 2 = enter시 넘어가기\n"))
    chosen_nation = int(input("영국식 발음 원하나? : 1 or 2\n1 = yes,\n2 = no\n"))
    
    word_list = list(word_dic.keys())
    visited = [0] * len(word_list) 
    
    if chosen_nation == 1:
        print(f"영국식 발음으로 변경하겠습니다.")
    else:
        print(f"미국식 발음으로 변경하겠습니다.")
    
    if chosen_number == 2:
        
        while True:
            if visited.count(0) == 0:
                break

            index = random.randint(0, len(word_list)-1)
            if visited[index] != 1:
                # set Default us
                object_gTTs = gTTS(text=word_list[index], lang="en", tld='co.uk') if chosen_nation == 1 else gTTS(text=word_list[index], lang="en")                     
                fileName = 'word7.mp4'
                # us_tts.save(fileName)
                object_gTTs.save(fileName)
                playsound.playsound(fileName)
                print(f"{word_list[index]}, {word_dic[word_list[index]]}\n")
                input()
                visited[index] = 1
                
    else:
        while True:
            if visited.count(0) == 0:
                break

            index = random.randint(0, len(word_list)-1)
            if visited[index] != 1:
                tts = gTTS(text=word_list[index], lang="en")
                fileName = 'word.mp4'
                tts.save(fileName)
                playsound.playsound(fileName)
                print(f"{word_list[index]}\n")
                result = input("의미 : ")  

                if "".join(result.split()) == "".join(word_dic[word_list[index]].split()):
                    print(f"정답")
                    visited[index] = 1
                    continue 
                else:
                    print("오답")
                    isAnswer = False
                    failCount = 1
                    while not isAnswer:
                        playsound.playsound(fileName)
                        if failCount == 2:
                            print(f"정답 : {word_dic[word_list[index]]}")
                            failCount = 0

                        result = input("의미 : ")
                        if "".join(result.split()) == "".join(word_dic[word_list[index]].split()):
                            print("정답")
                            visited[index] = 1
                            isAnswer = True
                        else:
                            print("오답")
                            failCount+= 1


랜덤단어뽑기_단어뜻맞추기(단어장('LC파트2(부가의문문).txt'))
# 랜덤단어뽑기_단어뜻맞추기(LCPart2())
# # 랜덤단어뽑기(가산명사())
# # 랜덤단어뽑기(불가산명사())
# # 랜덤단어뽑기(토익단어_엑셀())
# # 랜덤단어뽑기(형용사())
# LCPart2()
# # 랜덤단어뽑기(LCPart2())
