import urllib2
from lxml import etree
def stripEscape(string):
    """ Removes all escape sequences from the input string """
    delete = ""
    i=1
    while (i<0x20):
        delete += chr(i)
        i += 1
    t = string.translate(None, delete)
    return t

def openpage(url):
    """return the etree of the given url"""
    res=urllib2.urlopen(url)
    pg=res.read()
    x=etree.HTML(pg)
    return x

def givehname(hurl):
    """returns the name of hospital"""
    x=openpage(hurl)
    n1=x.xpath('//span[@class="fn"]/text()')
    return n1



def getdetails(just_url):
    response=urllib2.urlopen(just_url)
    page=response.read()
    x=etree.HTML(page)
    n5=x.xpath('//span[@class="jcn"]/a/@href')
    for i in range(len(n5)):
        x1=openpage(n5[i])    
        htp=x1.xpath('//span[@class="fn"]/text()')
        htemp=''.join(htp)
        hname=stripEscape(htemp)
        telat=x1.xpath("//input[@id='lt']/@value")
        telon=x1.xpath("//input[@id='ln']/@value")
        teadd=x1.xpath("//input[@id='where'][@type='hidden'][@name='where']/@value")
        lat=''.join(telat)
        lon=''.join(telon)
        add=''.join(teadd)
        n7=x1.xpath('//a[@class="tel"]/text()')
        n10=x1.xpath('//a[@class="tel"]/b/text()')
        if len(n7)==0:
            if len(n10)==1:
                hno=n10[0]
            else:
                hno=n10[0]
        else:
            hno=n7[0]
        n10=x1.xpath('//a[@class="tel"]/b/text()')
        print hname,'#',lat,'#',lon,'#',add,'#',hno,''
        
just_url='specify the url here.'
for i in range(1,11):
    url=just_url+str(i)
    getdetails(just_url)
    
