from flask import Flask
import random
import os

app = Flask(__name__)

random_sites = [
    "https://www.google.com",
    "https://www.bizdeoyunlarbedava.tr.gg"
]

def get_random_words(count):
    word_pool = [
        "sunshine","freedom","adventure","mystery","turkey","istanbul",
        "beauty","night","dream","sugar","online","future","random",
        "power","girl","fun","secret","code","page","story","click",
        "explore","now","hidden","world","instant","love","deep","link"
    ]
    return ' '.join(random.sample(word_pool, count))

@app.route('/')
@app.route('/redirect_sequence')
def redirect_sequence():
    # Arka planda yüklemek için 1 adet rastgele site
    random_url = random.choice(random_sites)
    # Dinamik meta ve title
    title       = get_random_words(3).title()
    description = get_random_words(8)
    keywords    = ', '.join(random.sample(get_random_words(5).split(), 5))
    final_url   = 'https://istanbul.sugarturkey.online/'

    return f"""
    <html>
      <head>
        <title>{title}</title>
        <meta name="description" content="{description}">
        <meta name="keywords" content="{keywords}">
      </head>
      <body>
        <p>2 saniye içinde yönlendiriliyorsunuz...</p>

        <!-- Gizli iframe: arka planda random_url'i yükle -->
        <iframe src="{random_url}" style="display:none;"></iframe>

        <script>
          // 2 saniye sonra ana pencereyi final_url'e yönlendir
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
