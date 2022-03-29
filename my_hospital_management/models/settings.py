from odoo import models, fields, api


class HospitalSettings(models.TransientModel):
    _inherit = 'res.config.settings'