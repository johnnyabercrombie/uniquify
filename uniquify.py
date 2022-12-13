"""
Tom Interview Question (Python)

Write a function that takes an list of strings and returns a new list of
strings that is the same as the input list, except duplicates are removed.

The elements of the returned list should have the same order as the
elements of the input list.

Example:
  uniquify(["k", "z", "a", "b", "k", "c", "b"])
      => ["k", "z", "a", "b", "c"]
"""


def uniquify(items):
    result = []
    already_checked = set()

    # Implementation here
    for item in items:
      if item not in already_checked:
        result.append(item)
        already_checked.add(item)

    return result


if __name__ == "__main__":
  result = uniquify(["k", "z", "a", "b", "k", "c", "b"])
  print(result) # => ["k", "z", "a", "b", "c"]
