def min_max(lst):
  lst.sort()
  tempor = [lst[0],lst[-1]]
  return tempor


def main():
    tempor = min_max([ 0, 112, 5, 0, 0 ])
    print(tempor)

if __name__ == "__main__":
    main()