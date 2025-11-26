from app import app

@app.route('/healthcheck')
def healthcheck():
    return "Success", 200