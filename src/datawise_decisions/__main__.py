import sys
from datawise_decisions import seer

def main():
    print(seer.see_rul(sys.argv[1], sys.argv[2]))
    

if __name__ == "__main__":
    main()