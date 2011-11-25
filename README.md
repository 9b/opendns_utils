Summary
=======
OpenDNS is great, but the lack of an API is frustrating. This CLI tool aims to provide some automation to the web browser through the use of Selenium. 

Modules
=======
* Auto-blocking - block a list of URLs for a given network

Dependencies
============
* X11
* Selenium (python)
* Firefox

Setup
=====
1. Execute java -jar selenium_server/selenium-server-standalone-2.13.0.jar
2. Execute auto_block.py with proper switches

Flow
====
Auto-block
----------
1. Passed in URL list is checked for global blocks and top alexa sites
2. Selenium is opened to opendns.com
3. User is signed in with credentials
4. Navigation is made to the proper networking settings page
5. Each URL in the list to block is added to the list of blocked domains

To Do
=====
* Error handling on Selenium tests
* Provide clean options for URL checking
* Clean up logging
