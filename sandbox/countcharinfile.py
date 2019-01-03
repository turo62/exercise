# Count number of specified character in imported file.


def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count


def get_input():
    filename = input("Enter a filename: ")
    char = input("Enter a character: ")
    with open(filename) as f:
        text = f.read(  )
    return text, char


def main():
       text, char = get_input()
       count = count_char(text, char)
       print(text, "Contains ", char," character: ", count)


if __name__ == '__main__':
        main()

