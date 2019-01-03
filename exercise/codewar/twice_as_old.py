def twice_as_old(dad_years_old, son_years_old):
    years = abs(dad_years_old - 2 * son_years_old)
    return years

def main():
    years = twice_as_old(55, 30)
    print(years)


if __name__ == "__main__":
    main()