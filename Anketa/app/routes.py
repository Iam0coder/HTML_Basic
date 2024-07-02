from flask import render_template, request
from app import app

@app.route('/', methods=['GET', 'POST'])
def index():
    user = None
    if request.method == 'POST':
        name = request.form.get('name')
        city = request.form.get('city')
        age = request.form.get('age')
        hobby = request.form.get('hobby')
        if name and city and age and hobby:
            user = {
                'name': name,
                'city': city,
                'age': age,
                'hobby': hobby
            }
    return render_template('form.html', user=user)
