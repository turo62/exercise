def nb_year(p0, percent, aug, p):
    years = 0
    while p0 <= p:
        p0 += int(p0 * percent / 100) + aug
        years += 1
    return years

def main():
    years = nb_year(1500000, 0.25, 1000, 2000000)
    print(years)

if __name__ == "__main__":
    main()
