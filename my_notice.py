import requests
from datetime import date, timedelta
from bs4 import BeautifulSoup
# 내 id와 pw는 소중하니까
from config import userid, passwd

error_mes = "error detected!"
# 크롤링을 위해 source를 뒤지다보니 이 url에 post method으로 userid, passwd를 보낸다는 것을 발견
login_url = "https://job.sogang.ac.kr/ajax/common/loginproc.aspx"

# 쿠키가 웹 브라우저에 사용자의 상태를 유지하기 위한 정보를 저장했다면,
# 세션은 웹 서버 쪽의 웹 컨테이너에 상태를 유지기 위한 정보를 저장한다

# 사용자의 정보를 유지하기 위해서는 쿠키보다 세션을 사용한 웹 브라우저가
# 웹 서버의 상태 유지가 훨씬 안정적이고 보안상의 문제도 해결할 수 있다
session = requests.session()

parameters = dict()
parameters['userid'] = userid
parameters['passwd'] = passwd

res = session.post(login_url, data=parameters)
res.raise_for_status() # 응답상태가 ok가 아니라면 에러발생

# 로그인 이후의 세션

def crawling(url):
    global message
    message = ""

    try:
        # 이제 로그인 이후에 접근할 수 있는 페이지를 접근할 수 있다
        req = session.get(url)
        req.raise_for_status()

        soup = BeautifulSoup(req.content, "html.parser")
        trs = soup.find("div", {"id":"contents"}).find("tbody").find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            if tds[1].find('img') is not None:
                message += tds[2].get_text() + " / "
                message += tds[3].get_text() + " / "
                message += tds[5].get_text() + "\n"
            else:
                # 어제오늘 새로운 뉴스를 알려줌 - 하루에 한번씩 알람뜨게 할 예정
                yesterday = date.today() - timedelta(1)
                if tds[1].get_text() == yesterday.strftime('%Y-%m-%d') or tds[1].get_text() == date.today().strftime('%Y-%m-%d'):
                    message += tds[2].get_text() + " / "
                    message += tds[3].get_text() + " / "
                    message += tds[5].get_text() + "\n"

        return message

    except:
        return error_mes

url = "https://job.sogang.ac.kr/jobs/sogang/intern/default.aspx?page=1"
message = ""

result = crawling(url)
result2 = crawling(url[:-1]+'2') # slicing

if result2 == error_mes:
    print(error_mes)
else:
    result += result2

if result == "":
    print("no recent notices")
else:
    print(result)