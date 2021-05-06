DISHES_DICT = {'Dish '+ str(int(i-11)) : i for i in range(12,19)}
DRINKS_DICT = {'Drink '+ str(int(i-4)) : i for i in range(5,10)}

def combinations(limit):
    count = 0
    combinations = {}

    for dish,dish_cost in DISHES_DICT.items():
        for drink,drink_cost in DRINKS_DICT.items():
            if dish_cost + drink_cost <= limit:
                combinations[dish+' '+drink] = 'Cost: '+ str(int(dish_cost+drink_cost))
                count +=1
    return combinations, count

def run():
    print(combinations(35))

if __name__ == '__main__':
    run()