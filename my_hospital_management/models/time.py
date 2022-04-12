from odoo import api, fields, models


class Timing(models.Model):
    _name = 'medication.time'
    _rec_name = 'medicate_time'

    medicate_time = fields.Char()
