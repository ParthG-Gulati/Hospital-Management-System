from odoo import api, models, fields


class HospitalPrescriptionLine(models.Model):
    _name = "prescription.line"
    _description = "prescription of doctor"

    medicine_id = fields.Many2one('my_hospital.prescription', string="Medicine")
    medicine_name = fields.Many2one('product.template', string="Medicine")

    medicine_dose = fields.Integer(string='Dose')
    # medic_time = fields.Many2many('medication.time' , string="Time")
    medicine_time = fields.Many2many('medication.time' , string="Time")
    medicine_timing = fields.Selection([
        ('before', 'Before Food'),
        ('after', 'After Food')
    ], string='Timing')




