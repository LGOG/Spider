#Import
import requests
import re
import colorama
from colorama import Fore, Style
​
#Set target
page = requests.get("http://localhost")
​
#Filter words only
words = (re.findall(r"[\w']+", page.text))
​
#Make 2 lists
x1=[]
x2=[]
​
#LV1 scan
#If you find php or html in the take the word before add "." and add the php\html and send a get requert to this website.
a = [i for i,x in enumerate(words) if x == "php" or  x == "html"]
for word in a:
	x1.append(words[word-1])
	x1.append(words[word])
​
#If the word index or other things that I don't need is found just skip it
	if "index" in x1 or "DOCTYPE" in x1 or "body" in x1 or "div" in x1 or x1[0] + "." + x1[1] == "html.html":
		x1 = []
	else:
		lv1 = requests.get("http://localhost/"+ x1[0] + "." + x1[1])
​
#print lv1 name BLUE
		print ("")
		print (Fore.BLUE +"http://localhost/"+ x1[0] + "." + x1[1])
		print(Style.RESET_ALL)
​
#LV2 scan
#Filter LV1 finding to words only
		words2 = (re.findall(r"[\w']+", lv1.text))
		c = [i for i,x in enumerate(words2) if x == "php" or  x == "html"]
​
		for word in c:
			x2.append(words2[word-1])
			x2.append(words2[word])
			if "index" in x2 or "DOCTYPE" in x2 or "body" in x2 or "div" in x2 or x2[0] + "." + x2[1] == "html.html":
				x2 = []
			else:
				print (x2)
				lv2 = requests.get("http://localhost/"+ x2[0] + "." + x2[1])
​
#print lv2 name RED
				print (" ")	
				print (Fore.RED + "http://localhost/"+ x2[0] + "." + x2[1])
				print(Style.RESET_ALL)
​
				print (lv2.text)
#restart the lists and go to the next word
				x1=[]
				x2=[]
​
​
