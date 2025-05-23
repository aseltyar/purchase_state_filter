# فلترة وتجميع حسب الحالة في طلبات الشراء

هذا الموديول يضيف خيارات فلترة وتجميع حسب الحالة في قائمة طلبات الشراء في نظام أودو.

## المميزات

- إضافة فلاتر جديدة للبحث حسب حالة طلب الشراء (مسودة، طلب الموافقة، مؤكد، ملغي، مغلق)
- إضافة خيار تجميع طلبات الشراء حسب الحالة

## التثبيت

1. نسخ المجلد إلى مسار إضافات أودو
   ```bash
   git clone https://github.com/aseltyar/purchase_state_filter.git
   ```

2. تحديث قائمة التطبيقات
   - قم بتسجيل الدخول إلى واجهة Odoo
   - انتقل إلى قائمة التطبيقات
   - انقر على زر "تحديث قائمة التطبيقات"

3. تثبيت التطبيق من قائمة التطبيقات
   - ابحث عن "Purchase State Filter"
   - انقر على زر التثبيت

## الاستخدام

1. انتقل إلى المشتريات > الطلبات > طلبات الشراء
2. استخدم الفلاتر الجديدة الموجودة في خيارات البحث
3. يمكنك التجميع حسب الحالة باستخدام خيار التجميع الجديد

## الإصدارات المدعومة

- أودو 17.0

## الترخيص

هذا الموديول متاح تحت رخصة AGPL-3.

## المؤلف

- Abdelrahman S. Eltyar