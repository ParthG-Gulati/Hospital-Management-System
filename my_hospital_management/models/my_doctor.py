from odoo import api, fields, models, _


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    doctor_shift = fields.Selection([
        ('shiftone', '06:00 - 14:00 hours'),
        ('shifttwo', '14:00 - 22:00 hours'),
        ('shiftthree', '22:00 - 06:00 hours'),
    ], required=True, default='shiftone', string='Shift')
    doctor_visitor = fields.Boolean(string="Visitor", default=False)
    doc_appointment_count = fields.Integer(string='Appointmnt Count', compute='doctor_appointment_count')
    doctor_address = fields.Text(string='Address')


    def doctor_appointment_count(self):
        '''Appointments Counts for doctors'''
        for rec in self:
            doc_appointment_count = self.env['calendar.event'].search_count([('doctor_app', '=', rec.id)])
            rec.doc_appointment_count = doc_appointment_count

    def action_open_appointment(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointments',
            'res_model': 'calendar.event',
            'domain': [('doctor_app', '=', self.id)],
            'view_mode': 'calendar,form,tree',
            'target': 'current',
        }
    