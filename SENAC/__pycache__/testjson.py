import json



def appendJson(task, filename):
  with open(filename, 'r+') as f:
      data = json.load(f)
      data.append(task)
      f.seek(0)
      json.dump(data, f, indent=4)
      f.truncate()

task = {
    "title": 'task2',
    "description": 'descrição mt top',
    "active": True,
    "date": 'hoje'
}

appendJson(task, "tasks.json")