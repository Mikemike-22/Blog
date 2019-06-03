from flask import render_template




@main.route('/')
def index():
    random = requests.get('http://quotes.stormconsultancy.co.uk/random.json').json()

    sports = Blog.get_blogs('Sports-Blog')
    travel = Blog.get_blogs('Travel-Blog')
    fitness = Blog.get_blogs('Fitness-Blog')
    fashion = Blog.get_blogs('Fashion-Blog')
    food = Blog.get_blogs('Food-Blog')
    politics = Blog.get_blogs('Political-Blog')

    return render_template('index.html', sports = sports, travel = travel, fitness = fitness, fashion = fashion, food = food, random = random)
