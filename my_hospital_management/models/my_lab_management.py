from odoo import fields, models, api


class LabManagement(models.Model):
    _name = 'hospital.laboratory'

    test_no = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                          default=lambda self: _('New'))
    lab_patient = fields.Many2one('res.partner', string='Patient', required=True)
    lab_doctor = fields.Many2one('hr.employee', string="Doctor")
    lab_pathologist = fields.Many2one('hr.employee', string="Pathologist")
    requested_date = fields.Datetime(string="Report requested Date", required=True)
    analysis_date = fields.Datetime(string="Analysis Date", required=True)
    # test = fields.Many2one('test.type','Test Type')
    test_id = fields.Many2one('test.name', 'Test Name', required=True)
    report_line_ids = fields.One2many('report.line', 'report_name', 'Tests')

    @api.model
    def create(self, vals):
        if vals.get('test_no', _('New')) == _('New'):
            vals['test_no'] = self.env['ir.sequence'].next_by_code('hospital.laboratory') or _('New')
        res = super(LabManagement, self).create(vals)
        return res

