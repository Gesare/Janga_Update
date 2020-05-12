from . import auth

@auth.route("/login")
def login():
    return "<h1>You are now logged in</h1>"