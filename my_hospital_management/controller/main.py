from odoo import http
from odoo.http import request
from datetime import datetime
from dateutil.relativedelta import relativedelta


class WebsiteAppoitment(http.Controller):
    @http.route('/book/appointment/',type='http',auth='user',website=True)
    def appointment_book(self,**kwargs):
        patient_record = request.env['res.partner'].search([])
        doctor_record = request.env['hr.employee'].search([])
        return request.render('my_hospital_management.book_appointment_online',{'doctor_record' : doctor_record , 'patient_record' : patient_record})

    @http.route('/appointment/placed/',type='http',auth='user',website=True)
    def create_appointment(self,**kwargs):
        val_list = {
            'patient_app' : kwargs.get('patient_name'),
            'name' : kwargs.get('meeting_subject'),
            'start' : datetime.strptime(kwargs.get('appointment_date'), '%Y-%m-%dT%H:%M') + relativedelta(hours=-6, minutes=30),
            'doctor_app' : kwargs.get('doctor_name'),
            'stop' : datetime.strptime(kwargs.get('appointment_date_end'), '%Y-%m-%dT%H:%M') + relativedelta(hours=-6, minutes=30),
            # 'duration' : kwargs.get('duration')
        }
        request.env['calendar.event'].sudo().create(val_list)
        return request.render('my_hospital_management.appointment_submit',{})