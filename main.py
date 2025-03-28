from flask import Flask, request, redirect

app = Flask(__name__)

@app.before_request
def redirect_to_www():
    """Redirect naked domain traffic to www."""
    if not request.host.startswith("www."):
        www_url = request.url.replace(f"//{request.host}", f"//www.{request.host}", 1)
        return redirect(www_url, code=301)