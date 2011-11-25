#!/usr/bin/python

__description__ = 'Automate certain tasks within OpenDNS using Selenium'
__author__ = 'Brandon Dixon'
__version__ = '1.0'
__date__ = '2011/11/24'

from libs.urlsanity import *
from libs.odautoblock import *
import time, re, optparse, getpass, time

def main():
    oParser = optparse.OptionParser(usage='usage: %prog [options]\n' + __description__, version='%prog ' + __version__)
    oParser.add_option('-u', '--username', type='string', help='username for openDNS')
    oParser.add_option('-p', '--password', default='', type='string', help='password for openDNS')
    oParser.add_option('-n', '--network', type='int', help='network identifier used as the primary interface for blockings')
    oParser.add_option('-l', '--urls', type='string', help='listing of URLs to block')
    oParser.add_option('-v', '--verbose', action="store_true", default=True, help='verbose logging on performed actions')
    oParser.add_option('-a', '--all', action="store_true", default=False, help='set true to block on all networks')
    (options, args) = oParser.parse_args()

    if options.username and options.network and options.urls:
        check = url_sanity(options.urls,options.verbose)
        critical = check.check_critical()
        top10k = check.check_top10K()
        
        if critical:
            print "[!] URL list included a global block"
            return
        if top10k:
            print "[!] URL list included URLs from the Alexa 10,000"
            return
        
        options.password = getpass.getpass("[=] OpenDNS Password: ")
        auto_block(options.username,options.password,options.network,options.urls,options.verbose,options.all)
    else:
        oParser.print_help()
        return

if __name__ == '__main__':
    main()
