from flask import Flask, redirect
import random
import os

app = Flask(__name__)

random_sites = [
    "https://www.google.com",
    "https://www.bizdeoyunlarbedava.tr.gg"
]

word_pool = [
    "sunshine", "freedom", "adventure", "mystery", "turkey", "istanbul",
    "beauty", "night", "dream", "sugar", "online", "future", "random",
    "power", "girl", "fun", "secret", "code", "page", "story", "click",
    "explore", "now", "hidden", "world", "instant", "love", "deep", "link"
]

def get_random_words(count):
    return ' '.join(random.sample(word_pool, count))

@app.route('/')
def first_redirect():
    random_url = random.choice(random_sites)
    return redirect(random_url)

@app.route('/redirect_sequence')
def redirect_sequence():
    random_url = random.choice(random_sites)
    title = get_random_words(3).title()
    description = get_random_words(8)
    keywords = ', '.join(random.sample(word_pool, 5))

    return f"""
    <html>
        <head>
            <title>{title}</title>
            <meta name="description" content="{description}">
            <meta name="keywords" content="{keywords}">
        </head>
        <body>
            <p>Yönlendiriliyorsunuz...</p>
            <script>
                setTimeout(function() {{
                    window.location.href = '{random_url}';
                }}, 1000);
                setTimeout(function() {{
                    window.location.href = 'https://istanbul.sugarturkey.online/';
                }}, 4000);
            </script>
        </body>
    </html>
    """

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
