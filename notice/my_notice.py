from pushbullet import Pushbullet
import time
import requests
from datetime import date, timedelta
from bs4 import BeautifulSoup
# id, pw is important
from config import userid, passwd


class PushNote(object):
    def __init__(self, access_token):
        self.error_mes = "error detected!"
        self.login_url = "https://job.sogang.ac.kr/ajax/common/loginproc.aspx"
        self.url = "https://job.sogang.ac.kr/jobs/sogang/intern/default.aspx?page=1"
        self.access_token = access_token

        self.session = requests.session()

        self.parameters = dict()
        self.parameters['userid'] = userid
        self.parameters['passwd'] = passwd

        res = self.session.post(self.login_url, data=self.parameters)
        res.raise_for_status()

    def do_crawling(self, url):
        message = ""

        try:
            # can access page after login
            req = self.session.get(url)
            req.raise_for_status()

            soup = BeautifulSoup(req.content, "html.parser")
            trs = soup.find("div", {"id": "contents"}).find("tbody").find_all('tr')
            for tr in trs:
                tds = tr.find_all('td')
                if tds[1].find('img') is not None:
                    message += tds[2].get_text() + " / "
                    message += tds[3].get_text() + " / "
                    message += tds[5].get_text() + "\n\n"
                else:
                    # recent notices(yesterday, today) / one time in a day
                    yesterday = date.today() - timedelta(1)
                    if tds[1].get_text() == yesterday.strftime('%Y-%m-%d') or \
                                    tds[1].get_text() == date.today().strftime('%Y-%m-%d'):
                        message += tds[2].get_text() + " / "
                        message += tds[3].get_text() + " / "
                        message += tds[5].get_text() + "\n\n"

            return message

        except:
            return self.error_mes

    def run(self):
        pb = Pushbullet(self.access_token)

        while True:
            result = self.do_crawling(self.url)
            result2 = self.do_crawling(self.url[:-1] + '2')  # slicing

            if result2 == self.error_mes:
                pb.push_note(u"Internship notices", self.error_mes)
            else:
                result += result2

            if result == "":
                pb.push_note(u"Internship notices","no recent notices")
            else:
                pb.push_note(u"Internship notices",result)

            time.sleep(48600)

