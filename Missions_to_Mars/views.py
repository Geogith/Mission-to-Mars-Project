from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pymongo

import scrape_mars

app = Flask(__name__)

# create default route
@app.route('/')
def index():
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    db = client.missionDB
    try:
        
        db.create_collection("destinations")

    except(pymongo.errors.CollectionInvalid): 
        print(True)
    
    collection = db.destinations
    inventory = list(collection.find())
  
    
    for item in inventory:
        
        news = item['news']['title']
        paragraph = item['news']['paragraph']
        img_url = item['featured_image_url']
        hem = item['hemisphere_image_urls']
        facts_table = item['facts_table']



    return render_template('index.html', data1=news, data2=paragraph, data3=img_url, data4=hem, data5=facts_table)

# create scrape route
@app.route('/scrape')
def scrape():

    # call scrape function and assign to planet dictionary variable
    planet = scrape_mars.scrape()

    # store planet variable into Mongo
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    db = client.missionDB

    # Declare the collection
    collection = db.destinations

    # Insert document into collection
    collection.insert_one(planet)

    return render_template('index.html', data=planet)

# run app
if __name__ == "__main__":
    app.run(debug=True)


