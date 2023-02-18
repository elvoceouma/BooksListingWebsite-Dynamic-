from flask import Flask, render_template


app = Flask(__name__)

CARS = [  
  {    
    "id": 1,    
    "make": "Ford",    
    "model": "Mustang",    
    "year": 2022,    
    "price": 35000  
  },  
  {
    "id": 2,    
    "make": "Chevrolet",    
    "model": "Corvette",    
    "year": 2021,    
    "price": 65000  
  },  
  {    
    "id": 3,    
    "make": "BMW",    
    "model": "M3",    
    "year": 2020,    
    "price": 55000  
  },  
  {    
    "id": 4,    
    "make": "Porsche",    
    "model": "911",    
    "year": 2022,    
    "price": 90000  
  },  
  {    
    "id": 5,    
    "make": "Tesla",    
    "model": "Model S",    
    "year": 2021,    
    "price": 80000  
  }
]


@app.route("/")
def hello_world():
  return render_template('home.html', cars=CARS)

if __name__ =="__main__":  
  app.run(host="0.0.0.0", debug=True)
