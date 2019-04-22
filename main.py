import apexApi
import argparse


def parseArgs():
    parser = argparse.ArgumentParser(description='apBotex')
    parser.add_argument("platform",type = int)
    parser.add_argument("username")
    args = parser.parse_args()
    return args.platform, args.username


def main(platform, username):
    bot = apexApi.apexApi(platform, username)
    print(bot.anotherGet())

if __name__ == "__main__":
    platform , username = parseArgs()
    main(platform, username)
