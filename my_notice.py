import requests
from datetime import date, timedelta
from bs4 import BeautifulSoup

from config import userid, passwd

login_url = "https://job.sogang.ac.kr/ajax/common/loginproc.aspx"

session = requests.session()

parameters = dict()
parameters['userid'] = userid
parameters['passwd'] = passwd

res = session.post(login_url, data=parameters)
res.raise_for_status()


url = "https://job.sogang.ac.kr/jobs/sogang/intern/default.aspx?page=1"
message = ""

def crawling(url):
    global message
    req = session.get(url)

    try:
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
                if tds[1].get_text() == yesterday.strftime('%Y-%m-%d'):
                    message += tds[2].get_text() + " / "
                    message += tds[3].get_text() + " / "
                    message += tds[5].get_text() + "\n"


        if message == "":
            message = "no new contents\n"
        return message

    except:
        return "error detected"
result = crawling(url)
print(result)