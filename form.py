# -*- coding: utf-8 -*-  
import os
from google.appengine.api import mail
from google.appengine.api import users
from google.appengine.ext import ndb
from datetime import datetime, timedelta
import jinja2
import webapp2
import uuid
import urllib
import urllib2



JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class buy(ndb.Model):
    """Models an individual Guestbook entry with author, content, and date."""

    product = ndb.StringProperty()
    cosumer = ndb.StringProperty()
    sex = ndb.StringProperty()
    email = ndb.StringProperty()
    address = ndb.StringProperty()
    total = ndb.StringProperty()
    other = ndb.StringProperty()
    date = ndb.DateTimeProperty()

class product(ndb.Model):
    """Models an individual Guestbook entry with author, content, and date."""

    product_name = ndb.StringProperty()
    porduct_price = ndb.StringProperty()
    product_scribe = ndb.StringProperty()
    product_pic = ndb.StringProperty()
    product_type = ndb.StringProperty()
    product_uuid = ndb.StringProperty()
    product_intro = ndb.StringProperty()
    product_bake = ndb.StringProperty()
    date = ndb.DateTimeProperty()

class vertify(webapp2.RequestHandler):
    
    def get(self):
  
    

        template_values = {
           
           
           
        }

        template = JINJA_ENVIRONMENT.get_template('vertify.html')
        self.response.write(template.render(template_values)) 
    



class MainPage(webapp2.RequestHandler):
    
    def get(self):
    
        greeting = product()

         
        #greeting.product_name = '瓜地馬拉安提瓜'
        #greeting.porduct_price = '500'
        #greeting.product_scribe = '00000000000000000000000000000000'
        #greeting.product_pic = 'http://3.bp.blogspot.com/-lyF61Bj3bro/Ulo_J5uvysI/AAAAAAAACvY/ulw2phc2_JQ/s640/%E7%93%9C%E5%9C%B0%E9%A6%AC%E6%8B%89%E5%AE%89%E6%8F%90%E7%93%9C.jpg'
        #greeting.product_type = '百分百品賞包'
        #greeting.product_uuid = ''
        #greeting.product_intro = ''
        #greeting.put()
        #self.response.headers.add_header("Set-Cookie", "name=0")
   

     
        greetings_query = product.query()
        #greetings_query = greetings_query.order(-product.date)
        #greetings = greetings_query.fetch(20)
        greetings = greetings_query
    

        template_values = {
            'greetings': greetings,
           
           
           
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values)) 
        
           

class coffee_list(webapp2.RequestHandler):
    
    def get(self):
        
        product_type = self.request.get('type')
        
        if self.request.cookies.get('name'):
            name = self.request.cookies.get('name')
            #output = str(name+10)
            ttt = name.split('$')
        else:
            ttt = '0'
        
        greetings_query = product.query()
        #greetings_query = greetings_query.order(-product.date)
        #greetings = greetings_query.fetch(20)
        greetings = greetings_query
        
        #self.response.write('</a>'+str(uuid.uuid1())+'</a>')

        template_values = {
            'greetings': greetings,
            'product_type': product_type,
            'ttt': ttt,
            
            
           
           
        }

        template = JINJA_ENVIRONMENT.get_template('coffee_list.html')
        self.response.write(template.render(template_values)) 


class mycart(webapp2.RequestHandler):
    


    def post(self):

        challenge=self.request.get('recaptcha_challenge_field')
        response=self.request.get('recaptcha_response_field')
        remoteip=self.request.remote_addr #取得使用者ip
        privatekey='6LcqLewSAAAAAJfkCZaUv34cGPybhmgt4R3j3D2i'
          #以上為所要用到的四個參數
        url='http://www.google.com/recaptcha/api/verify'
           
           
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; <span class="e5zs656f8" id="e5zs656f8_4">Windows</span> NT)'
        headers = { 'User-Agent' : user_agent } #製作header
        value={'challenge':challenge,'response':response,'remoteip':remoteip,'privatekey':privatekey}
        data = urllib.urlencode(value)
        req = urllib2.Request(url, data, headers)
          #建立post
        response = urllib2.urlopen(req)
          #發送post
        response_list = response.read().split('\n')
        
      
    
    
        

        #000000000000000000000000000000000000000000000000000000
        if self.request.cookies.get('name'):
            name = self.request.cookies.get('name')
            #output = str(name+10)
            ttt = name.split('$')
        else:
            ttt = '0'
        
        greetings_query = product.query()
        #greetings_query = greetings_query.order(-product.date)
        #greetings = greetings_query.fetch(20)
        greetings = greetings_query
        
        #self.response.write('</a>'+str(uuid.uuid1())+'</a>')

        template_values = {
            'greetings': greetings,
            'ttt': ttt,
            'captcha': response_list[0],

           
           
        }

        template = JINJA_ENVIRONMENT.get_template('mycart.html')
        self.response.write(template.render(template_values)) 


class mycart1(webapp2.RequestHandler):
    
    def get(self):
        
        
        if self.request.cookies.get('name'):

            self.request.cookies.get('name')
            name = self.request.cookies.get('name')
            ttt = name.split('$')

            check_cart = 'True'
            for i in ttt:
                if i != "None" and i !="":
                    check_cart = 'False'

        else:
            check_cart = 'True'
            ttt="0"
        
        greetings_query = product.query()
        #greetings_query = greetings_query.order(-product.date)
        #greetings = greetings_query.fetch(20)
        greetings = greetings_query
        
        #self.response.write('</a>'+str(uuid.uuid1())+'</a>')

        template_values = {
            'greetings': greetings,
            'ttt': ttt,
            'check_cart':check_cart,
            
            
           
           
        }

        template = JINJA_ENVIRONMENT.get_template('mycart1.html')
        self.response.write(template.render(template_values))       

class cancel_list(webapp2.RequestHandler):
    
    def get(self):
        self.response.headers.add_header("Set-Cookie", "name=$")
        self.redirect('/mycart1')


class confirm(webapp2.RequestHandler):
    

    def post(self):
        if self.request.cookies.get('name'):

            self.request.cookies.get('name')
            name = self.request.cookies.get('name')
            ttt = name.split('$')
           
            product_list=[]
            user_information_list=[]
            user_information_list.insert(0,[self.request.get('cosumer'),self.request.get('email'),self.request.get('sex'),self.request.get('addr_zip'),self.request.get('addr_county'),self.request.get('addr_area'),self.request.get('address')])
            a = 0


            for i in ttt:
               
               if i != " " and i != "None" and i != "":
                   product_list.insert(a,[self.request.get(i+'_name'),self.request.get(i),self.request.get(i+'_type'),i,self.request.get(i+'_price')])
                  
                   a=a+1
            
                 
            
        template_values = {
            'user_information_list':user_information_list,
            'product_list':product_list,
           
            }

        template = JINJA_ENVIRONMENT.get_template('2.html')
        self.response.write(template.render(template_values))      
           


class Guestbook(webapp2.RequestHandler):

    def post(self):
        self.request.cookies.get('name')
        name = self.request.cookies.get('name')
        ttt = name.split('$')
        # We set the same parent key on the 'Greeting' to ensure each Greeting
        # is in the same entity group. Queries across the single entity group
        # will be consistent. However, the write rate to a single entity group
        # should be limited to ~1/second.
        def send_mail(address,content,sex):
            message = mail.EmailMessage(sender="york11122@gmail.com",
                            subject="Your account has been approved")

            message.to = address
            message.body = """
Dear %s%s

您所選購商品
%s

運費%s 總價%s
=======================================================
匯款後續相關內容...................
匯款後續相關內容...................
匯款後續相關內容...................
匯款後續相關內容...................
            """ % (self.request.get('cosumer').encode('utf-8'),sex,content,self.request.get('other_price2').encode('utf-8'),self.request.get('total_price2').encode('utf-8'))

            message.send() 

        greeting = buy()
        productstring=''
        sex='先生'
        greeting.cosumer = self.request.get('cosumer')
        greeting.sex = self.request.get('sex')
        greeting.email = self.request.get('email')
        greeting.address = self.request.get('address')
       
        for i in ttt:
               
               if i != " " and i != "None" and i != "": 
                    productstring = productstring+'['+'商品:'+self.request.get(i+'_name').encode('utf-8')+' 類型:'+self.request.get(i+'_type').encode('utf-8')+' 數量:'+self.request.get(i+'_number').encode('utf-8')+' 價格:$'+self.request.get(i+'_price').encode('utf-8')+' 小計:$'+self.request.get(i+'_count2').encode('utf-8')+']\n\r'
                   

        greeting.product = productstring
        greeting.other = self.request.get('other_price2')
        greeting.total = self.request.get('total_price2')
        greeting.date = datetime.now()+timedelta(hours=8) 
        greeting.put()
        if self.request.get('sex').encode('utf-8')=='女':
            sex='小姐'
        send_mail(self.request.get('email'),productstring,sex)
        self.redirect('/thanks')

class cart(webapp2.RequestHandler):
    
    def post(self):

        if not self.request.cookies.get('name') :   
       
            self.response.headers.add_header("Set-Cookie", "name=$")
            name = str(self.request.cookies.get('name'))+"$"+str(self.request.get('cart'))
            self.response.headers.add_header("Set-Cookie", "name=%s;"%name)
            self.redirect('/coffee_list?type=all')
           
        else:    
            name = str(self.request.cookies.get('name'))+"$"+str(self.request.get('cart'))
            self.response.headers.add_header("Set-Cookie", "name=%s;"%name)
            self.redirect('/coffee_list?type=all')


class page2(webapp2.RequestHandler):
    
    def get(self):
        
        
        

        template_values = {
         
            
            
           
           
        }

        template = JINJA_ENVIRONMENT.get_template('2.html')
        self.response.write(template.render(template_values))   
    
class thanks(webapp2.RequestHandler):
    
    def get(self):
        
        
        

        template_values = {
         
            
            
           
           
        }

        template = JINJA_ENVIRONMENT.get_template('thanks.html')
        self.response.write(template.render(template_values))   
    


       
     
application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook),
    ('/cart', cart),
    ('/coffee_list', coffee_list),
    ('/mycart', mycart),
    ('/mycart1', mycart1),
    ('/confirm', confirm),
    ('/cancel_list', cancel_list),
    ('/vertify', vertify),
    ('/page2', page2),
    ('/thanks', thanks),


    
], debug=True)