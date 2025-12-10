import argparse
import sys
import os
import requests

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:145.0) Gecko/20100101 Firefox/145.0"

parser = argparse.ArgumentParser(prog="webscan", description="web scanner for existing (and/or hidden) directories", 
                                 epilog="(c) Ivaylo Vasilev")
parser.add_argument("url", nargs="?", help="specify url")
parser.add_argument("-a", "--user-agent", metavar="str", default=USER_AGENT, help="specify user agent")
parser.add_argument("-w", "--wordlist", metavar="txt", required=True, help="specify wordlist")
parser.add_argument("--version", action="version", version="%(prog)s 1.1.0", help="show program version")
args = parser.parse_args()


def main():
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    
    if not args.url:
        parser.print_usage()
        print("error: mising required argument 'url'")
        sys.exit(2)
    elif not os.path.exists(args.wordlist):
        print(f"error: wordlist file '{args.wordlist}' does not exist")
        sys.exit(3)
    
    target_url = args.url.rstrip("/")

    counter = 0

    print("scanning ...")
    with open(args.wordlist, "r") as wordlist:
        for line in wordlist.readlines():
            full_url = (target_url + "/" + line.strip() + "/")

            response = request_dirs(full_url)

            if response:
                print(f"[+] {full_url} | code: {response.status_code}")
                counter += 1
    
    if counter == 0:
        print("nothing found.")


def request_dirs(url):
    user_agent = args.user_agent
    try:
        return requests.get(url, headers={"User-Agent": user_agent})
    except requests.exceptions.ConnectionError:
        pass


if __name__ == "__main__":
    main()
