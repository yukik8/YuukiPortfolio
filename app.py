import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from werkzeug.utils import secure_filename

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or "your-secret-key"

# アップロードされた写真の保存先
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 最大16MB
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}

db.init_app(app)

with app.app_context():
    from models import Photo
    db.create_all()

# アップロードされたファイルの拡張子チェック
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    from models import Photo
    photos = Photo.query.order_by(Photo.created_at.desc()).all()
    return render_template('index.html', photos=photos)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'photo' not in request.files:
            flash('写真が選択されていません')
            return redirect(request.url)
        
        file = request.files['photo']
        if file.filename == '':
            flash('ファイルが選択されていません')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            from models import Photo
            
            filename = secure_filename(file.filename)
            # ファイル名が重複しないように、タイムスタンプを追加
            filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{filename}"
            
            # アップロードフォルダが存在しない場合は作成
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            # データベースに保存
            photo = Photo(
                title=request.form.get('title', 'Untitled'),
                description=request.form.get('description', ''),
                filename=filename
            )
            db.session.add(photo)
            db.session.commit()
            
            flash('写真がアップロードされました')
            return redirect(url_for('index'))
            
    return render_template('upload.html')
