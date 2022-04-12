from odoo import http
from odoo.http import request
class WebLabReport(http.Controller):
    @http.route('/patient/labreport', type='http',auth='user',website=True)
    def view_prescriptions(self,**kwargs):
        lab_record = request.env['hospital.laboratory'].sudo().search([("lab_patient","=",request.env.user.partner_id.id)])
        return request.render('my_hospital_management.patient_lab_details',{'lab_record': lab_record})
