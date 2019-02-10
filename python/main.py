import sys
import argparse
from todoist.api import TodoistAPI

def helloa():
    print("hello A")

def hellob():
    print("hello B")


def main():
  parser = argparse.ArgumentParser(
    prog='CLIツール',
    usage='python3 main2.py サブコマンド',
    description='CLIツールのテストです',
    add_help=True,
  )
  
  parser.add_argument('--version', action='version', version='%(prog)s 1.0')
  subparsers = parser.add_subparsers(dest='[エラー内容] サブコマンド必須です。 -h, --help で確認してください。', title='subcomands')
  subparsers.required = True
  
  parser_helloa = subparsers.add_parser('helloa', help='helloaだよ')
  parser_helloa.set_defaults(fn=helloa)
  
  parser_hellob = subparsers.add_parser('hellob', help='hellobだよ')
  parser_hellob.set_defaults(fn=hellob)

  args = parser.parse_args()
  args.fn()

if __name__ == "__main__": main()