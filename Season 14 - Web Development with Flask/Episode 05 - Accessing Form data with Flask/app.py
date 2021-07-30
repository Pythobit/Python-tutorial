from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
posts = {
    0: {
        'post_id': 0,
        'title': 'Hello World..!!',
        'content': 'This is my first post on this site.'
    }
}


@app.route('/')
def home():
    return 'Hello world.!'


@app.route('/posts/<int:post_id>')
def post(post_id):
    post = posts.get(post_id)
    if not post:
        return render_template('404.html', message=f'A post with post-id:{post_id}, is not found.!')
    return render_template('post.html', post=post)


@app.route('/posts/form')
def form():
    return render_template('create.html')


# 127.0.0.1:5000/posts/create?title=title-here&content=content-here
@app.route('/posts/create', methods=['POST'])   # added methods=['POST']
def create():
    title = request.form.get('title')       # updated args -> form
    content = request.form.get('content')   # updated args -> form
    post_id = len(posts)
    posts[post_id] = {'id': post_id, 'title': title, 'content': content}
    return redirect(url_for('post', post_id=post_id))


if __name__ == '__main__':
    app.run(debug=True)
