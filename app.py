from flask import Flask, render_template, url_for
from models import ALL_CLUBS, ALL_FIXTURES, ALL_RESULTS
from models.result import get_lastest_results

# sort clubs based on ranking
ALL_CLUBS.sort(key=lambda x: x.stats.get('league_stats').get('GD'), reverse=True)
ALL_CLUBS.sort(key=lambda x: x.stats.get('league_stats').get('PTS'), reverse=True)


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    results = get_lastest_results(ALL_RESULTS)
    return render_template('index.html', clubs=ALL_CLUBS, fixtures=ALL_FIXTURES, results=results)


if __name__ == '__main__':
    app.run(debug=True)
