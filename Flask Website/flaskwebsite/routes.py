from flask import render_template, url_for, flash, redirect, request, abort
from flaskwebsite import app, db
from flaskwebsite.forms import ReviewForm
from flaskwebsite.models import Post
@app.route('/')
def homepage():
    return render_template("index.html")
@app.route('/books')
def bookpage():
    return render_template("books.html")
@app.route('/movie1')
def moviepage1():
    return render_template("movie1.html")
@app.route('/movie2')
def moviepage2():
    return render_template("movie2.html")
@app.route('/faq')
def faqpage():
    return render_template("faq.html")
@app.route('/reviews', methods=['GET', 'POST'])
def reviewpage():
    form=ReviewForm()
    if form.validate_on_submit():
        post = Post(name=form.name.data, email=form.email.data, your_idea=form.your_idea.data)
        db.session.add(post)
        db.session.commit()
        flash('Thank you for sharing your reviews', 'success')
        return redirect(url_for('reviewpage'))
    return render_template("reviews.html",form=form)
@app.route('/posts')
def posts():
    posts=Post.query.all()
    return render_template("post.html",posts=posts)
