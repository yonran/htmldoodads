from google.appengine.ext import webapp
import wsgiref.handlers
class RedirectHandler(webapp.RequestHandler):
  def get(self):
    self.redirect("/ruler.html")
def main():
  application = webapp.WSGIApplication([(r'/', RedirectHandler)], debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()
