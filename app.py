from flask import Flask, redirect
import random
import os

app = Flask(__name__)

# Yönlendirilecek siteler listesi
random_sites = [
    "https://www.google.com",
    "https://www.bizdeoyunlarbedava.tr.gg"
]

# Dinamik title/description/keywords için kelime havuzu
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
    # Ana sayfaya geleni anında rastgele bir siteye gönder
    random_url = random.choice(random_sites)
    return redirect(random_url)

@app.route('/redirect_sequence')
def redirect_sequence():
    # 2 saniye sonra tek bir rastgele siteye yönlendirecek
    random_url = random.choice(random_sites)
    title       = get_random_words(3).title()
    description = get_random_words(8)
    keywords    = ', '.join(random.sample(word_pool, 5))

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
          // 2 saniye sonra rastgele seçilen URL'e yönlendir
          setTimeout(function() {{
            window.location.href = '{random_url}';
          }}, 2000);
        </script>
      </body>
    </html>
    """

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
