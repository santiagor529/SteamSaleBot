from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')

def check():
  return "Up and running!"

def run():
  app.run(host='0.0.0.0',port=8080)

def Web_Server():
  t = Thread(target=run)
  t.start()