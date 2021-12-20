import predictor_local as myapp_loc
import predictor as myapp

# This is just a simple wrapper for gunicorn to find your app.
# If you want to change the algorithm file, simply change "predictor" above to the
# new file.

app_loc = myapp_loc.app
app = myapp.app
