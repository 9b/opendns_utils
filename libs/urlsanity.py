import StringIO, csv, zipfile, urllib2

class url_sanity():
    def __init__(self,urls,verbose):
        self._url_file = urls
        self._urls = []
        self._max_list = 10000
        self._top_sites = []
        self._alexa_link = "http://s3.amazonaws.com/alexa-static/top-1m.csv.zip"  
        self.verbose = verbose
        
    def check_critical(self):
        f = open(self._url_file,"r")
        lines = f.readlines()
        if self.verbose:
            print "[*] Checking URL list for global blocks"
        for line in lines:
            if line.strip() == "." or line.strip() == "www":
                self._proceed = False
                return self._proceed
            else:
                self._proceed = True
        return self._proceed
                
    def check_top10K(self):
        matches = None
        if self.verbose:
            print "[*] Checking URL list against top 10,000 Alexa sites"        
        self.get_top_sites()
        matches = set(self._urls) & set(self._top_sites)
        if matches != None:
            self._proceed = False
            return self._proceed
        else:
            self._proceed = True
        return self._proceed
                
    def get_top_sites(self):
        f = urllib2.urlopen(self._alexa_link)
        data = self.open_web_zip(f)
        self.read_top_list(data)
        
    def open_web_zip(self, infile):
        fstream = StringIO.StringIO(infile.read())
        zf = zipfile.ZipFile(fstream)
        data = zf.read('top-1m.csv')
        fstream.close()
        zf.close()
        return data
        
    def read_top_list(self, data):
        data_stream = StringIO.StringIO(data)
        reader = csv.reader(data_stream, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        count = 0
        
        for row in reader:
            try:
                if count < self._max_list: 
                    self._top_sites.append(row[1])
                    count +=1
            except:
                continue
        data_stream.close()
