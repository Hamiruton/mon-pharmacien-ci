from src import create_app
from waitress import serve

mode = 'prod'

if __name__ == "__main__":
    app = create_app()

    if mode == 'prod':
        serve(app, threads=1, port=50100, host='0.0.0.0')
    else:
        app.run()