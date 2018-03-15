import math

normDict = dict() #정상
slangDict = dict() #비정상

normCnt = 0 #정상문장의 전체 단어 개수
normKnd = 0 #정상문장의 단어 종류
normStr = 0 #정상문장의 개수
slangCnt = 0 #욕문장의 전체 단어 개수
slangKnd = 0 #욕문장의 단어 종류
slangStr = 0 #욕문장의 개수
isSlang = 0 #욕문장인지 판단
reSlang = 0 #프로그램 결과가 욕인지

A=0
B=0
C=0
D=0 #precision

f= open('chat_test_bal.txt','r')

s = f.readline()
for s in f:

        #맨앞에 +로 바꿔준다 구분시켜주기 위해서
        
        a = s.replace('+',' ')
        if a[0] == '-': #정상문장 개수
                normStr += 1
        else:  #비정상문장 개수
                slangStr += 1
        cnt = 0
        
        while a[cnt] != '\t':           # \t가 아닐때
            cnt+=1
            
        word = a[cnt+1:].replace('\t',' ').split()
        print(word)
        
        count = 0
        for i in word:          # word 단어를 추출해서 하나씩 비교 한다.
            if a[0] == '-':     # 정상문자일때 사전에 저장
                if word[count] in normDict.keys():              
                    normDict[word[count]] += 1   # Dict에다가 넣는다.
                    normCnt += 1                # 
                else:
                    normDict[word[count]] = 1   # Dict에다가 넣을경우 초기값을 1로 지정해준다.
                    normCnt += 1
                    normKnd += 1
            else:               #비정상문장일때 사전에 저장
                if word[count] in slangDict.keys():
                    slangDict[word[count]] += 1
                    slangCnt += 1
                else:
                    slangDict[word[count]] = 1
                    slangCnt += 1
                    slangKnd += 1
            count +=1


#print(normDict)
print(slangDict)
f.close()

print('정상문장 전체 단어 개수 : ', normCnt)
print('정상문장 단어 종류 : ' ,normKnd)
print('정상문장 개수 : ', normStr)
print('욕문장 전체 단어 개수 : ',slangCnt)
print('욕문장 단어 종류 : ' ,slangKnd)
print('욕문장 개수 : ', slangStr)

############### 사전구축 끝 ##############


################### 베이즈 함수 ################


Ps = (slangStr+1) / (slangStr + normStr+2) #욕클라스 확률
Pn = (normStr+1) / (slangStr + normStr+2) #정상클라스 확률


############### Test파일 한줄씩 읽음 ##########

Tf= open('chat_test_bal.txt','r')

Ts = Tf.readline()
for Ts in Tf:
        Ta = Ts.replace('+',' ')
        isSlang = 0
        reSlang = 0
        if Ta[0] != '-': #정상문장
            isSlang = 1  #욕이 맞으면 1
            
        cnt = 0
            
        while Ta[cnt] != '\t':
            cnt+=1

        Tword = Ta[cnt+1:].replace('\t',' ').split()
        #print(Tword)
        count = 0
        Psd = 1 # P( d | C욕 )
        Pnd = 1 # P( d | C정상 )
        for j in Tword:
            saveSvalue = 0 #각 단어의 value값을 저장하는 변수
            saveNvalue = 0

            #P_S 욕사전에 있는지만 확인함
            if Tword[count] in slangDict.keys():#해당단어가 욕사전에 있는지 확인
                saveSvalue = slangDict.get(Tword[count])
                Psd = Psd * ((saveSvalue + 1) / (slangCnt + slangKnd + normKnd))
            else:
                saveSvalue = slangDict.get(Tword[count])
                Psd = Psd * ((0 + 1) / (slangCnt + slangKnd + normKnd))

            #P_N 정상사전에 있는지만 확인함
            if Tword[count] in normDict.keys():
                saveNvalue = normDict.get(Tword[count])
                Pnd = Pnd * ((saveNvalue + 1) / (normCnt + normKnd + slangKnd))
            else:
                saveNvalue = normDict.get(Tword[count])
                Pnd = Pnd * ((0 + 1) / (normCnt + normKnd + slangKnd))
            count += 1
            
        P_S = Ps*Psd
        P_N = Pn*Pnd
        #print(math.log(P_S))
        #print(math.log(P_N))
        if math.log(P_S) > math.log(P_N): #수가 커서 로그로 표현
           # print('욕')
            reSlang = 1
        #else:
           # print('정상')
################# precision ###################
            
        if (isSlang == 0 and reSlang == 0): #둘다 욕이 아닌 경우 A
            A += 1
        elif isSlang == 1 and reSlang == 1: #둘다 욕인 경우 B
            B += 1
        elif isSlang == 0 and reSlang == 1: #결과만 욕인 경우 C
            C += 1
        elif isSlang == 1 and reSlang == 0: #정답만 욕인 경우 D
            D += 1
f.close() 
#####################################################
precision = B/(B+C)
recall = B/(B+D)
measure = 2*precision*recall/(precision+recall)
print('Precision : ',precision)
print('Recall : ', recall)
print('F-Measure : ', measure)
