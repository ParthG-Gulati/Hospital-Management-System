from odoo import fields, models, api


class InpatientInherited(models.Model):
    _inherit = 'sale.order'

    attend_doctor_id = fields.Many2one('hr.employee', string='Attending Doctor')
