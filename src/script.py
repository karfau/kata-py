#!python


def main(*args):
    return "returned from main"

if __name__ == '__main__':
    import sys
    print "provided arguments:", sys.argv
    if len(sys.argv) > 1:
        print main(sys.argv[1:])
    else:
        for line in sys.stdin:
            print main(line.split(', '))
