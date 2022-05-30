from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.renderers import render_to_response

import mysql.connector as mysql
import os

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

def ui_page(req):

  return render_to_response('templates/ui.html', {}, request=req)

def features_page(req):

  return render_to_response('templates/features.html', {}, request=req)

def interactions_page(req):

  return render_to_response('templates/interactions.html', {}, request=req)

def revenue_page(req):

  return render_to_response('templates/revenue.html', {}, request=req)

def pivots_page(req):

  return render_to_response('templates/pivots.html', {}, request=req)



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

  config.add_route('ui_page', '/ui')
  config.add_view(ui_page, route_name='ui_page')

  config.add_route('features_page', '/features')
  config.add_view(features_page, route_name='features_page')

  config.add_route('interactions_page', '/interactions')
  config.add_view(interactions_page, route_name='interactions_page')

  config.add_route('revenue_page', '/revenue')
  config.add_view(revenue_page, route_name='revenue_page')

  config.add_route('pivots_page', '/pivots')
  config.add_view(pivots_page, route_name='pivots_page')

  config.add_static_view(name='/', path='./public', cache_max_age=3600)

  app = config.make_wsgi_app()
  server = make_server('0.0.0.0', 6000, app)
  server.serve_forever()