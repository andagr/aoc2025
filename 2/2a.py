input = ''
with open('input.txt', 'r') as file:
    input = file.read()

ranges = [(int(range.split('-')[0]), int(range.split('-')[1])) for range in input.split(',')]
invalid_product_ids = []
for (min, max) in ranges:
    for product_id in range(min, max+1):
        product_id_str = str(product_id)
        if len(product_id_str) % 2 == 0:
            left = product_id_str[:len(product_id_str)//2]
            right = product_id_str[len(product_id_str)//2:]
            if left == right:
                invalid_product_ids.append(product_id)

print(sum(invalid_product_ids))