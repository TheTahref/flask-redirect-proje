from flask import Flask, redirect, url_for
import random
import os

app = Flask(__name__)

random_sites = [
    "https://www.google.com",
    "https://www.bizdeoyunlarbedava.tr.gg"
]

def get_random_words(count):
    word_pool = [
        "sunshine", "freedom", "adventure", "mystery", "turkey", "istanbul",
        "beauty", "night", "dream", "sugar", "online", "future", "random",
        "power", "girl", "fun", "secret", "code", "page", "story", "click",
        "explore", "now", "hidden", "world", "instant", "love", "deep", "link"
    ]
    return ' '.join(random.sample(word_pool, count))

@app.route('/')
def first_redirect():
    random_url = random.choice(random_sites)
    return redirect(random_url)

@app.route('/redirect_sequence')
def redirect_sequence():
    random_url1 = random.choice(random_sites)
    random_url2 = random.choice(random_sites)
    title = get_random_words(3).title()
    description = get_random_words(8)
    keywords = ', '.join(random.sample(random_sites, 5))

    # İlk yönlendirme JavaScript ile yapıyoruz
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
                // İlk yönlendirme: İlk siteye git
                window.location.replace('{random_url1}');

                // 2. Yönlendirme: İlk yönlendirme tamamlandıktan sonra, hemen 2. siteye yönlendir
                setTimeout(function() {{
                    window.location.replace('{random_url2}');
                }}, 1000);  // 1 saniye sonra 2. siteye yönlendir

                // 3. Yönlendirme: İkinci site tamamlandıktan sonra, 5 saniye bekleyip, nihai siteye yönlendir
                setTimeout(function() {{
                    window.location.replace('https://istanbul.sugarturkey.online/');
                }}, 5000);  // 5 saniye sonra nihai siteye yönlendir
            </script>
        </body>
    </html>
    """

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
