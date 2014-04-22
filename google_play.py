import urllib
from lxml import etree
inp='y'
while(inp=='y'):
    print('Enter your choice:')
    print ('1. Top Paid\n2. Top Free\n3. Top Grossing\n4. Top New Paid\n5. Top New Free')
    choice=int(raw_input())
    if choice==1:
        page=urllib.urlopen('https://play.google.com/store/apps/collection/topselling_paid').read()
    
    elif choice==2:
        page=urllib.urlopen('https://play.google.com/store/apps/collection/topselling_free').read()
    
    elif choice==3:
        page=urllib.urlopen('https://play.google.com/store/apps/collection/topgrossing').read()
    
    elif choice==4:
        page=urllib.urlopen('https://play.google.com/store/apps/collection/topselling_new_paid').read()
    
    elif choice==5:
        page=urllib.urlopen('https://play.google.com/store/apps/collection/topselling_new_free').read()
    
    else:
        print("You didn't entered a valid choice")
        break

    x=etree.HTML(page)
    name=x.xpath('(//a[@class="title"]/text())')
    rank=x.xpath("//div[@class='ordinal-value']/text()")
    dev=x.xpath('//a[@class="goog-inline-block"]/text()')
    
    print("Rank ".rjust(5)+"Name of the application ".center(40) + "Developer's Name".center(25))
    for i in range(20):
        print(rank[i].center(5)+ name[i].center(40)+dev[i].center(25))

    print("Do you want to continue[y/n]")
     
     
    inp=str(raw_input())

