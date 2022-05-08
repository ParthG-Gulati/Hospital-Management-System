from odoo import fields, models, api, _


class LabManagement(models.Model):
    _name = 'hospital.laboratory'
    _rec_name = 'test_no'

    test_no = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                          default=lambda self: _('New'))
    lab_patient = fields.Many2one('res.partner', string='Patient', required=True)
    lab_doctor = fields.Many2one('hr.employee', string="Doctor")
    lab_pathologist = fields.Many2one('hr.employee', string="Pathologist")
    requested_date = fields.Datetime(string="Report requested Date", default=fields.Datetime.now)
    analysis_date = fields.Datetime(string="Analysis Date", default=fields.Datetime.now)
    # test = fields.Many2one('test.type','Test Type')
    test_id = fields.Many2one('test.name', 'Test Name', required=True)
    report_line_ids = fields.One2many('report.line', 'report_name', 'Tests')
    patient_age = fields.Integer(string='Age')
    manager_email = fields.Many2one('res.users',string="Manager")
    patient_gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender', default='male')
    patient_contact = fields.Char(string='Mobile No.')
    user_id = fields.Many2one('res.users', string='User')
    mail_id = fields.Char(string='Email', related='lab_patient.email')

    @api.model
    def create(self, vals):
        if vals.get('test_no', _('New')) == _('New'):
            vals['test_no'] = self.env['ir.sequence'].next_by_code('hospital.laboratory') or _('New')
        res = super(LabManagement, self).create(vals)
        return res

    def print_lab_test(self):
        return self.env.ref('my_hospital_management.patient_lab_report').report_action(self)

    def action_send_card(self):
        '''Send Mail action for Lab report'''
        template_id = self.env.ref('my_hospital_management.prescription_email_template').id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)

