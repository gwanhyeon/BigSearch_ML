import re





string = "-1 마졷 비매만그때 안했었어도 얼라랑 계속 겜 하셨을텐데 	마졷/UNK	비매만/UNK+그때/NNG	안/MAG+하/VA+ㅆ었어도/E	얼라랑/UNK	계속/NNG	겜/UNK	하/NNP+셨을/P+SPC/SPC+터/NNG+인데/P"
result_sp = ""
exception= re.compile('[^r-ㅣ가-힣]+')
result = exception.sub('',string)
result_sp =result

while True:
    result_sp = result_sp.replace(" ","")
    if result_sp == result:
        break;
    result = result_sp

print(result)


string = 
