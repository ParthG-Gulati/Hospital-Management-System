from odoo import api, fields, models


class HospitalMedicine(models.Model):
    _inherit = 'product.template'
    _rec_name = 'name'

    sale_lines_ids = fields.One2many('saleproduct.report', 'name')
    purchase_lines_ids = fields.One2many('hospitalproduct.purchase', 'product_name', 'Purchases')
    medicine_type = fields.Selection([
        ('one', 'Oral drugs'),
        ('two', 'Parenterals Formulations'),
        ('three', 'Topical Medicines'),
        ('fouth', 'Modified release Formulations'),
        ('fifth', 'Novel Drug Formulations'),
        ('sixth', 'Oncological Formulations')
    ], string="Medicine Type")
