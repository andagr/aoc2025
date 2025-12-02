input = ''
with open('input.txt', 'r') as file:
    input = file.read()

def is_repeated(product_id):
    product_id_str = str(product_id)
    product_id_str_len = len(product_id_str)
    if (product_id_str_len < 2):
        return False
    for part_len in range(1, product_id_str_len):
        if product_id_str_len % part_len != 0:
            continue
        first_part = product_id_str[:part_len]
        nbr_of_repeats = product_id_str_len // part_len
        part_repeated = first_part * nbr_of_repeats
        if part_repeated == product_id_str:
            return True
    return False

ranges = [(int(range.split('-')[0]), int(range.split('-')[1])) for range in input.split(',')]
invalid_product_ids = []
for (min, max) in ranges:
    for product_id in range(min, max+1):
        if is_repeated(product_id):
            invalid_product_ids.append(product_id)
        
print(sum(invalid_product_ids))
