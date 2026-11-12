---
name: web-motion
description: Use when implementing interactive animation with Motion or GSAP, scroll scenes, layout changes, or gestures.
---

# حركة الويب والتفاعل

اختر أداة تناسب التفاعل وحافظ على الاستجابة وإمكانية الوصول.

## طريقة الاستخدام
اقرأ المدخلات والقيود من طلب المستخدم وملفات المشروع. استنتج الخيارات القابلة للعكس، واسأل فقط عمّا يمنع التنفيذ. لا تفترض توفر محرر أو renderer أو حساب مدفوع. نفّذ داخل المشروع عندما تكون الأدوات متاحة، ثم افحص الناتج. لا تدّع تنفيذ رندر أو مشاهدة مرجع لم تنفذه أو تشاهده.

## خطوات العمل

1. استخدم Motion لحالات React وlayout وgestures، وGSAP للتتابع المعقد وSVG وscroll. لا تضف الأداتين دون سبب.
2. ابدأ transform وopacity. افحص تكلفة blur وfilters وlayout بدل افتراض أن أي animation يعمل على GPU.
3. عرّف حالات idle وenter وactive وexit والمقاطعة؛ عالج النقر المتكرر وتغيّر المسار وتنظيف listeners وtimelines.
4. احترم prefers-reduced-motion ووفّر وصولًا للمعلومة دون الحركة. لا تجعل scroll hijacking شرطًا لفهم الصفحة.
5. اختبر لوحة المفاتيح، الهاتف، تغيير حجم الشاشة، مغادرة المكون والعودة إليه. حدّد تراجعًا بسيطًا للأجهزة الضعيفة.

## المخرجات

مكون تفاعلي وحالاته، cleanup، نسخة reduced motion، تقرير معاينة.

## بوابة الجودة

لا listeners متراكمة؛ لا محتوى مخفي دائمًا؛ لا قفز layout؛ التفاعل يظل سريعًا.

## مثال طلب

> بطاقة منتج تتحول إلى تفاصيل مع دعم المقاطعة وتقليل الحركة.

## المراجع

- [gsap](../../references/sources.md#gsap)
- [motion](../../references/sources.md#motion)
