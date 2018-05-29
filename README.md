# crawling_project

## WHAT IS THIS?  

계획만 하던 프로젝트를 드디어 진행해보았다-  
**"나레기 인턴 하고싶다-"** 에서 시작해서  
인턴 정보를 주기적으로 알림받고 싶었다:)
>**결론은 학교 홈페이지에 뜨는 인턴 정보를 주기적으로 알림해주는 프로그램**      



## REQUIREMENTS?  

pushbullet  
requests  
datetime  
bs4    


**config.py라는 파일을 notice폴더와 같은 위치에 다음과 같이 작성**
```
userid="자신의 saint아이디"  
passwd="자신의 saint비번"
```
  
*설치된 모듈 버전 확인*
`pip freeze`

## HOW CAN I USE IT?  

*사실은... 패키지로 만들고 싶었는데.. 그건 좀 더 노력을 해보는 것으로...*  
*git clone을 한다거나... 한다거나...ㅎ......*  

example.py 에다가 자신의 access_token[^1] 을 입력하면 끝~     
**example.py**  
```
from notice import my_notice

gp = my_notice.PushNote("access_token")
gp.run()
```
  
---
#### Background 실행
  
nohup 명령어로 시도하다가 importerror가 계속발생 - 망
실행파일로 바꿔도 importerror가 계속발생
*어떻게 해야할까 ㅠㅠㅠㅠㅠㅠ*    

#### Import Problem

vi ~/.bash_profile 
```
~~~~~
export PYTHONPATH="프로젝트경로"
~~~~~
```    
#### 삽질

pip 설치를 하고 list까지 확인했는데도 module import error가 계속 발생  
-> pycharm에서는 실행되고 terminal에서는 안됨  
-> interpreter가 달랐음(anaconda install 이후 path가 꼬임)  
-> .bash_profile 을 보니 python3 보다 anaconda path 설정이 더 뒤에 있음  
-> 순서를 바꿔주면 됨 (둘 다 패키지를 찾을 수 있으면 덮어쓰기가 되는건가...)    

---
[^1]: [Pushbullet](https://www.pushbullet.com)을 까셔야 알림을 받아용....  
account 등록하시고, set up your phone & [create access token](https://www.pushbullet.com/#settings/account) 하세용
