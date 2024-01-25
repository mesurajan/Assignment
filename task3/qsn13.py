"""
Write a function concat_tuples(tuple1, tuple2) that takes two tuples as arguments and returns a new tuple
containing elements from both tuples.
"""


def concat_tuples(tuple1, tuple2):
    result_tuple = tuple1 + tuple2
    return result_tuple


tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c")

result = concat_tuples(tuple1, tuple2)
print(result)
