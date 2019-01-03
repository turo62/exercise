# Mine.
def tribonacci(signature, n):
    tribs = [signature[0], signature[1], signature[2]]
    if n == 0:
        return []
    if n == 1:
        tribs = [tribs[0]]
        return tribs
    if n == 2:
        tribs = [tribs[0], tribs[1]]
        return tribs
    for i in range(3, n):
        tribs.append(tribs[-1] + tribs[-2] + tribs[-3])
    return tribs

def main():
    tribs = tribonacci([10, 17, 16], 1)
    print(tribs)

if __name__ == '__main__':
        main()

# Codewar best practice.

def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res
