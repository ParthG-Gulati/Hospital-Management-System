from odoo import api, models, fields


class HospitalPrescriptionLine(models.Model):
    _name = "prescription.line"
    _description = "prescription of doctor"

    medicine_id = fields.Many2one('my_hospital.prescription', string="Medicine")
    medicine_dose = fields.Integer(string='Dose')
    medicine_time = fields.Selection([
        ('morning', 'Morning'),
        ('noon', 'Noon'),
        ('night', 'Night')
    ], default='morning', string="Time")
    medicine_timing = fields.Selection([
        ('before', 'Before Food'),
        ('after', 'After Food')
    ], string='Timing')




