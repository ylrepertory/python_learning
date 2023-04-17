import pizza
from pizza import make_pizza
from pizza import make_pizza as mp
if __name__ == '__main__':
    mp(16, 'pepperoni')
    make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')