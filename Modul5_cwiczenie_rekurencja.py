# przyklad rekurencji liczenie od 1 do 10

def count_to(start=1, limit=10):
    print(start)
    if start == limit:
        return

    return count_to(start + 1, limit)

print(count_to(1,10))
