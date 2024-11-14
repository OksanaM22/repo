# Подробнее о функциях
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(data_structure):
  summa_ = 0
  if isinstance(data_structure, (tuple, set, list)):
    for element in data_structure:
      summa_ += calculate_structure_sum(element)
  elif isinstance(data_structure, (int, float)):
    summa_ += data_structure
  elif isinstance(data_structure, str):
    summa_ += len(data_structure)
  elif isinstance(data_structure, dict):
    for key, value in data_structure.items():

      summa_ += calculate_structure_sum(value)
      summa_ += calculate_structure_sum(key)
  return summa_

result = calculate_structure_sum(data_structure)
print(result)
