
#1 import re = 정규표현식
import re

cnt = 0



def TagRemove():


    fr = open('1.html','r')
    html = fr.readline()
    #html = "<html><head>some header information</head> \ <Body>it's start. <script src='..'>some script</script>  <!-- some comments -->some <b>body</b> contents.. \n<a href='some link'>gogo</a>  그리고 다른 것들..  <script>another</script></Body></html>"
    body = re.search('<body.*/body>', html, re.I|re.S)

    #2 <body></body>의 내용만 잘라내기

    if (body is None):
        print ("No <body> in html")
        exit()
    body = body.group()

    body = re.sub('<script.*?>.*?</script>', '', body, 0, re.I|re.S)
    #body안에 script문 삭제 하기
    # script로  다시 어떤내용이 있을 수 있으며 끝은 </script>로 끝난다는내용


    #3 <body> 안의 <script>....</script> 삭제하기

    # .*? 오면 어떠한 내용이 올수가 있는지 없는지여부이고 0이오는이유는
    # 부합되는 모든 문자열을 지우라는 의미이고, 1을 적게 되면 첫번째
    # 스크립트만 삭제 되게 된다.

    #4 태그 및 주석 삭제 하기

    text = re.sub('<.+?>','',body,0,re.I|re.S)
    print(text)

    #5 공백 제거 하기(\t\r\n,nonspace)
    nospace = re.sub('&nbsp;| |\t|\r|\n', '', text)
    print(nospace)


# 인터프리터 언어는 한줄한줄씩 인식이 가능하기 때문에, 호출하는 순간은
# 그 호출메소드의 뒷쪽에서 해주어야한다

TagRemove()
