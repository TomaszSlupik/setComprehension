"""
Set comprehension w Pythonie to wyrażenie, 
które pozwala na tworzenie nowego zbioru (set) 
na podstawie istniejących danych lub iteracji. 
Jest to sposób na generowanie zbioru w jednej linii kodu.
"""

# Rozważmy dwukrotny rzut kostką. Zbuduj przestrzeń zdarzeń elementarnych omega, 
# następnie policz prawdopodobieństwo zdarzenia polegającego na uzyskania sumy oczek wyższej niż 10

dice = range(1, 7)
omega = {(i, j) for i in dice for j in dice}
sum_gt_10 = {(i, j) for (i, j) in omega if i + j > 10}
probability = len(sum_gt_10) / len(omega)
print(f'Probability: {probability:.2f}')

print('---')

# Rozważmy dwukrotny rzut kostką. Zbuduj przestrzeń zdarzeń elementarnych omega, 
# następnie policz prawdopodobieństwo zdarzenia polegającego na 
# uzyskaniu sumy kwadratów oczek wyższej lub równej 45.

diceTwo = range(1, 7)
omegaTwo = {(i, j) for i in diceTwo for j in diceTwo}
sum_square = {(i, j) for (i, j) in omegaTwo if i**2 + j**2>= 45}
probabilityTwo = len(sum_square) / len(omegaTwo)
print(f'Probability: {probabilityTwo:.2f}')

print('---')

# wyciągnąć unikalne tagi z listy artykułów na stronie o ciekawostkach w branży IT.
articles = [
    {
        'title': 'Artykuł 1',
        'tags': ['Python', 'baz danych'],
    },
    {
        'title': 'Artykuł 2',
        'tags': ['Python', 'web dev', 'frontend'],
    },
    {
        'title': 'Artykuł 3',
        'tags': ['AI', 'data science'],
    },
]

unique_tags = {tags for article in articles for tags in article['tags']}

print(unique_tags)

print("---")

# wyciągnij unikalne kombinacje rozmiarów i kolorów dla każdego produktu, które są dostępne w sklepie
products = [
    {
        'name': 'T-shirt',
        'color': 'white',
        'sizes': ['S', 'M', 'L', 'XL'],
    },
    {
        'name': 'Trousers',
        'color': 'blue',
        'sizes': ['M', 'L', 'XL'],
    },
    {
        'name': 'Jacket',
        'color': 'black',
        'sizes': ['L', 'XL', 'XXL'],
    },
    {
        'name': 'Shoes',
        'color': 'red',
        'sizes': ['40', '41', '42', '43', '44'],
    },
]

for product in products:
    for size in product['sizes']:
        print(f"{product['color']} - {size}")

print("---")

# wyodrębnienie zbioru unikalnych tagów z podanej listy produktów.
productsComputer = [
    {
        'id': 1,
        'name': 'Keyboard',
        'tags': ['electronics', 'computer accessories'],
    },
    {
        'id': 2,
        'name': 'Mouse',
        'tags': ['electronics', 'computer accessories'],
    },
    {
        'id': 3,
        'name': 'Monitor',
        'tags': ['electronics', 'monitors'],
    },
    {
        'id': 4,
        'name': 'Speakers',
        'tags': ['electronics', 'audio accessories'],
    },
    {
        'id': 5,
        'name': 'Headphones',
        'tags': ['electronics', 'audio accessories'],
    },
]

unique_tags = {tag for product in productsComputer for tag in product['tags']}
print(unique_tags)

print("---")

"""
1. Zamień wszystkie duże litery na małe.
2. Usuń przecinki oraz kropki.
3. Podziel tekst na wyrazy względem znaku spacji.
4. Pozostaw tylko wyrazy mające minimum 8 znaków.
5. Posortuj wyrazy alfabetycznie.
"""
lines = """
PLAYWAY\n\nPlayWay to producent i wydawca gier komputerowych 
i mobilnych. Spółka charakteryzuje się bardzo dużą liczbą 
zespołów deweloperskich i dużą liczbą gier wytwarzanych jednocześnie.
\nPlayWay prowadzi sprzedaż m. in. za pośrednictwem portalu STEAM, 
AppStore oraz GooglePlay. Rynki USA i Niemiec to dwa największe rynki 
sprzedaży Grupy.\nDodatkowo, spółka posiada PlayWay Campus - kampus 
dla współpracujących zespołów programistów.
"""

newLines = ("").join(lines.lower().replace(",", "").replace(".", "")).split()

bigLines = sorted([line for line in newLines if len(line) >= 8], reverse=False)

print(bigLines)

print("---")

# Przekształcenie na listę 
data = dict(zip(('a', 'b', 'c', 'd', 'e', 'f'),(1, 2, 3, 4, 5, 6)))

result  = [[key, value] for key, value in data.items()]
print(result)

print("---")

# Usunąć # ze słów 
hashtags = ['#travel', '#nature', '#photography']

hashtagsWithout = [myHash.replace("#", "") for myHash in hashtags]
hashSecond = [myHash.strip('#') for myHash in hashtags]

print(hashtagsWithout)
print(hashSecond)

print("---")

"""
Twoim zadaniem jest utworzenie nowej listy, która
będzie zawiera tylko te produkty z 
listy products, których cena jest wyższa niż 
średnia cena wszystkich produktów.
"""

products = [
    {'id': 1, 'name': 'Keyboard', 'price': 110},
    {'id': 2, 'name': 'Mouse', 'price': 50},
    {'id': 3, 'name': 'Monitor', 'price': 200},
    {'id': 4, 'name': 'Loudspeakers', 'price': 75},
    {'id': 5, 'name': 'Headphones', 'price': 90},
]

avgProducts = [prod['price'] for prod in products]
resultAvgProducts = sum(avgProducts) / len(avgProducts)

final_product = [prod for prod in products if prod['price'] > resultAvgProducts]

print(final_product)

print("---")

"""
nową listę, zawierającą tylko tych pacjentów, 
u których oba pomiary (ciśnienie skurczowe i rozkurczowe) 
są w normie, czyli mieści się w przedziale od 90/60 mmHg do 120/80 mmHg 
(pierwsza wartość to ciśnienie skurczowe, druga to rozkurczowe). 
"""

blood_pressure_results = [
    {'patient_id': 1, 'systolic': 118, 'diastolic': 72},
    {'patient_id': 2, 'systolic': 130, 'diastolic': 90},
    {'patient_id': 3, 'systolic': 120, 'diastolic': 80},
    {'patient_id': 4, 'systolic': 110, 'diastolic': 70},
    {'patient_id': 5, 'systolic': 140, 'diastolic': 95},
]

rangeSystolic = [90, 120]
rangeDiastolic = [60, 90]

numbRangeSystolic = list(range(rangeSystolic[0], rangeSystolic[1] + 1))
numbRangeDiastolic = list(range(rangeDiastolic[0], rangeDiastolic[1] + 1))

filter_blood_pressure_results = [blood for blood in blood_pressure_results if blood['systolic'] in numbRangeSystolic and blood['diastolic'] in numbRangeDiastolic]
print(filter_blood_pressure_results)

# zbiór kwadratów liczb od 1 do 10
squares = {x**2 for x in range(1, 11)}
print(squares)