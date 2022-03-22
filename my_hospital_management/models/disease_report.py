from odoo import fields,models,api

class ReportDisease(models.Model):
    _name='main.disease'

    patient_disease_line = fields.Many2one('res.partner')
    patient_disease_sequence = fields.Integer(string="No.")
    my_patient_disease_name = fields.Many2one('patient.disease', 'Disease Name')
    patient_disease_status = fields.Selection([
        ('one', 'Cured'),
        ('two', 'Active')
    ], )