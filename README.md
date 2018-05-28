# crawling_project

## WHAT IS THIS?  

계획만 하던 프로젝트를 드디어 진행해보았다-  
**"나레기 인턴 하고싶다-"** 에서 시작해서  
인턴 정보를 주기적으로 알림받고 싶었다:)
>**결론은 학교 홈페이지에 뜨는 인턴 정보를 주기적으로 알림해주는 프로그램**      



## REQUIREMENTS?  

pushbullet  
time  
requests  
datetime  
bs4    


**config.py라는 파일을 notice폴더와 같은 위치에 다음과 같이 작성**
```
userid="자신의 saint아이디"  
passwd="자신의 saint비번"
```



## HOW CAN I USE IT?  

*사실은... 패키지로 만들고 싶었는데.. 그건 좀 더 노력을 해보는 것으로...*  
*git clone을 한다거나... 한다거나...ㅎ......*  

example.py 에다가 자신의 access_token [^1] 을 입력하면 끝~  

---
[^1]: [Pushbullet](https://www.pushbullet.com)을 까셔야 알림을 받아용....  
account 등록하시고, set up your phone & [create access token](https://www.pushbullet.com/#settings/account) 하세용
