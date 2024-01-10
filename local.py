class Middleware():

    def __init__(self, app):
        self.app = app

from src.external import app

if __name__ == "__main__":
    app.run(debug=True)
    