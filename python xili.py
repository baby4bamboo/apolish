import re,urllib2
url="http://www.pythonchallenge.com/pc/def/equality.html"
thestring=urllib2.urlopen(url).read()
thepatten='[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]'
m=re.findall(thepatten,thestring)
print ''.join(m)



