from odoo import fields, api, models


class DiseaseName(models.Model):


class Diseaseslines(models.Model):
    _name = 'patient.disease.line'

    disease_line = fields.Many2one('res.partner')
    disease_sequence = fields.Integer(string="No.")
    patient_disease_name=fields.Many2one('patient.disease','Disease Name')
    disease_status = fields.Selection([
        ('one','Cured'),
        ('two','Active')
    ],)