from odoo import fields,models,api

class PatientSymptoms(models.Model):
    _name='patient.symptom'

    sequence = fields.Many2one('calendar.event','Sequence')

    sequence_field= fields.Integer(string="Sequence")
    symptom = fields.Char(string="Symptoms")