from flask import Flask, render_template, url_for, redirect, request, session, flash
import datetime
from flask_compress import Compress
from flask_sslify import SSLify


#flask config
app = Flask(__name__)


app.secret_key = 'SECRET_KEY'
sslify = SSLify(app)
Compress(app)







@app.route("/home", methods=["GET", "POST"])
def date():
    currentDT = datetime.datetime.now()
    dateTime =currentDT.strftime("%Y-%m-%d %H:%M:%S")
    return render_template('/date.html',date=dateTime)

if __name__ == "__main__":
    # Development
    app.run( debug=True)

    #Production
    # http_server = WSGIServer(('', 8080), app)
    # http_server.serve_forever()


    
            
        
        
        
        
        
        
       