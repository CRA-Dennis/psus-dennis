from odoo import models, fields

class TodoTask(models.Model):
  _name = 'todo.task'
  _description = "To-Do Task"

  name = fields.Char(string="Task Description", required=True)
  due_date =fields.Date(string="Due Date")
  priority = fields.Selection(
    [('low', 'Low'), ('medium', 'Medium'), ('high', 'High')],
    string="Priority", default='medium'
  )
  status = fields.Selection(
  [('todo', 'To Do'), ('in_progress', 'In Progress'), ('done', 'Done')],
  string="Status", default='todo'
  )
