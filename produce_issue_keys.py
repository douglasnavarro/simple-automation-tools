import sys

def produce_issue_keys(prefix, start, end):
    issues = ""
    for i in range(int(start), int(end)+1):
        issues += " " + prefix + str(i)
    print(issues)

def main():
    produce_issue_keys(sys.argv[1], sys.argv[2], sys.argv[3])

main()
