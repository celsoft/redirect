#!/usr/bin/env python

import logging

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

DOMAIN = "https://igrovii-automati-besplatno.appspot.com"

class AllHandler(webapp.RequestHandler):
    def get(self):
        #logging.info("INFO --- %s", self.request.path)
        self.redirect(DOMAIN + self.request.path, True)

application = webapp.WSGIApplication([('/.*', AllHandler)])

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()