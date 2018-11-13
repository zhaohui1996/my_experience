import urllib.request#爬取使用的包,网络请求模块
import re#解析需要使用到正则表达式

stock_CodeUrl = 'http://quote.eastmoney.com/stocklist.html'#东方财富网股票页面(要爬取的目的地址)
#获取股票代码列表
def urlTolist(url):#定义获取url的函数
    allCodeList = []#定义一个列表来保存需要爬取具体的url
    html = urllib.request.urlopen(url).read()#请求,获取HTML网页
    html = html.decode('gbk')#转码
    s = r'<li><a target="_blank" href="http://quote.eastmoney.com/\S\S(.*?).html">'
    pat = re.compile(s)#创建正则表达式的模板
    code = pat.findall(html)#正则表达式计算
    for item in code:
        if item[0]=='6' or item[0]=='3' or item[0]=='0':#6(上海证交所),0(深圳证交所),3(创业板)
            allCodeList.append(item)
    return allCodeList#返回一个列表


def get_data():
    allCodelist = urlTolist(stock_CodeUrl)#获取全部股票代码
    start = '20180701'#设置时间段
    end = '20180730'
    for code in allCodelist:#遍历全部代码,调用163接口获得数据
        print('正在获取%s股票数据...' % code)
        if code[0] == '6':
            url = 'http://quotes.money.163.com/service/chddata.html?code=0' + code + \
                  '&start=' + start + '&end=' + end + '&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
        else:
            url = 'http://quotes.money.163.com/service/chddata.html?code=1' + code + \
                  '&start=' + start + '&end=' + end + '&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
        urllib.request.urlretrieve(url, 'd:\\fei\\stock\\' + code + '_' + end + '.csv')
if __name__=='__main__':
    get_data()
#为了保证操作正常运行,需要确保D盘下存在\fei\\stock文件夹