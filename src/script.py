#!python


def main():
    return "returned from main"

if __name__ == '__main__':
    import sys
    print "provided arguments:", sys.argv
    print main()
