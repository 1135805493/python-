import urllib
import urllib2
import re



user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
x = 0
for i in range (1,200):
    url = 'http://moe.005.tv/moeimg/list_2_'+str(i)+'.html'
    print url
    try:
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        html = response.read()
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason

    content_pattern = re.compile('<span class="zt_pic".*?<img src="(.*?)">', re.S)
    content_list = re.findall(content_pattern, html)
    for item in content_list:
        print item

        
        '''  爬取网站的图片连接 '''
       

    for imgurl in content_list:
        urllib.urlretrieve(imgurl,'D:\E\%s.jpg' % x)
        x+=1

        '''  下载爬取到的图片连接 '''

        
    input = raw_input()
    if input == "":
        print "下一页"
        continue
    else:
        print "结束"
        break
'''  判断是否要输出下一页,是则输入回车，否则输入其他字符  '''
