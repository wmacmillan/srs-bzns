import datetime as dt
from uuid import uuid1
from timeboard.calendars.US import Weekly8x5

class Task:
  """
  A class to describe the observable change in entropy.
  """   
  
  def __init__(self,*args, **kwargs):
    self.descriptives = kwargs.get('descriptives')
    self.output = kwargs.get('output')
    self.duration = kwargs.get('duration')
    self.start_date = kwargs.get('start_date')
    self.end_date = kwargs.get('end_date')
    self.dependencies = kwargs.get('dependencies')
    self.sem_context = kwargs.get('sem_context')
    self.assigned_workers = kwargs.get('assigned_workers')
    self.other_people = kwargs.get('other_people')
    if kwargs.get('task_id'):
      self.task_id = kwargs.get('task_id')
    else:
      self.task_id = uuid1()
    if kwargs.get('milestone'):
      self.milestone = True
      def aggregate_output(self, task_ids):
        return None
    
    if kwargs.get('meta_task'):
      self.meta_task = True
  
  def __repr__(self):
    printstring = f"Task id: {self.task_id}\nTitle: {self.descriptives['title']}"
    if self.assigned_workers:
      printstring = printstring + f"\nWorkers: {self.assigned_workers}"
    return printstring
  
  def __str__(self):
    printstring = f"Task id: {self.task_id}\nTitle: {self.descriptives['title']}"
    if self.assigned_workers:
      printstring = printstring + f"\nWorkers: {self.assigned_workers}"
    return printstring
  
# ----------

if __name__ == '__main__':

  workers = uuid1()
  descriptives = {'title': 'Some bullshit','description': 'Some comment describe the crap.'}
  a_task = Task(descriptives = descriptives, assigned_workers = workers)
  print(a_task)
