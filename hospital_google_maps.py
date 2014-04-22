"""google maps parsing"""
import urllib2
import simplejson as json
count=1
base="http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=" 
f=open('list1.txt','r')
for line in f:
    #print count
    count=count+1
    str=line
    if str.find('&')!=-1:
        count=count+1
        continue
    co=str.find(',')
    if co!=-1:
        str=str[:co]
    str=str.replace(' ','+')
    hurl=base+str
    response=urllib2.urlopen(hurl)
    hpage=response.read()
    js=json.loads(hpage)
    c,d=0,0
    iuy=len(js['results'])
    print(iuy)
    for i in js['results']:
        flag=0
        flag2=0
        n=js['results'][c]['address_components']
        le=len(n)
        for i in range(le):
	        if n[i]['long_name']=="India":
		        flag=1
		        break
        for i in range(le):
	        if n[i]['long_name']=="Noida":
		        flag2=1
		        break
        flag= flag and flag2
        if flag==1:
            print n[0]['long_name'],
            print '#',
            print js['results'][c]['formatted_address'],
            print '#',
            print js['results'][c]['geometry']['location']['lat'],
            print '#',
            print js['results'][c]['geometry']['location']['lng']
            
        c=c+1
