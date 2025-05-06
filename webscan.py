import argparse
import sys
import os
import requests

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:138.0) Gecko/20100101 Firefox/138.0"

parser = argparse.ArgumentParser(prog="webscan", description="web scanner for existing (and/or hidden) directories", 
                                 epilog="(c) Ivaylo Vasilev")
parser.add_argument("url", nargs="?", help="specify url")
parser.add_argument("-a", "--user-agent", metavar="str", default=USER_AGENT, help="specify user agent")
parser.add_argument("-w", "--wordlist", metavar="txt", help="specify wordlist")
parser.add_argument("--version", action="version", version="%(prog)s 1.0.4", help="show program version")
args = parser.parse_args()


def main():
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    
    if not args.url:
        parser.print_usage()
        sys.exit("error: mising required argument 'url'")
    if not args.wordlist:
        parser.print_usage()
        sys.exit("error: missing required argument -w <wordlist>")
    elif not os.path.exists(args.wordlist):
        sys.exit(f"error: wordlist file '{args.wordlist}' does not exist")
    
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
