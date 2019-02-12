import sys
import argparse
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
  for name in list:
    print(name['name'])

def tasks():
  items = api.state['items']
  for name in items:
    if name['project_id'] == 2190973782:
      print(name['content'])

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
  
  parser_tasks = subparsers.add_parser('tasks', help='tasksだよ')
  parser_tasks.set_defaults(fn=tasks)

  args = parser.parse_args()
  args.fn()

if __name__ == "__main__": main()