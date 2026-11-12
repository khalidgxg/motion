---
name: remotion-production
description: Use when implementing frame deterministic React video compositions, previews, and renders with Remotion.
---

# إنتاج الفيديو بـ Remotion

حوّل اللوحات إلى فيديو برمجي يمكن إعادة رندره وتعديله.

## طريقة الاستخدام
اقرأ المدخلات والقيود من طلب المستخدم وملفات المشروع. استنتج الخيارات القابلة للعكس، واسأل فقط عمّا يمنع التنفيذ. لا تفترض توفر محرر أو renderer أو حساب مدفوع. نفّذ داخل المشروع عندما تكون الأدوات متاحة، ثم افحص الناتج. لا تدّع تنفيذ رندر أو مشاهدة مرجع لم تنفذه أو تشاهده.

## خطوات العمل

1. افحص package.json والـ lockfile والإصدار قبل كتابة API. استخدم scripts الموجودة وثبّت الحزم المتوافقة؛ لا تحدّث مشروعًا قائمًا عشوائيًا.
2. سجّل Composition بالدقة وfps وdurationInFrames، واجعل النصوص والألوان والأصول props واضحة.
3. اشتق كل حركة من useCurrentFrame وuseVideoConfig. استخدم interpolate مع clamp عند اللزوم وspring بإعدادات صريحة. اجعل Sequence والتوقيت المحلي مفهومين.
4. لا تعتمد على CSS animations أو Date.now أو Math.random غير المثبت أو صوت المتصفح في إخراج الفيديو. حمّل الخطوط والأصول قبل capture.
5. نفّذ typecheck، ثم stills لبداية ووسط ونهاية ومفاصل الانتقال، ثم عينة قصيرة ثم الرندر النهائي. افحص metadata والفيديو نفسه.

## المخرجات

Composition قابلة للتعديل، props، أمر تشغيل، صور تحقق، فيديو إن نجح الرندر.

## بوابة الجودة

تحديد إطار عشوائي يعطي الحالة الصحيحة؛ لا أصول مفقودة؛ مدة وفريمات ودقة صحيحة.

## مثال طلب

> نفّذ storyboard من 450 إطارًا مع RTL وخمسة مشاهد وprops للنص والألوان.

## المراجع

- [remotion](../../references/sources.md#remotion)
- [remotion-example](../../references/sources.md#remotion-example)
