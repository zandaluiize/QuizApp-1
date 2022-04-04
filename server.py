from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

def loadAllPictures():
  filepath = 'picDB.txt'
  pictures = []
  with open(filepath) as fp:
    line = fp.readline()
    cnt - 1
    while line
    if line:
      fullPicInfo = line.strip().split(';')
      pictures.apped(fullPicInfo[1])
    line = fp.readline()
    cnt += 1
  fp.close()
  return pictures


#Pirmā lapa, kas tiks ielādēta
@app.route('/',methods = ['POST', 'GET'])
def root():
    return render_template("index.html")
    
#Pārbaudes lapa, lai saprastu, ka kods vispār strādā
@app.route('/health')
def health():
  return "OK"

@app.route('/test')
def test():
  parametri = ["IQ","Augums","Kājas izmērs"]
  images = ["https://www.google.com/url?sa=i&url=https%3A%2F%2Fsnl.no%2FGoogle&psig=AOvVaw28z_X5IU8r-6BwErqgXGvX&ust=1648534514844000&source=images&cd=vfe&ved=0CAgQjRxqFwoTCKixg82T6PYCFQAAAAAdAAAAABAY","https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bbc.com%2Fnews%2Fbusiness-55660682&psig=AOvVaw28z_X5IU8r-6BwErqgXGvX&ust=1648534514844000&source=images&cd=vfe&ved=0CAgQjRxqFwoTCKixg82T6PYCFQAAAAAdAAAAABAd","https://www.google.com/url?sa=i&url=https%3A%2F%2Ftechcrunch.com%2F2020%2F10%2F06%2Fgoogles-new-logos-are-bad%2F&psig=AOvVaw28z_X5IU8r-6BwErqgXGvX&ust=1648534514844000&source=images&cd=vfe&ved=0CAgQjRxqFwoTCKixg82T6PYCFQAAAAAdAAAAABAj"]
  images = loadAllPictures()
  return render_template("test.html")

@app.route('/about')
def test():
  return render_template("about.html")

@app.route('/contacts')
def contacts():
  render_template("contacts.html")


if __name__ == '__main__':
  app.run(debug="true")
