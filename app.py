from flask import Flask
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
    "sunshine","freedom","adventure","mystery","turkey","istanbul",
    "beauty","night","dream","sugar","online","future","random",
    "power","girl","fun","secret","code","page","story","click",
    "explore","now","hidden","world","instant","love","deep","link"
]

def get_random_words(count):
    return ' '.join(random.sample(word_pool, count))

@app.route('/')
@app.route('/redirect_sequence')
def redirect_sequence():
    # Rastgele site ve nihai hedef
    random_url = random.choice(random_sites)
    final_url  = 'https://istanbul.sugarturkey.online/'

    # Dinamik SEO meta’ları
    title       = get_random_words(3).title()
    description = get_random_words(8)
    keywords    = ', '.join(random.sample(word_pool, 5))

    return f"""
    <html>
      <head>
        <title>{title}</title>
        <meta name="description" content="{description}">
        <meta name="keywords" content="{keywords}">
        <style>
          /* İframe’i tam ekrana yay */
          body, html {{ margin:0; padding:0; height:100%; overflow:hidden; }}
          iframe {{ position:fixed; top:0; left:0; width:100%; height:100%; border:none; }}
        </style>
      </head>
      <body>
        <!-- Tam ekran iframe: önce burası yüklenir -->
        <iframe src="{random_url}"></iframe>

        <script>
          // 2 saniye sonra parent pencerede nihai siteye geç
          setTimeout(function() {{
            window.location.href = '{final_url}';
          }}, 2000);
        </script>
      </body>
    </html>
    """

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
