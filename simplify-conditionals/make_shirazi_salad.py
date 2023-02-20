# by Kami Bigdely
# Consolidate conditional expressions

def dice(ingredients):
    print("diced all ingredients.")
def mix_all(diced_ingredients):
    print("mixed all.")
def add_salt():
    print('added salt.')
def pour(liquid):
    print('poured', liquid + '.',)
def check_ingredients(food):
    ingredients= ['cucumber', 'tomato', 'lemon juice', 'onion']
    return not all(ingredient in food for ingredient in ingredients)


def make_shirazi_salad(ingredients):
    if check_ingredients(ingredients):
        print('lacks ingredients.')
        return
    dice(ingredients)
    mix_all(ingredients)
    add_salt()
    pour('lemon juice')
    print('Your yummy shirazi salad is ready!')

if __name__ == "__main__":
    make_shirazi_salad(['cucumber', 'tomato', 'lemon juice', 'onion'])
