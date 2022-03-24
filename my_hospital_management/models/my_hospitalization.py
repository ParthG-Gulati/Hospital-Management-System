from odoo import fields, api, models, _


class HospitalHospitalization(models.Model):
    _name = 'hospital.hospitalization'
    _rec_name = 'name_id'
    hospitalization_sequence = fields.Char(string='Registration No.', required=True, copy=False, readonly=True,
                                           default=lambda self: _('New'))
    name_id = fields.Many2one('res.partner', string='Patient', required=True)
    doctor_id = fields.Many2one('hr.employee', string='Doctor')
    hospitalization_date = fields.Datetime(string='Hospitalization Date', required=True)
    discharge_date = fields.Datetime(string='Expected discharge', )
    reason_for_admission = fields.Text(string="Reason for admission")
    remarks = fields.Text(string='Remarks')
    treatment_plan = fields.Text(string='Treatment Plan')
    discharge_plan = fields.Text(string='Discharge Plan')
    state = fields.Selection([
            ('draft', 'Draft'),
            ('confirmed', 'Confirmed'),
            ('hospitalized', 'Hospitalized'),
            ('discharged','Discharged'),
            ('canceled', 'Canceled')
    ], string='Status', default='draft')

    def action_drafted(self):
        self.state = 'draft'

    def action_confirmed(self):
        self.write({'state': 'confirmed'})

    def action_hospitalized(self):
        self.state = 'hospitalized'

    def action_discharged(self):
        self.state = 'discharged'

    def action_canceled(self):
        self.state = 'canceled'

    @api.model
    def create(self, vals):
        '''Sequence for patients Hospitalize'''
        if vals.get('hospitalization_sequence', _('New')) == _('New'):
            vals['hospitalization_sequence'] = self.env['ir.sequence'].next_by_code('hospital.hospitalization') or _('New')
        res = super(HospitalHospitalization, self).create(vals)
        return res
