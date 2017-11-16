Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib
>>> import urllib2
>>> url = 'http://www.4399.com/'
>>> user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
>>> referer = 'https://www.baidu.com/link?url=gdp5S5ec7JxIIqZ8txLdoK445NcfFQduTbguFoUT8Iy&wd=&eqid=ad5c0ea900006dca000000055a0cf9dc'
>>> request = urllib2.Request(url,  headers = {'user_Agent':user_agent, 'Referer':referer})
>>> response = urllib2.urlopen(request)
>>> page = response.read(1000)
>>> page
'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\r\n<html xmlns="http://www.w3.org/1999/xhtml">\r\n<head>\r\n<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />\r\n<title>\xd0\xa1\xd3\xce\xcf\xb7,4399\xd0\xa1\xd3\xce\xcf\xb7,\xd0\xa1\xd3\xce\xcf\xb7\xb4\xf3\xc8\xab,\xcb\xab\xc8\xcb\xd0\xa1\xd3\xce\xcf\xb7\xb4\xf3\xc8\xab - www.4399.com \xd6\xd0\xb9\xfa\xc1\xec\xcf\xc8\xb5\xc4\xd3\xce\xcf\xb7\xc6\xbd\xcc\xa8</title>\r\n<meta name="description" content="4399\xca\xc7\xd6\xd0\xb9\xfa\xc1\xec\xcf\xc8\xb5\xc4\xd0\xa1\xd3\xce\xcf\xb7\xd7\xa8\xd2\xb5\xcd\xf8\xd5\xbe,\xc3\xe2\xb7\xd1\xce\xaa\xc4\xe3\xcc\xe1\xb9\xa9\xd0\xa1\xd3\xce\xcf\xb7\xb4\xf3\xc8\xab,4399\xc2\xe5\xbf\xcb\xcd\xf5\xb9\xfa\xd0\xa1\xd3\xce\xcf\xb7,\xcb\xab\xc8\xcb\xd0\xa1\xd3\xce\xcf\xb7,\xc1\xac\xc1\xac\xbf\xb4\xd0\xa1\xd3\xce\xcf\xb7,\xc8\xfc\xb6\xfb\xba\xc5,\xb0\xc2\xc0\xad\xd0\xc7,\xb0\xc2\xc6\xe6\xb4\xab\xcb\xb5\xd0\xa1\xd3\xce\xcf\xb7,\xd4\xec\xc3\xce\xce\xf7\xd3\xce3\xb5\xc8\xd7\xee\xd0\xc2\xd0\xa1\xd3\xce\xcf\xb7\xa1\xa3" />\r\n<meta name="keywords" content="\xd0\xa1\xd3\xce\xcf\xb7,4399\xd0\xa1\xd3\xce\xcf\xb7\xb4\xf3\xc8\xab,\xd4\xda\xcf\xdf\xd0\xa1\xd3\xce\xcf\xb7" />\r\n<meta property="og:type" content="image"/>\r\n<meta property="og:image" content="http://imga1.5054399.com/upload_pic/2015/7/10/4399_11174921955.jpg" />\r\n<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE7" />\r\n<meta property="qc:admins" content="5303563577643116375" />\r\n<meta property="wb:webmaster" content="9a9751c8cd36bccb" />\r\n<link rel="alternate" media="only screen and(max-width: 640px)" '
>>> 
