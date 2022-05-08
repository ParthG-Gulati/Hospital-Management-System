from odoo import http
from odoo.http import request
class WebPatientPrescription(http.Controller):
    @http.route('/patient/prescription', type='http',auth='user',website=True)
    def view_prescriptions(self,**kwargs):
        prescription_record = request.env['my_hospital.prescription'].sudo().search([("patient_prescription_name_id","=",request.env.user.partner_id.id)])
        pre_count = request.env['my_hospital.prescription'].sudo().search_count(
            [("patient_prescription_name_id", "=", request.env.user.partner_id.id)])
        print("..................",pre_count)
        return request.render('my_hospital_management.patient_prescription_details',{'prescription_record': prescription_record})

