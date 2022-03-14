from odoo import fields, models, api


class HospitalizationInherited(models.Model):
    _inherit = ['sale.order']

    attending_doctor_id = fields.Many2one('hr.employee', string='Attending Doctor')
