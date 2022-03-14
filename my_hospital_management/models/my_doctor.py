from odoo import api, fields, models, _


class HrEmployee(models.Model):
     _inherit = 'hr.employee'
     doctor_shift = fields.Selection([
          ('shiftone', '06:00 - 14:00 hours'),
          ('shifttwo', '14:00 - 22:00 hours'),
          ('shiftthree', '22:00 - 06:00 hours'),
     ], required=True, default='shiftone', string='Shift')
     doctor_visitor = fields.Boolean(string="Visitor", default=False)
