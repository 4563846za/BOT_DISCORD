from fask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return 'เซิฟเวอร์กำลังทำงาน'

def server_on():
    t = Thread(target=run)
    t.start()