import random

from gevent import monkey

monkey.patch_all()

from flask import Flask
from flask_beanstalk import Beanstalk

app = Flask(__name__)
app.config['BEANSTALK_HOST'] = '127.0.0.1'
app.config['BEANSTALK_PORT'] = 11300

beanstalk = Beanstalk(app)


@app.route('/')
def index():
    secs = random.randint(0, 10)
    beanstalk.use('twitter')
    beanstalk.put(str(secs))
    return "placed job that sleeps for %d seconds" % secs


if __name__ == '__main__':
    app.run(debug=True)
