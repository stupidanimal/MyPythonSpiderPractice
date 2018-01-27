class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
    def has_new_url(self):
        return self.new_url_size()!=0
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
    def add_new_url(self,urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.new_urls.add(url)
    def new_url_size(self):
        return len(self.new_urls)
    def old_url_size(self):
        return len(self.old_urls)