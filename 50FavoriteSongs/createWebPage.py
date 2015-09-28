
class WebPageCreator():
    def create(self):
        self.readUrls()
        self.readTitles()
        self.makeWebPage()
        
    def readUrls(self):
        self.urls = self.readFile('urls.txt')
    
    def readTitles(self):
        self.titles = self.readFile('titles.txt')
    
    def readFile(self, filename):
        with open(filename, 'r') as f:
            data = f.readlines()
        return data
    
    def savePage(self, filename, content):
        with open(filename, 'w') as f:
            f.write(content)
           
    def makeWebPage(self):
        
        webPage = self.getStartPart()
        for i in range(len(self.urls)):
            #webPage += self.getEmbededVideoPart(self.urls[i].strip(), self.titles[i].strip())
            webPage += self.getLink(self.urls[i].strip(), self.titles[i].strip())
            
            
        webPage += self.getEndPart()
        
        self.savePage('allLinks.html', webPage)
    
    def getStartPart(self):
        start = """<html>
  <head>
    <title>50 Favorite Songs</title>
  </head>
  <body>
  
"""
        return start
    
    def getEndPart(self):
        end = """
  </body>
</html>"""
        return end
    
    def getEmbededVideoPart(self, url, title):
        linkAddress = 'https://www.youtube.com/watch?v=%s'
        thumbnail = '<img src="http://i1.ytimg.com/vi/%s/1.jpg" alt="%s" title="%s" />'
        
        imgLink = '    <a href="%s">%s</a>\n' % (linkAddress, thumbnail)
        imgLink % (url, url, title, title )
        
        return imgLink
    
    
    def getLink(self, url, title):
        linkAddress = 'https://www.youtube.com/watch?v=%s' % url
        
        imgLink = '    <a href="%s">%s</a><br />\n' % (linkAddress, title)
        
        return imgLink
    
    
if __name__ == "__main__":
    creator = WebPageCreator()
    creator.create()
    