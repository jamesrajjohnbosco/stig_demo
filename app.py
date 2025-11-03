from flask import Flask
import os

app = Flask(__name__)

# Basic endpoint that returns a simple message
@app.route('/')
def hello():
    # Retrieve the version from an environment variable set in the k8s deployment
    version = os.environ.get('APP_VERSION', '1.0')
    return f"Hello from the GKE CI/CD Pipeline! (Version: {version})\n"

if __name__ == '__main__':
    # Flask application runs on port 8080 by default in this configuration
    # This port must match the 'targetPort' in the Kubernetes Service/Deployment
    app.run(debug=True, host='0.0.0.0', port=8080)
