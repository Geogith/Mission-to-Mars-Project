from Missions_to_Mars import app 


@app.route('/')
def index():
    return 'Hello World'