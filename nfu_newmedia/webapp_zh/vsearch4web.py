 # -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, escape


app = Flask(__name__)



@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    return render_template('map.html',
                           the_title='广东省城市地图！')


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_title='广东省城市地图！')



if __name__ == '__main__':
    app.run(debug=True)
