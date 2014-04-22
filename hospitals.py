import urllib,urllib2
response=urllib2.urlopen("http://www.justdial.com/Noida/Hospitals")
page=response.read()
from lxml import etree
x=etree.HTML(page)
n3=x.xpath('(//p[@class="jrcw"]/a/text())')
n4=x.xpath('(//span[@class="jcn"]/a/text())')

for i in n3:
	print i
for j in n4:
    print j
    
    
    
    
    n5=x.xpath('//span[@class="jcn"]/a/@href')
    
    for i in range(len(n5)):
	str=n5[i]
	response=urllib2.urlopen(str)
	page1=response.read()
	x1=etree.HTML(page1)
	n6=x1.xpath('//span[@class="fn"]/text()')
	n7=x1.xpath('//a[@class="tel"]')
	for j in range(len(n7)):
		print n7[j],
	print n6
	
	def stripEscape(string):
    """ Removes all escape sequences from the input string """
    delete = ""
    i=1
    while (i<0x20):
        delete += chr(i)
        i += 1
    t = string.translate(None, delete)
    return t
    
    n8=''.join(n6)
    stripEscape(n8)
    
    #working
    for i in range(len(n5)):
	str=n5[i]
	response=urllib2.urlopen(str)
	page1=response.read()
	x1=etree.HTML(page1)
	n6=x1.xpath('//span[@class="fn"]/text()')
	n8=''.join(n6)
	n9=stripEscape(n8)
	n7=x1.xpath('//a[@class="tel"]/text()')
	n10=x1.xpath('//a[@class="tel"]/b/text()')
	print n9,
	if len(n7)==0:
		print n10,
	else:
		for j in range(len(n7)):
			print n7[j],
	print("\n")

