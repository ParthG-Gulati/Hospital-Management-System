from odoo import api, fields, models


class LabTestName(models.Model):
    _name = 'test.name'
    _rec_name = 'lab_test_name'

    lab_test_name = fields.Char(string="Test Name")


class LabTestType(models.Model):
    _name = 'test.type'
    _rec_name = 'lab_test_type'

    lab_test_type=fields.Char(string="Type",required=True)
