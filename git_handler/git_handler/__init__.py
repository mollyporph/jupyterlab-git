from git_handler.handlers import setup_handlers
# Jupyter Extension points
def _jupyter_server_extension_paths():
    return [{
        'module': 'git_handler',
    }]

def _jupyter_nbextension_paths():
    return [{
        "section": "notebook",
        "dest": "git_handler",
        "src": "static",
        "require": "git_handler/one"
    }]

def load_jupyter_server_extension(nbapp):
    setup_handlers(nbapp.web_app)