import datetime as dt
from uuid import uuid1
from timeboard.calendars.US import Weekly8x5

class Worker:
  """
  A class to describe those whom change the level of entropy.
  """   
  
  def __init__(self, **kwargs):
    self.name = kwargs.get('name')
    self.profile = kwargs.get('profile')
    self.rate = kwargs.get('rate')
    self.availability = kwargs.get('availability')
    self.sem_context = kwargs.get('sem_context')
    if kwargs.get('worker_id'):
      self.worker_id = kwargs.get('worker_id')
    else:
      self.worker_id = uuid1()
    if kwargs.get('manager'):
      self.manager = True
      def alter_task(self, task_ids):
        return None
    
    if kwargs.get('pm'):
      self.pm = True
  
  def __repr__(self):
    return "<Worker name:%s, worker_id:%s>" % (self.name, self.worker_id)
  
  def __str__(self):
    return "<Worker name:%s, worker_id:%s>" % (self.name, self.worker_id)
  
# ----------

if __name__ == '__main__':

  a_worker = Worker(name = 'Julio', availability = Weekly8x5())
  print(a_worker)
