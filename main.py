from flask import Flask, render_template
# Instaniate the Flask application object
app = Flask(__name__) # __name__ is a special variable in Python that holds the name of the current module. When you run a script directly, __name__ is set to "__main__". When you import a module, __name__ is set to the module's name. By passing __name__ to Flask, it helps Flask determine the root path of the application, which is important for locating resources and templates.
app.debug = True # Enable debug mode for the Flask application. This allows for automatic reloading of the server when code changes are detected and provides detailed error messages in the browser if an error occurs.
# Add Dummpy data (posts)
posts = [
    {
        'author': 'John Doe',
        'title': 'First Post',
        'content': 'This is the content of the first post.',
        'date_posted': 'April 20, 2024'
    },
    {
        'author': 'Jane Smith',
        'title': 'Second Post',
        'content': 'This is the content of the second post.',
        'date_posted': 'April 21, 2024'
    }
]
# Define route decorator to specify the URL endpoint and the function that should be called when that endpoint is accessed. In this case, the root URL ("/") is associated with the home function.
@app.route('/')
@app.route('/home') # This allows both the root URL ("/") and "/home" to point to the same function, providing flexibility in how users can access the home page.
def home():
    # posts is a list of dictionaries, where each dictionary represents a blog post with attributes like 'author', 'title', 'content', and 'date_posted'. This data is passed to the template to be rendered dynamically.
    return render_template('home.html', posts=posts) # The render_template function is used to render an HTML template. It looks for the specified template (in this case, 'home.html') in the "templates" directory of the Flask application. When a user accesses the root URL or "/home", the home function is called, and it returns the rendered HTML content of 'home.html' to be displayed in the user's browser.

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

