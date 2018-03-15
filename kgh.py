import re
import string
print('##### read 함수 #####')
f = open('chat_train_bal.txt', 'r')
#s = f.read()


d_list = ["시발","병신","또라이","장애인","부모님","니미","미친",'년','놈','쉬발','삐리리','개년','좆']
cnt = 0
dic = ['ㅅㅂ','서든']
a = {'a':[1,2,3]}
print("a",a)


#print(d['1'])
#print(d['-1'])

#맨처음문자 어떤 건지 확인 하기
# 문자열 분리 시키기
# 문자열의 위치를 가져온다.
FuckCheck = 0
NotFuckCheck = 0
FuckCheckNum =0;
list_Fucknum=[]
char_num = 0
performance = []

while True:
    #파일 읽기
    s = f.readline()
    if not s :       
        break
    div = s[0 : 2]

    # -1 , 1로 비속어 있는 문장인지 확인하기
    if s[0] == "1":
       # print("욕 포함 문장:",s[0])
        compare = s[0]
        FuckCheck +=1
    elif s[0] == "-":
       # print("욕 포함 아닌 문장:",s[0:2])
        compare = s[0:2]
        NotFuckCheck +=1
    else:
        print("예외")

    # 형태소 부분만 찾기위해서  
    num = s.find('\t')

    #한글만 추출해버리기 
    words = re.findall(u'[\uAC00-\uD7A3]+',s[num:])
    
    #print("words",words)
    char_num += len(words)

    #d_list에 있는 값에 출현 빈도수 확인
    tt=0
    tt+=1
    
    inter = list(set(words) & set(d_list))
    performance.append(len(inter))
    #print("performance",performance)
   
   # resultlist =[]
   # for s in d_list:
   #     if "서든어택" in s:
   #         resultlist.append(s)
   #         print(resultlist)


    rrr = list(set(words) & set(d_list))
    print(len(rrr))
    if len(rrr) >=1:
        print("비속어가 존재합니다")
        FuckCheckNum+=1
    elif len(rrr) == 0:
        print('비속어가 존재하지 않습니다')
        
    
    #if list(set(words) & set(d_list)):
        
     #   print("비교해보자 ",list(set(words) & set(d_list)))

                
   # if "서든어택" in d_list:
       # print("욕이 포함 되어 있다")
        #print(words in d.values().index())
    #else:
        #print('욕이 포함 되어 있지 않다')
        #print(words in d.values())
    

    #check = d['1'].find(words)
    #print('있는 단어인가?',check)
   
    
    #print(s[num:].split(' '))
    #print(test)
        
    #s.strip()
    #print(num) \t등장한 문자열 위치를 가져온다.
  
    cnt+=1
    #print ("형태소 분리: ",cnt,s[num:].strip())
    
    list_Fucknum.append(FuckCheckNum)
    FuckCheckNum =0;
    #print("test",list_Fucknum)
    
#hi = s.split('\t')
#print(hi)

print("############베이즈정리###########")
print("총문장의 개수 :",cnt)      # 맨마지막 문자열 빼준다 ( 총 문장의 개수)
print("총 문자 개수",char_num)
print('욕이 포함된 문장의 개수',FuckCheck)
print('욕이 포함되지 않은  문장의 개수',NotFuckCheck)
cnt_1 = 0
print('욕 포함 문자 개수',len(list_Fucknum))
for i in list_Fucknum:
    cnt_1 = cnt_1 + int(i)
print('욕 포함되지 않은 문자의 개수 :',char_num-len(list_Fucknum))

#욕이란 단어가 있을 때 비속어 인지아닌지를 구별 할 확률
#총 = 문장 13개
#p(욕일경우) FuckCheck 개수
#p(욕이 아닐경우) NotFuckCheck 개수



# 성능 평가









f.close()
