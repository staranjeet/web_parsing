from lxml import etree
import urllib
req=urllib.urlopen("http://pyvideo.org/category/50/pycon-us-2014")
base_url="http://pyvideo.org"
page=req.read()
x=etree.HTML(page)
vurls=x.xpath('//div[@class="thumbnail-data"]/a/@href')
string=""
for i in range(5):
    newurl=base_url+vurls[i]
    rq=urllib.urlopen(newurl)
    pg=rq.read()
    x1=etree.HTML(pg)
    sname=x1.xpath("//div[@id='sidebar']/dl/dd/div/a/text()")
    n3=x1.xpath("//div[@id='sidebar']/dl/dd/a/text()")
    nurl=n3[1]
    rqq=urllib.urlopen(nurl)
    pgg=rqq.read()
    x2=etree.HTML(pgg)
    subscriber_count=x2.xpath('//span[@class="yt-subscription-button-subscriber-count-branded-horizontal"]/text()')
    views=x2.xpath('//span[@class="watch-view-count "]/text()')
    likes=x2.xpath('//span[@class="likes-count"]/text()')
    dislikes=x2.xpath('//span[@class="dislikes-count"]/text()')
    speaker=''.join(sname)
    sub_c=''.join(subscriber_count)
    vi=''.join(views)
    vi=vi.strip()
    lik=''.join(likes)
    dislik=''.join(dislikes)
    print "Speaker name : %s" % speaker
    print"Subscriber count : %s" % sub_c
    print"Views : %s" % vi
    print"Likes : %s" % lik
    print"Dislikes : %s" % dislik
    
    

