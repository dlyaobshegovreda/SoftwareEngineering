def main(*args):
    return sum(args) / len(args)

if __name__ == '__main__':
    print(main(0, 4, 8))