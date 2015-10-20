# -*- coding: utf-8 -*-
"""
    presidential-debate-simulator
    ~~~~~~

    Generates republican debates
    :copyright: (c) 2015 by Gregory Guterman.
    :license: MIT.
"""

from flask import Flask, url_for, render_template
import debate

app = Flask(__name__)
@app.route('/presidential-debate-simulator')
def pds():
    sentences = debate.generate_debate();
    return render_template('debatevis.html', sentences=sentences)

if __name__ == '__main__':
    app.run()
