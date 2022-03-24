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
    quantity_sold = fields.Integer(string="Quantity Sold")
    quantity_remaining = fields.Integer(string="Quantity Remains")
    quantity_purchase =fields.Integer(string="Quantity Purchased")
    vendor = fields.Char(string="Vendor Name")


    def wizard_sell(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'sale.update',
            'view_mode': 'form',
            'target': 'new'}

    def wizard_purchase(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'purchase.update',
            'view_mode': 'form',
            'target': 'new'}
