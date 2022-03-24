from odoo import api, models, fields


class HospitalMedicationLine(models.Model):
    _name = "medication.line"
    _description = "Medication"

    medication_id = fields.Many2one('res.partner', string="Medicine")
    medication_name = fields.Many2one('product.template', string="Medicine")

    medication_dose = fields.Integer(string='Dose')
    medication_time = fields.Selection([
        ('morning', 'Morning'),
        ('noon', 'Noon'),
        ('night', 'Night')
    ], default='morning', string="Time")
    medication_timing = fields.Selection([
        ('before', 'Before Food'),
        ('after', 'After Food')
    ], string='Timing')