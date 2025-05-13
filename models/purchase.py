from odoo import models, fields, api

class PurchaseOrder(models.Model):
    """
    توريث نموذج أمر الشراء لإضافة الفلترة والتجميع حسب الحالة
    هذا النموذج يستخدم في وحدة المشتريات (purchase) في نظام أودو
    """
    _inherit = 'purchase.order'
    
    # يمكن إضافة حقول إضافية هنا إذا كنت بحاجة إليها
    # على سبيل المثال:
    # state_description = fields.Char(string="وصف الحالة", compute="_compute_state_description")
    
    # def _compute_state_description(self):
    #     """حساب وصف الحالة بناءً على حالة طلب الشراء"""
    #     for record in self:
    #         if record.state == 'draft':
    #             record.state_description = "مسودة"
    #         elif record.state == 'sent':
    #             record.state_description = "طلب الموافقة"
    #         # ... إلخ
