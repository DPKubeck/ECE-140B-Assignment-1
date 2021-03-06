from pyramid.config import Configurator
from pyramid.renderers import render_to_response

import mysql.connector as mysql
import os
import bjoern

db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST']

def get_home(req):
  # Connect to the database and retrieve the users
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select first_name, last_name, email from Users;")
  records = cursor.fetchall()
  db.close()

  return render_to_response('templates/home.html', {'users': records}, request=req)

def product_page(req):

  return render_to_response('templates/product.html', {}, request=req)

def kvp_page(req):

  return render_to_response('templates/kvp.html', {}, request=req)


''' Route Configurations '''
if __name__ == '__main__':
  config = Configurator()

  config.include('pyramid_jinja2')
  config.add_jinja2_renderer('.html')

  config.add_route('get_home', '/')
  config.add_view(get_home, route_name='get_home')

  config.add_route('product_page', '/product')
  config.add_view(product_page, route_name='product_page')

  config.add_route('kvp_page', '/kvp')
  config.add_view(kvp_page, route_name='kvp_page')

  config.add_static_view(name='/', path='./public', cache_max_age=3600)
  config.add_static_view(name='/product', path='./public', cache_max_age=3600)
  config.add_static_view(name='/kvp', path='./public', cache_max_age=3600)

  app = config.make_wsgi_app()
  bjoern.run(app, "0.0.0.0", 6000)