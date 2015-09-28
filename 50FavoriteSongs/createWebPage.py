
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
        start = """<html>
  <head>
    <title>50 Favorite Songs</title>
  </head>
  <body>
"""
        end = """
  </body>
</html>"""

        linkAddress = 'https://www.youtube.com/watch?v=%s'
        thumbnail = '<img src="http://i1.ytimg.com/vi/%s/1.jpg" alt="%s" title="%s" />'
        
        imgLink = '    <a href="%s">%s</a>\n' % (linkAddress, thumbnail)
        
        
        webPage = start
        for i in range(len(self.urls)):
            webPage += imgLink % (self.urls[i].strip(), self.urls[i].strip(), self.titles[i].strip(), self.titles[i].strip() )
            
        webPage += end
        
        self.savePage('allLinks.html', webPage)
    
if __name__ == "__main__":
    creator = WebPageCreator()
    creator.create()
    