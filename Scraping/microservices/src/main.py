import os
from endpoints.app import crear_app
import time
app = crear_app()

@app.errorhandler(500)
def server_error(e):
    return {
        "Status": "The service has failed"
    }

if __name__ == '__main__':
    app.debug = True
    app.run(
        debug = True,
        # host='127.0.0.1',
        host='0.0.0.0',
        port=int(os.environ.get("PORT", 8081))
    )