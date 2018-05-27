from pushbullet import Pushbullet
import notice.my_notice.crawling as nt
import time

class Pushnote(object):
    def __init__(self, access_token):
        self.access_token = access_token

    def run(self):
        pb = Pushbullet(self.access_token)

        while True:
            result = nt.do_crawling(self.url)
            result2 = nt.do_crawling(self.url[:-1] + '2')  # slicing

            if result2 == nt.error_mes:
                pb.push_note(u"Internship notices",nt.error_mes)
            else:
                result += result2

            if result == "":
                pb.push_note(u"Internship notices","no recent notices")
            else:
                pb.push_note(u"Internship notices",result)

            time.sleep(60)

