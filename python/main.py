import sys
import argparse
import json
import os
from todoist.api import TodoistAPI
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
api = TodoistAPI(os.environ.get("APITOKEN"))
api.sync()

def projects():
    list = api.state['projects']
    print(list[0]['name'])

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
  
  parser_projects = subparsers.add_parser('projects', help='projectsだよ')
  parser_projects.set_defaults(fn=projects)
  
  parser_hellob = subparsers.add_parser('hellob', help='hellobだよ')
  parser_hellob.set_defaults(fn=hellob)

  args = parser.parse_args()
  args.fn()

if __name__ == "__main__": main()