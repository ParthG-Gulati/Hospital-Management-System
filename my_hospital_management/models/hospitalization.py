from odoo import fields, models, api


class HospitalizationInherited(models.Model):
    _inherit = ['sale.order']

    attending_doctor_id = fields.Many2one('hr.employee', string='Attending Doctor')
    ward = fields.Selection([
        ('general', 'GENERAL WARD'),
        ('causality', 'CAUSALITY'),
        ('semi_special_rooms', 'SEMI-SPECIAL ROOM'),
        ('special_ward', 'SPECIAL WARD'),
        ('deluxe_room', 'DELUXE ROOM'),
        ('icu', 'ICU')
    ], default='general', string='Ward')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('sale', 'Confirmed'),
        ('cancel', 'Cancel'),
        ('done', 'Done'),

    ])

    discharge =fields.Boolean(string='Discharged')

    bed = fields.Selection([
        ('bed_001', 'BED 001'),
        ('bed_002', 'BED 002'),
        ('bed_003', 'BED 003'),
        ('bed_004', 'BED 004'),
        ('bed_005', 'BED 005'),
        ('bed_006', 'BED 006'),
        ('bed_007', 'BED 007'),
        ('bed_008', 'BED 008'),
        ('bed_009', 'BED 009'),
        ('bed_010', 'BED 010'),
    ], string='Bed')

    _sql_constraints = [
        ('patient_bed', 'UNIQUE(bed)', 'Bed Already taken , please choose other bed ')
    ]

    # def action_discharge(self):
    #     self.state = 'discharge'
