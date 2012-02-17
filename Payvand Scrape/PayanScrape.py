#Author: Javed Ahamed (University of Maryland Programming Club)

from BeautifulSoup import BeautifulSoup #BeautifulSoup is a html parser
import urllib2, re #urllib2 lets you open url html and re is for regular expressions

#For the pages we are trying to scrape, look at http://www.payvand.com/yp/pk/search.html

#These are the states that you can search listings in:
urlmodifiers = ["Balochistan", "Islamabad", "North-West+Frontier", "Punjab", "Sindh"]

#This function does the scraping/writing to file for the Business listings
def computeBus(url, file):

  #uncomment the folowing lines to add proxy support with TOR/privoxy  
  #proxy_handler = urllib2.ProxyHandler({'http':'localhost:8118'})
  #opener = urllib2.build_opener(proxy_handler)
  
  html = urllib2.urlopen(url).read()

  soup = BeautifulSoup(html)
  soupL = soup.findAll('td') #this splits the html file by its table elements

  #Deletes the first Country = Pakistan Entry that we should not scrape
  del soupL[0]

  fout = open(file, "a")

  for var in xrange(len(soupL)):
    p = re.compile(r"name: [^<]+")
    nameL = p.findall(str(soupL[var]))
		    
    p = re.compile(r'mailto:(.*?)"')
    emailL = p.findall(str(soupL[var]))
    
    p = re.compile(r'url: <a href="(.*?)"')
    urlL = p.findall(str(soupL[var]))
    
    p = re.compile(r"addr: [^<]+")
    addrL = p.findall(str(soupL[var]))
    
    p = re.compile(r"city: [^<]+")
    cityL = p.findall(str(soupL[var]))
	    
    p = re.compile(r"state: [^<]+")
    stateL = p.findall(str(soupL[var]))
    
    p = re.compile(r"tel: [^<]+")
    telL = p.findall(str(soupL[var]))
    
    p = re.compile(r"fax: [^<]+")
    faxL = p.findall(str(soupL[var]))
    
    try:
      fout.write(nameL[0]+"|")
    except IndexError:
      fout.write("name: NOT LISTED|")
    try:
      fout.write("email: "+emailL[0]+"|")
    except IndexError:
      fout.write("email: NOT LISTED|")
    try:
      fout.write("url: "+urlL[0]+"|")
    except IndexError:
      fout.write("url: NOT LISTED|")
    try:
      fout.write(addrL[0]+"|")
    except IndexError:
      fout.write("addr: NOT LISTED|")
    try:
      fout.write(cityL[0]+"|")
    except IndexError:
      fout.write("city: NOT LISTED|")
    try:
      fout.write(stateL[0]+"|")
    except IndexError:
      fout.write("state: NOT LISTED|")
    try:
      fout.write(telL[0]+"|")
    except IndexError:
      fout.write("tel: NOT LISTED|")
    try:
      fout.write(faxL[0]+"|")
    except IndexError:
      fout.write("fax: NOT LISTED|")
    
    fout.write("\n")
    
  fout.close()

#This function does the scraping/writing to file for the Individual listings
def computeInd(url, file):

  #proxy_handler = urllib2.ProxyHandler({'http':'localhost:8118'})
  #opener = urllib2.build_opener(proxy_handler)
  
  html = urllib2.urlopen(url).read()
  
  soup = BeautifulSoup(html)
  soupL = soup.findAll('td')

  #Deletes the first Country = Pakistan Entry
  del soupL[0]

  fout = open(file, "a")

  for var in xrange(len(soupL)):
    p = re.compile(r'<b>(.*?)</b>')
    nameL = p.findall(str(soupL[var]))
    
    p = re.compile(r"occupation: [^<]+")
    occupationL = p.findall(str(soupL[var]))
    
    p = re.compile(r"specialty: [^<]+")
    specialtyL = p.findall(str(soupL[var]))
    
    p = re.compile(r"company: [^<]+")
    companyL = p.findall(str(soupL[var]))
    
    p = re.compile(r'mailto:(.*?)"')
    emailL = p.findall(str(soupL[var]))
    
    p = re.compile(r'url: <a href="(.*?)"')
    urlL = p.findall(str(soupL[var]))
    
    p = re.compile(r"addr: [^<]+")
    addrL = p.findall(str(soupL[var]))
    
    p = re.compile(r"city: [^<]+")
    cityL = p.findall(str(soupL[var]))
    
    p = re.compile(r"state: [^<]+")
    stateL = p.findall(str(soupL[var]))
    
    p = re.compile(r"tel: [^<]+")
    telL = p.findall(str(soupL[var]))
    
    p = re.compile(r"fax: [^<]+")
    faxL = p.findall(str(soupL[var]))
    
    try:
      fout.write(nameL[0]+"|")
    except IndexError:
      fout.write("name: NOT LISTED|")
    try:
      fout.write(occupationL[0]+"|")
    except IndexError:
      fout.write("occupation: NOT LISTED|")
    try:
      fout.write(specialtyL[0]+"|")
    except IndexError:
      fout.write("specialty: NOT LISTED|")
    try:
      fout.write(companyL[0]+"|")
    except IndexError:
      fout.write("company: NOT LISTED|")
    try:
      fout.write("email: "+emailL[0]+"|")
    except IndexError:
      fout.write("email: NOT LISTED|")
    try:
      fout.write("url: "+urlL[0]+"|")
    except IndexError:
      fout.write("url: NOT LISTED|")
    try:
      fout.write(addrL[0]+"|")
    except IndexError:
      fout.write("addr: NOT LISTED|")
    try:
      fout.write(cityL[0]+"|")
    except IndexError:
      fout.write("city: NOT LISTED|")
    try:
      fout.write(stateL[0]+"|")
    except IndexError:
      fout.write("state: NOT LISTED|")
    try:
      fout.write(telL[0]+"|")
    except IndexError:
      fout.write("tel: NOT LISTED|")
    try:
      fout.write(faxL[0]+"|")
    except IndexError:
      fout.write("fax: NOT LISTED|")
    
    fout.write("\n")
    
  fout.close()
  
#main program loop
for programIters in xrange(len(urlmodifiers)):
  computeBus("http://www.payvand.com/cgi-bin/SearchPay.cgi?co=pk&code=bus&state="+urlmodifiers[programIters]+"&city=&string=", "payanbus.txt")
  computeInd("http://www.payvand.com/cgi-bin/SearchPay.cgi?co=pk&code=ind&state="+urlmodifiers[programIters]+"&city=&string=", "payanind.txt")
