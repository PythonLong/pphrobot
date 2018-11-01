import datetime
import  re
import  requests
from urllib.request import quote
class Command:



    def gettime(self):
        pass


    ##图书管理
    def book(self,keyword):
        url = "http://172.16.209.168/NTBookRetr.aspx?page=1&Index=4&KeyWord=%s&LocLmt=&SrchTab=0&Acurate=0&nSort=0&nSrch=" % keyword
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
        }
        r = requests.get(url, headers=head)

        if r.status_code != 200:
            return "网页获取错误!"

        listresult = re.findall("<font color=\"#0db3fd\" style=\"font-family: 幼圆;font-size: 15px;\">(.+?)</a></font>",
                                r.text)

        textresult = '\n'.join(listresult)

        return textresult

    ##有道翻译
    def fanyi(self,item):
        key = {'type': "AUTO",
               'i': item,
               "doctype": "json",
               "version": "2.1",
               "keyfrom": "fanyi.web",
               "ue": "UTF-8",
               "action": "FY_BY_CLICKBUTTON",
               "typoResult": "true"}
        url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
        r = requests.post(url, data=key)
        d = r.json()
        return d["translateResult"][0][0]['tgt']

    ##返回课表
    def classtable(self,day):
        table = {
            '周一': '0102:数据结构实验(2-16周 A501)\n0304:数据结构(1-16周 A605)\n0708:马克思主义原理(1-16周 B205)',
            '周二': '0102:经济学(1-16周 A605)\n0304:数据结构(1-8周 A602)',
            '周三': '0102:计算机网络(1-16周 A602)\n0304:经济学(1-16周 A602)\n0304:web开发技术(1-16周 A601)\n0506:大学体育(1-13周)',
            '周四': '0102:计算机网络(1-4周 A6017-15周 A516)\n0304:大学英语(1-16周 B206)\n0506:概率论(1-4周 6-11周 C504)',
            '周五': '0102:Web开发技术(1-4周 A601)\n0304:概率论(1-4周 6-11周 C504)'
        }
        return table.get(day,"星期错误")

    ##百科
    def baike(self,keyword):
        head={
       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"}
        url = 'https://baike.baidu.com/item'+'/'+ keyword
        r=requests.get(url,headers = head)
        r.encoding = 'utf8'

        result = re.findall("<meta name=\"description\" content=\"(.+?)\">",r.text)

        if result:
            return result[0] + '\n' + '详细请访问:' + quote(url,safe=";/?:@&=+$,",encoding="utf8")
        else:
            return "未找到结果"

    def __init__(self):
        self.map = {'图书':self.book,'翻译':self.fanyi,'百科':self.baike,'课表':self.classtable}


c = Command()

if __name__ == "__main__":
    print(c.baike('westboy'))


    # print(c.fanyi('I love you'))
    # print(c.book('龙族'))
