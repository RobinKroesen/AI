def palindroom(woord):
    omgekeerd_woord = woord[::-1]
    if omgekeerd_woord == woord:
        return True
    return False

print(palindroom("tarwewrat"))