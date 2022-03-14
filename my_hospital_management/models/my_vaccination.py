from odoo import api, fields, models


class HospitalVaccination(models.Model):
    _name = 'hospital.vaccination'
    _description = 'Vaccination'

    vaccine_name = fields.Char(string='Vaccine Name')
    vaccine_dose = fields.Integer(string='Dose')
    vaccine_date = fields.Date(strin='Date')
    hospital_management_vaccine_id = fields.Many2one('res.partner', string='Vaccine')
