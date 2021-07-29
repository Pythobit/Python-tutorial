from flask import Flask

app = Flask(__name__)
posts = {
    0: {
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
    return f'Post {post["title"]}, Content: \n{post["content"]}'


if __name__ == '__main__':
    app.run(debug=True)
