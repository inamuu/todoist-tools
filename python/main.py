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
  print('### プロジェクト一覧')
  for name in list:
    print(name['name'])

def tasks(args):
  list = api.state['projects']
  for projects_id in list:
    if projects_id['name'] == args.tasks:
      tasks_project_id = projects_id['id']

  items = api.state['items']
  print('### タスク一覧')
  for name in items:
    if name['project_id'] == tasks_project_id:
      print(name['content'])

def main():
  parser = argparse.ArgumentParser(
    prog='CLIツール',
    usage='python3 main2.py オプション',
    description='CLIツールのテストです',
    add_help=True,
  )
  
  parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
  parser.add_argument('-p', '--projects', action='store_true', help='プロジェクト一覧を表示します')
  parser.add_argument('-t', '--tasks', help='タスク一覧を表示します')
  args = parser.parse_args()

  if args.projects: projects()
  if args.tasks: tasks(args)

if __name__ == "__main__": main()