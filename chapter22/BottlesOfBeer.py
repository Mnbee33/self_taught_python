def bottles_of_beer(bob):
    """
    Prints Bottles of Beer on the Wall lyrics.
    :param bob: Must be a positive integer.
    """

    if bob < 1:
        print("""No more bottles of beer on the wall.
                No more bottles of beer.""")
        return

    tmp = bob
    bob -= 1
    print("""{tmp} bottles of beer on the wall.
{tmp} bottles of beer.
Take one down, pass it around,
{bob} bottles of beer on the wall.
""".format(tmp = tmp, bob = bob))
    bottles_of_beer(bob)

bottles_of_beer(99)
