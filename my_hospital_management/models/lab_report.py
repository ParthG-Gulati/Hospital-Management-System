from odoo import api, models, fields


class TestReport(models.Model):
    _name = 'report.line'

    report_name = fields.Many2one('hospital.laboratory')

    lab_test_name = fields.Many2one('test.name', string="Test Name")
    lab_test_type = fields.Many2one('test.type', string="Type")
    test_result = fields.Char(string='Result')
    normal_range = fields.Char(string="Normal Range")
    test_unit = fields.Char(string='Test Unit')