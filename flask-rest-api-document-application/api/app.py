from flask import render_template
import connexion


""""
Create the application instance using Connexion rather than Flask. 
Internally, the Flask app is still created, but it now has additional functionality added to it.
"""
app = connexion.App(__name__, specification_dir="./")


""""
This tells the app instance to read the file swagger.yml from the specification directory 
and configure the system to provide the Connexion functionality.
The parameter specification_dir: This informs Connexion what directory to look in for its configuration file, 
in this case our current directory. 
"""
app.add_api("swagger.yml")


# Create a URL route in our application for "/"
@app.route("/")
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template("home.html")


# If we're running in stand alone mode, run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

