import datetime as dt
from uuid import uuid1
from timeboard.calendars.US import Weekly8x5

class Task:
  """
  A class to describe the observable change in entropy.
  """   
  
  def __init__(self, **kwargs):
    self.descriptives = kwargs.get('descriptives')
    self.output = kwargs.get('output')
    self.duration = kwargs.get('duration')
    self.start_date = kwargs.get('start_date')
    self.dependencies = kwargs.get('dependencies')
    self.sem_context = kwargs.get('sem_context')
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
    return "<Task descriptives:%s, task_id:%s>" % (self.descriptives, self.task_id)
  
  def __str__(self):
    return "<Task descriptives:%s, task_id:%s>" % (self.descriptives, self.task_id)
  
# ----------

if __name__ == '__main__':

  descriptives = [{'title': 'Some bullshit'},{'description': 'Some comment describe the crap.'}]
  a_task = Task(descriptives = descriptives)
  print(a_task)
