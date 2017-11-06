from views import *


@app.route('/query')
def index():
    return render_template('query.html')