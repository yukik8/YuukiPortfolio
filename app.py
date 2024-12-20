import os
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or "your-secret-key"

@app.route('/')
def index():
    # Sample photo data - in a real app, this would come from a database
    photos = [
        {
            'id': 1,
            'title': 'Mountain Landscape',
            'description': 'Beautiful mountain vista at sunset',
            'url': 'https://source.unsplash.com/800x600/?mountain'
        },
        {
            'id': 2,
            'title': 'Ocean Waves',
            'description': 'Peaceful ocean waves at dawn',
            'url': 'https://source.unsplash.com/800x600/?ocean'
        },
        {
            'id': 3,
            'title': 'Urban Architecture',
            'description': 'Modern city architecture',
            'url': 'https://source.unsplash.com/800x600/?architecture'
        },
        {
            'id': 4,
            'title': 'Nature Close-up',
            'description': 'Macro photography of nature',
            'url': 'https://source.unsplash.com/800x600/?nature'
        },
        {
            'id': 5,
            'title': 'Street Photography',
            'description': 'Urban life captured in moment',
            'url': 'https://source.unsplash.com/800x600/?street'
        },
        {
            'id': 6,
            'title': 'Portrait',
            'description': 'Artistic portrait photography',
            'url': 'https://source.unsplash.com/800x600/?portrait'
        }
    ]
    return render_template('index.html', photos=photos)
