def ft_count_harvest_recursive(i=1, days=int(input("Days until harvest: "))):
    print("Day ", i)
    if (i < days):
        ft_count_harvest_recursive(i=i+1)
    else:
        print("Harvest time!")
