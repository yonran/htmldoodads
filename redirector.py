from google.appengine.ext import webapp
import wsgiref.handlers
import datetime, time
import logging, os
class RedirectHandler(webapp.RequestHandler):
  ruler_data = open(os.path.join(os.path.dirname(__file__), 'ruler.html')).read()
  def get(self):
    logging.info(self.request.path)
    if '/ruler.html' != self.request.path:
      self.redirect("http://www.rulernow.com/ruler.html")
    else:
      self.response.headers['Content-type'] = 'text/html'
      self.response.headers['Expires'] = wsgiref.handlers.format_date_time(
          time.mktime((datetime.datetime.now() + datetime.timedelta(days=7)).
          timetuple()))
      self.response.headers['Cache-Control'] = 'public, max-age=%d'%(60*60*24*7)
      self.response.out.write(self.ruler_data)

def main():
  application = webapp.WSGIApplication(
    [
      (r'/', RedirectHandler),
      (r'/ruler.html', RedirectHandler),
    ],
    debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()
