import re

def app_favicon(request):
    if re.match(r'^/(islamic(|-.*))', request.path):
        return {'favicon_path': 'images/logos/favicon-islamic.ico'}
    elif re.match(r'^/(premier(|-.*))', request.path):
        return {'favicon_path': 'images/logos/premier-favicon.ico'}
    return {'favicon_path': 'images/logos/conventional_favicon.ico'}