from odoo import models, fields


class HospitalAppointmentInherited(models.Model):
    _inherit = 'calendar.event'

    patient_app = fields.Many2one('res.partner', string='Patient Name', required=True)
    doctor_app = fields.Many2one('hr.employee', string='Doctor Name')
    hospitalization_selection = fields.Boolean(string='Hospitalize')

