from selenium import selenium
import unittest

class auto_block():
    def __init__(self,username,password,network,urls,verbose,add_all):
        self._url = "https://opendns.com"
        self._username = username
        self._password = password
        self._network = str(network)
        self._urls = None
        self.url_file = urls
        self.verbose = verbose
        self._add_all = add_all

        self.verificationErrors = []
        if self.verbose:
            print "[+] Setting up Selenium"        
        self.selenium = selenium("127.0.0.1", 4444, "*chrome", self._url)
        self.selenium.start()
        
        self.process_urls()
        self.login_test()
        self.check_login()
        self.core_test()
        self.clean_up()
        
    def process_urls(self):
        f = open(self.url_file,"r")
        lines = f.readlines()
        self._urls = lines

    def login_test(self):
        if self.verbose:
            print "[*] Opening browser to https://opendns.com"   
        sel = self.selenium
        sel.open(self._url)    
        sel.click("link=Sign In")
        sel.wait_for_page_to_load("50000")
        if self.verbose:
            print "[*] Attempting to sign-in with provided credentials"
        sel.type("id=username",self._username)
        sel.type("id=password",self._password)
        sel.click("id=dont_expire")
        sel.click("id=sign-in")
        sel.wait_for_page_to_load("50000")
            
    def check_login(self):
        sel = self.selenium 
        if not sel.is_element_present("link=Settings"):
            print "[!] Login Failed"
            raise Exception("FAILED_LOGIN")
        else:
            if self.verbose:
                print "[*] Signed in as " + self._username            

    def core_test(self):
        sel = self.selenium
        if self.verbose:
            print "[*] Accessing setttings"
        sel.click("link=Settings")
        sel.wait_for_page_to_load("50000")
        if self.verbose:
            print "[*] Selecting network " + self._network
        sel.select("id=navigation-select","id=nav-network-" + self._network)
        sel.wait_for_page_to_load("50000")
        if sel.is_element_present("id=add-domain-applytoall") and self._add_all:
            sel.click("add-domain-applytoall")
        for url in self._urls:
            sel.type("id=block-domain", url.strip())
            sel.click("id=add-domain")
            if self.verbose:
                print "[*] Blocking URL " + url.strip()
                print "[*] Waiting for success"
            sel.wait_for_condition("var value = selenium.browserbot.findElementOrNull('add-domain-busy'); value.style.display == 'none'","20000")

    def clean_up(self):
        if self.verbose:
            print "[+] Cleaning up"
        self.selenium.stop()
        #self.assertEqual([], self.verificationErrors)
