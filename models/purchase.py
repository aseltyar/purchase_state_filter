from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    
    # يمكن إضافة حقول إضافية هنا إذا كنت بحاجة إليها
    
    # يمكن إضافة طرق خاصة بالفلترة والتجميع هنا