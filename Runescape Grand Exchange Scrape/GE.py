#Author: Javed Ahamed (University of Maryland Programming Club)
#This script was built to scrape items/prices off of Runescape's Grand Exchange market to try to game it by looking at current market prices and seeing where the highest profit margins were.
#http://services.runescape.com/m=itemdb_rs/g=runescape/frontpage.ws

import urllib2, re, string, sqlite3

db = sqlite3.connect("/home/javed/Desktop/GE/geDB")
cursor = db.cursor()
cursor.execute("CREATE table items (name text, price double, alch text)")

for character in "A":
	url = "http://itemdb-rs.runescape.com/results.ws?query=&sup=Initial%20Letter&cat="+character+"&sub=All&page=1&vis=1&order=1&sortby=name&price=&members="
	html = urllib2.urlopen(url).read()

	reg = re.compile(r'<a href=".*">(\d+)<')
	maxpages = reg.findall(html)

	for pagenum in range(1, int(maxpages[-1:][0])+1):
		url = "http://itemdb-rs.runescape.com/results.ws?query=&sup=Initial%20Letter&cat="+character+"&sub=All&page="+str(pagenum)+"&vis=1&order=1&sortby=name&price=&members="
		html = urllib2.urlopen(url).read()

		reg = re.compile(r'viewitem.ws.obj=.+"> (.*)</a>')
		items = reg.findall(html)

		reg = re.compile('<td>(\d+.*)</td>')
		prices = reg.findall(html)

		hqurl = "http://www.runehq.com/databasesearch.php?db=item"
		hqhtml = urllib2.urlopen(hqurl).read()

		for index in range(len(prices)):
			items[index] = string.replace(items[index], "'", "''")
			prices[index] = string.replace(prices[index], ",", "")
			if prices[index][-2:] == "k ":
				prices[index] = float(prices[index][:-2]) * 1000
			elif prices[index][-3:] == "m  ":
				prices[index] = float(prices[index][:-3]) * 1000000
			else:
				prices[index] = float(prices[index])

		for index in range(len(items)):
			reg = re.compile(r'href="(.*)">'+items[index]+'<')
			hqlink = reg.findall(hqhtml)
			print(hqlink)
			if(len(hqlink) != 0):
				hqlink[0] = string.replace(hqlink[0], "amp;", "")
				alchhtml = urllib2.urlopen("http://www.runehq.com"+hqlink[0]).read()
				reg = re.compile(r"<td class='smallrow2'>(\d.*)</td>")
				alchprice = reg.findall(alchhtml)
				cursor.execute("INSERT into items values('%s', %f, '%s')" % (items[index], prices[index], alchprice[-1:][0]))
			else:
				cursor.execute("INSERT into items values('%s', %f, '%s')" % (items[index], prices[index], 'no alch price'))
			db.commit()

cursor.close()
