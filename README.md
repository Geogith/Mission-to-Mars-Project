# Mission to Mars Project

This was the most difficult assignment to date. It required web scraping several sites:
https://mars.nasa.gov/news
https://www.jpl.nasa.gov/spaceimages/?search=&catergory=Mars)
https://space-facts.com/mars/
https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)
The following steps were taken to complete this homework:
Step 1: A repository was created on GitHub.
Step2: Several applications were used to web scrape, such as Jupyter Notebook, BeautifulSoup, Pandas, Request/Splinter, MongoDB and a Flask application.
Step 3: Web scraping was done by creating a Jupyter notebook (mission_to_mars.ipynb) to extract the news title and paragraph text for approximately 10 articles from the nasa news site shown above.
Step 4: Four mars images (featured_image_url) were scraped from the jpl.nasa. gov website using splinter to navigate the site and to find the images. The url images were assigned a variable named featured_image_url.
Step 5: Pandas was used to convert the data to a HTML table string.
Step 6: High resolution images were scraped from the astrogeology website. These images were stored in a Python dictionary.
Step 7: VS Code was used to create the Flask Application and MongoDB. The Jupyter notebook script was converted to a Python script called scrape_mars.py in VS Code. Next a route call ‘/scrape’ was created to import my scrape_mars.py script. The ‘/scrape’ function was called and the returned values were stored in Mongo as a Python dictionary.
Step 8: Another root ‘/’ was created to query the Mongo database. This was used to pass the mars data into a HTML template for display.
Step 9: Finally, an index.html file was created to take the mars data dictionary and display all the data and images on a HTML webpage.
After completing all steps, the web scraped data and files were upload to GitHub for transfer to bootcampspot.  A screenshot of featured images was also uploaded to show that the code ran successfully.

