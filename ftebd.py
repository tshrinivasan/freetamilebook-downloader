import xml.etree.ElementTree
import requests
z=0
e = xml.etree.ElementTree.parse('books.xml').getroot()
for atype in e.findall('book'):
    header={'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30'}
    #print atype.find('link').text.rsplit('/',2)[1]
    data=requests.get(atype.find('pdf').text, stream=True,headers=header)
    
    with open(atype.find('link').text.rsplit('/',2)[1]+".pdf",'wb') as fil:
         fil.write(data.content)
         
    print "download book",z
    z=z+1
