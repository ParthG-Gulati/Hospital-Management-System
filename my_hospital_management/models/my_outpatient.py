from odoo import models, fields, api


class HospitalOutpatient(models.Model):
    _inherit = ['sale.order']
