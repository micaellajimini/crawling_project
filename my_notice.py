import requests
from datetime import date, timedelta
from bs4 import BeautifulSoup

from config import userid, passwd

error_mes = "error detected!"
login_url = "https://job.sogang.ac.kr/ajax/common/loginproc.aspx"

session = requests.session()

parameters = dict()
parameters['userid'] = userid
parameters['passwd'] = passwd

res = session.post(login_url, data=parameters)
res.raise_for_status()

def crawling(url):
    global message
    message = ""

    try:
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
result2 = crawling(url[:-1]+'2')

if result2 == error_mes:
    print(error_mes)
else:
    result += result2

print(result)