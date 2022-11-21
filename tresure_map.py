map = [
  ['[ ]', '[ ]', '[ ]'],
  ['[ ]', '[ ]', '[ ]'],
  ['[ ]', '[ ]', '[ ]'],
]

print(f"      1.     2.     3. \n1. {map[0]}\n2. {map[1]}\n3. {map[2]}")

vertical_index = input('Which vertical line do you want?\n')
horizontal_index = input('Which horizontal line do you want?\n')

vertical_index_as_num = int(vertical_index) - 1
horizontal_index_as_num = int(horizontal_index) - 1

map[horizontal_index_as_num][vertical_index_as_num] = '[x]'

print(f"      1.     2.     3. \n1. {map[0]}\n2. {map[1]}\n3. {map[2]}")
