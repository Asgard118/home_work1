import json

with open ('recept.txt', 'r', encoding='utf-8') as cook_book:
    cook_books = {}
    for dish in cook_book:
        dish_count = int(cook_book.readline())
        dish_list = []
        for count in range(dish_count):
            ingredient_name, quantity, measure = cook_book.readline().strip().split(' | ')
            dish_list.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        cook_book.readline()
        cook_books[dish.strip()] = dish_list
    fin = json.dumps(cook_books, ensure_ascii=False, indent=1)
    # print(fin)

def get_shop_list_by_dishes(dishes, person_count):
    fin_prod = {}
    for key in dishes:
        if key in cook_books:
            ingredients = cook_books[key]
            for ing in ingredients:
                name = ing['ingredient_name']
                measure = ing['measure']
                quantity = int(ing['quantity']) * person_count
                
                if name in  fin_prod:
                     fin_prod[name]['quantity'] += quantity
                else:
                     fin_prod[name] = {'measure': measure, 'quantity': quantity}
    return fin_prod 
        


# por_cal = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2)
# print(por_cal)


files = ['1.txt', '2.txt', '3.txt']

line_counts = {}

for file in files:
    with open(file, 'r', encoding='utf-8') as fil:
        lines = fil.readlines()
        line_counts[file] = len(lines)

sorted_files = sorted(line_counts, key=line_counts.get)

fynal = 'all files.txt'

with open(fynal, 'w', encoding='utf-8') as result_file:
    for file_name in sorted_files:
        result_file.write(f'{file_name}\n')
        result_file.write(f'{line_counts[file_name]}\n')
        
        with open(file_name, 'r', encoding='utf-8') as file:
            result_file.write(file.read())
        
