from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define the first function for the route '/'
@app.route('/')
def hello():
    return 'Hello, World!'
def goodbye():
    return 'Goodbye, World!'

# Define the second function for the route '/'
# @app.route('/')
# def goodbye():
#     return 'Goodbye, World!'

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
