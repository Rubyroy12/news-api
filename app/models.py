class Newsource:
    """
    class  to define news source objects     
    """
    def __init__(self,source,title,description,image,time,link):
        self.source = source
        self.title = title
        self.description = description
        self.image = image
        self.time = time
        self.link = link

class Article:
    """article"""
    def __init__(self,name,description,url):
        self.name = name
        self.description = description
        self.url = url
