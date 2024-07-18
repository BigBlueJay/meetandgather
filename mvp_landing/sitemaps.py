from django.contrib.sitemaps import Sitemap
from django.urls import reverse
#from blog.models import Post

class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return ['home', 'bookings', 'bookform','openhouse','events',
                'gallery','contact','about'] #returning static pages; home and contact us
 
    def location(self, item):
        return reverse(item) #returning the static pages URL; home and contact us