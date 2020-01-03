"""
IMHO Python Flask boilerplate

Update `nameyourapp` according to your own.
"""
from nameyourapp import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
