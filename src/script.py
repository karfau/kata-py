#!python


def main(*args):
    return args[0]

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        # arguments win over std in, pass all but the first one to main
        print "provided arguments:", sys.argv
        print main(*sys.argv[1:])
    else:
        for line in sys.stdin:
            # pass every line from stdin as space separated arguments
            print main(*line.split())
