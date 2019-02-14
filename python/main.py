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

def projects(args):
  list = api.state['projects']
  for name in list:
    print(name['name'])

def tasks(args):
  items = api.state['items']
  for name in items:
    if name['project_id'] == 2190973782:
      print(name['content'])

def main():
  parser = argparse.ArgumentParser(
    prog='CLIツール',
    usage='python3 main2.py オプション',
    description='CLIツールのテストです',
    add_help=True,
  )
  
  parser.add_argument('--version', action='version', version='%(prog)s 1.0')
  parser.add_argument('-p', '--projects', action='store_true')
  parser.add_argument('-t', '--tasks', action='store_true')
  args = parser.parse_args()

  if args.projects: projects(args)
  if args.tasks: tasks(args)

if __name__ == "__main__": main()