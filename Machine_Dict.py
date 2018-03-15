import re
import string
import math

swear_Dict = dict()  # 욕 사전
non_Swear_Dict = dict() # 욕이 아닌 사전

s_Swear_Cnt = 0     # 욕인 문장 개수
s_Non_Swear_Cnt = 0 # 욕이 아닌 문장 개수

w_Swear_Cnt = 0     # 욕인 단어 개수
w_Non_Swear_Cnt = 0 # 욕이 아닌 단어 개수

w_Swear_kind = 0    # 욕인 단어 종류
w_Non_Swear_kind = 0 # 욕이 아닌 단어 종류


f = open('chat_train_bal.txt','r')
s = f.readline()
for s in f:
    if s[0] != "1":
        s[0].replace('+',"1")
    # -1 , 1로 비속어 있는 문장인지 확인하기
    if s[0] == "1":
       #print("욕 포함 문장:",s[0])    
        s_Swear_Cnt +=1
    elif s[0] == "-":
       #print("욕 포함 아닌 문장:",s[0:2])
        s_Non_Swear_Cnt +=1
    else:
        print("문장끝")
    num = s.find('\t')              # '\t'가 나온 위치를 찾는다
    words = s[num:].replace('+',' ').split() # 공백을 모두 + 로 바꿔서 형태소를 + 로 구분 시켜주기 위해서 replace를 해준다.

    # words가 리스트 형태로 분리 되어 들어간다는것을 알아야한다.
    # 이제 단어에 넣을 차례
    count = 0
    for i in words:          # word 단어를 추출해서 하나씩 비교 한다.
            if s[0] == '-':     # 정상문자일때 사전에 저장

                #  욕이 아닌 단어가 사전에 단어가 있을경우 몇번나오는지 확인 시키기 위함
                
                if words[count] in non_Swear_Dict.keys():
                    non_Swear_Dict[words[count]] += 1   # Dict에다가 넣는다.
                    w_Swear_Cnt += 1                 #

                # 욕이 아닌 단어가 사전에 단어가 존재 하지 않을 경우 
                else:
                    non_Swear_Dict[words[count]] = 1   # Dict에다가 넣을경우 초기값을 1로 지정해준다.
                    w_Swear_Cnt += 1
                    w_Swear_kind  += 1

                # 사전에    
            else:               #비정상문장일때 사전에 저장
                if words[count] in swear_Dict.keys():
                    swear_Dict[words[count]] += 1
                    w_Non_Swear_Cnt+= 1
                else:
                    swear_Dict[words[count]] = 1
                    w_Non_Swear_Cnt += 1
                    w_Non_Swear_kind  += 1
            count +=1            

f.close()
print("욕인 문장 개수: ",s_Swear_Cnt)     # 욕인 문장 개수
print("욕이 아닌 문장 개수 : ",s_Non_Swear_Cnt) # 욕이 아닌 문장 개수

print("욕인 단어 개수 : ",w_Swear_Cnt)     # 욕인 단어 개수
print("욕이 아닌 단어 개수 : ",w_Non_Swear_Cnt) # 욕이 아닌 단어 개수
    
print("욕 단어 종류 : " , w_Swear_kind)    # 욕단어 종류
print("욕이 아닌 단어 종류",w_Non_Swear_kind) # 욕이 아닌 단어 종류

#print("욕 문장 :\n", swear_Dict)           # 욕 문장 리스트
#print("욕 아닌 문장 :\n",non_Swear_Dict)   # 욕 아닌 문장 리스트


#베이지언 로직


Ps = (s_Swear_Cnt+1) / (s_Swear_Cnt + s_Non_Swear_Cnt+2) #욕클라스 확률
Pn = (s_Non_Swear_Cnt+1) / (s_Swear_Cnt + s_Non_Swear_Cnt+2) #정상클라스 확률

print('Ps : ',Ps)
print('Pn : ',Pn)

# SVM


fp = open('chat_test_bal.txt','r')
p = open("t.txt", 'w')


svm_swear = dict()
svm_non_swear = dict()
for s1 in fp:
    #if s1[0] != "1":
    #    s1[0].replace('+',"1")
    # -1 , 1로 비속어 있는 문장인지 확인하기


    
    if s1[0] == "1":
       #print("욕 포함 문장:",s[0])    
        s_Swear_Cnt +=1
    elif s1[0] == "-":
       #print("욕 포함 아닌 문장:",s[0:2])
        s_Non_Swear_Cnt +=1
    else:
        print("문장끝")

    svm_num = s1.find('\t')              # '\t'가 나온 위치를 찾는다
    svm_words = s1[svm_num:].replace('+',' ').split() # 공백을 모두 + 로 바꿔서 형태소를 + 로 구분 시켜주기 위해서 replace를 해준다.
    print(svm_words)
    


    if s1[0] == '-':
        p.write('-1 ')
    else:
        p.write('+1 ')
    
    svm_count = 0
    posi_cnt = 0
    nega_cnt = 0
    
    # 형태소 부분만 찾기위해서  
    
    #svm_num = s1.find('\t')   
    #한글만 추출해버리기 
    #svm_words = re.findall(u'[\uAC00-\uD7A3]+',s1[svm_num:].split())
    
    check = -1
    for a in svm_words:          # word 단어를 추출해서 하나씩 비교 한다.

            if s[0] == '-':     # 정상문자일때 사전에 저장
                
                #  욕이 아닌 단어가 사전에 단어가 있을경우 몇번나오는지 확인 시키기 위함
                
                if svm_words[svm_count] in non_Swear_Dict.keys():
                   # svm_swear[svm_words[svm_count]] += 1  
                    posi_cnt += 1
                    p.write(svm_words[svm_count])
                    p.write(':')
                    #p.write(str(posi_cnt))
                    #p.write(' ')
                    check = 0
                # 욕이 아닌 단어가 사전에 단어가 존재 하지 않을 경우 
                else:
                    #svm_non_swear[svm_words[svm_count]] = 1  
                    p.write(svm_words[svm_count])
                    p.write(':')
                    p.write('0')
                    p.write(' ')
                    posi_cnt = 1
                    
                      # Dict에다가 넣을경우 초기값을 1로 지정해준다.
                # 사전에

                
            else:               #비정상문장일때 사전에 저장

                #p.write('+1')
                if svm_words[svm_count] in swear_Dict.keys():
                   # svm_swear[svm_words[svm_count]] += 1  
                    nega_cnt += 1
                    p.write(svm_words[svm_count])
                    p.write(':')
                    #p.write(str(nega_cnt))
                    #p.write(' ')
                    check = 1
                else:
                    #svm_non_swear[svm_words[svm_count]] = 1
                    p.write(svm_words[svm_count])
                    p.write(':')
                    p.write('0')
                    p.write(' ')
                    nega_cnt = 1
            
            svm_count +=1
            if check == 0:
                p.write(str(posi_cnt))
                p.write('  ')
            elif check == 1:
                p.write(str(nega_cnt))
                p.write('  ')
            check = -1
    p.write('\n')

fp.close()
p.close()








