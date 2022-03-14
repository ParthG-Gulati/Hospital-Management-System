# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'My Hospital Management',
    'version': '1.1',
    'summary': 'Hospital Management',
    'sequence': 1,
    'description': """
    """,
    'category': 'Productivity',
    'website': 'https://www.odoo.com',
    'images': [],
    'depends': ['base', 'hr', 'calendar', 'sale', 'sale_management', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/my_patient_view.xml',
        'views/my_doctor_view.xml',
        'views/my_appointment_view.xml',
        'views/appointment.xml',
        'views/my_hospitalization_view.xml',
        'views/hospitalization_view.xml',
        'views/my_outpatient_view.xml',
        'views/my_inpatient_view.xml',
        'views/my_hospital_pharmacy_view.xml',
        'views/my_lab_management_view.xml',
        'views/my_invoicing_view.xml',
        'views/my_prescription_view.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {
        'web._assets_primary_variables': [],
        'web.assets_backend': [],
        'web.assets_frontend': [],
        'web.assets_tests': [],
        'web.qunit_suite_tests': [],
        'web.assets_qweb': [],
    },
    'license': 'LGPL-3',
}