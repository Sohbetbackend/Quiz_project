from flask import Flask, render_template, request, redirect, url_for, current_app
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Banner, News, Services, Projects, Videos
from app.forms import LoginForm, RegistrationForm, AddbannerForm, AddnewsForm, AddservicesForm, AddprojectsForm, AddvideosForm
from app import app, db, photos
import os 

@app.route('/')
@app.route('/admin/')
@login_required
def admin():
    return render_template('index.html', title='Admin')


@app.route('/admin/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
        if user is None:
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('admin'))
    return render_template('login.html', title='Login Page', form=form)


@app.route('/admin/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/admin/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title='Admin Register', form=form)


@app.route('/admin/banners', methods=['GET'])
def get_banners():
    banners = Banner.query.all()
    return render_template('banners.html', banners=banners)


@app.route('/admin/news', methods=['GET'])
def get_news():
    news = News.query.all()
    return render_template('news.html', news=news)


@app.route('/admin/services', methods=['GET'])
def get_services():
    services = Services.query.all()
    return render_template('services.html', services=services)


@app.route('/admin/recentprojects', methods=['GET'])
def get_projects():
    projects = Projects.query.all()
    return render_template('projects.html', projects=projects)


@app.route('/admin/videos', methods=['GET'])
def get_videos():
    videos = Videos.query.all()
    return render_template('videos.html', videos=videos)

# ADD BANNER
@app.route('/admin/addbanner', methods=['GET', 'POST'])
def addbanner():
    form = AddbannerForm()
    if request.method =='POST':
        name = form.name.data
        img = photos.save(request.files.get('img'))
        addbanner = Banner(name=name, img=img)
        db.session.add(addbanner)
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('postpart/addbanner.html', form=form, title='Add Banner')


@app.route('/admin/updatebanner/<int:id>', methods=['GET','POST'])
@login_required
def updatebanner(id):
    form = AddbannerForm()
    banner = Banner.query.get_or_404(id)
    if request.method =="POST":
        banner.name = form.name.data
        if request.files.get('img'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + banner.img))
                banner.img = photos.save(request.files.get('img'))
            except:
                banner.img = photos.save(request.files.get('img'))
        db.session.commit()
        return redirect(url_for('admin'))
    form.name.data = banner.name
    return render_template('postpart/addbanner.html', form=form, title='Update Banner')


@app.route('/deletebanner/<int:id>', methods=['POST'])
@login_required
def deletebanner(id):
    banner = Banner.query.get_or_404(id)
    if request.method =="POST":
        try:
            os.unlink(os.path.join(current_app.root_path, "static/images/" + banner.img))
        except Exception as e:
            print(e)
        db.session.delete(banner)
        db.session.commit()
        return redirect(url_for('admin'))
    return redirect(url_for('admin'))


# NEWS PART
@app.route('/admin/addnews', methods=['GET', 'POST'])
def addnews():
    form = AddnewsForm()
    if request.method =='POST':
        name = form.name.data
        img = photos.save(request.files.get('img'))
        addnews = News(name=name, img=img)
        db.session.add(addnews)
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('postpart/addnews.html', form=form, title='Add News')


@app.route('/admin/updatenews/<int:id>', methods=['GET','POST'])
@login_required
def updatenews(id):
    form = AddnewsForm()
    news = News.query.get_or_404(id)
    if request.method =="POST":
        news.name = form.name.data
        if request.files.get('img'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + news.img))
                news.img = photos.save(request.files.get('img'))
            except:
                news.img = photos.save(request.files.get('img'))
        db.session.commit()
        return redirect(url_for('admin'))
    form.name.data = news.name
    return render_template('postpart/addnews.html', form=form, title='Update News')


@app.route('/deletenews/<int:id>', methods=['POST'])
@login_required
def deletenews(id):
    news = News.query.get_or_404(id)
    if request.method =="POST":
        try:
            os.unlink(os.path.join(current_app.root_path, "static/images/" + news.img))
        except Exception as e:
            print(e)
        db.session.delete(news)
        db.session.commit()
        return redirect(url_for('admin'))
    return redirect(url_for('admin'))


# SERVICES PART
@app.route('/admin/addservices', methods=['GET', 'POST'])
def addservices():
    form = AddservicesForm()
    if request.method =='POST':
        name = form.name.data
        desc = form.desc.data
        addservices = Services(name=name, desc=desc)
        db.session.add(addservices)
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('postpart/addservices.html', form=form, title='Add Services')


@app.route('/admin/updateservices/<int:id>', methods=['GET','POST'])
@login_required
def updateservices(id):
    form = AddservicesForm()
    services = Services.query.get_or_404(id)
    if request.method =="POST":
        services.name = form.name.data
        services.desc = form.desc.data
        db.session.commit()
        return redirect(url_for('admin'))
    form.name.data = services.name
    form.desc.data = services.desc
    return render_template('postpart/addservices.html', form=form, title='Update Services')


@app.route('/deleteservices/<int:id>', methods=['POST'])
@login_required
def deleteservices(id):
    services = Services.query.get_or_404(id)
    if request.method =="POST":
        try:
            os.unlink(os.path.join(current_app.root_path, "static/images/" + services.img))
        except Exception as e:
            print(e)
        db.session.delete(services)
        db.session.commit()
        return redirect(url_for('admin'))
    return redirect(url_for('admin'))


# PROJECTS PART
@app.route('/admin/addprojects', methods=['GET', 'POST'])
def addprojects():
    form = AddprojectsForm()
    if request.method =='POST':
        name = form.name.data
        desc = form.desc.data
        img = photos.save(request.files.get('img'))
        addprojects = Projects(name=name, desc=desc, img=img)
        db.session.add(addprojects)
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('postpart/addprojects.html', form=form, title='Add Projects')


@app.route('/admin/updateprojects/<int:id>', methods=['GET','POST'])
@login_required
def updateprojects(id):
    form = AddprojectsForm()
    projects = Projects.query.get_or_404(id)
    if request.method =="POST":
        projects.name = form.name.data
        projects.desc = form.desc.data
        if request.files.get('img'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + projects.img))
                projects.img = photos.save(request.files.get('img'))
            except:
                projects.img = photos.save(request.files.get('img'))
        db.session.commit()
        return redirect(url_for('admin'))
    form.name.data = projects.name
    form.desc.data = projects.desc
    return render_template('postpart/addbanner.html', form=form, title='Update Services')


@app.route('/deleteprojects/<int:id>', methods=['POST'])
@login_required
def deleteprojects(id):
    projects = Projects.query.get_or_404(id)
    if request.method =="POST":
        try:
            os.unlink(os.path.join(current_app.root_path, "static/images/" + projects.img))
        except Exception as e:
            print(e)
        db.session.delete(projects)
        db.session.commit()
        return redirect(url_for('admin'))
    return redirect(url_for('admin'))
