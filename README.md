# مكتبة مهارات الموشن جرافيك

مكتبة عربية لتوجيه Claude في تخطيط الموشن جرافيك وتصميمه وتنفيذه ومراجعته. تضم مهارات إنتاجية ووصفات إبداعية أصلية ومراجع تقنية من أصحاب الأدوات. هذه المهارات تعليمات عمل؛ لا تثبّت برامج الرندر ولا تُنتج فيديو بمجرد نسخها.

## الاستخدام مع Claude

- ابدأ بمهارة [motion-director](skills/motion-director/SKILL.md) للمشروع الكامل، أو اختر تخصصًا من الفهرس.
- للاستخدام اليدوي: أرفق `SKILL.md` المطلوب والملفات المرجعية المرتبطة به، ثم اذكر المخرجات والمدة والأبعاد والأصول المتاحة.
- في نظام يدعم Agent Skills: أضف مجلد المهارة وفق آلية النظام. يحتوي كل مجلد على frontmatter باسم ووصف. يُراجع مسار الاكتشاف في إصدار Claude المستخدم؛ وجودها داخل هذا المستودع لا يعني تثبيتها تلقائيًا.
- لتجهيز مجلدات مستقلة أو ZIP ارفعها حيث تدعم الواجهة ذلك: شغّل `python3 scripts/package_skills.py --output /tmp/motion-skills`؛ تُضمّن المراجع داخل كل مهارة مع تحديث روابطها.
- لا يوجد اعتماد على نموذج أو API محدد. لم يمكن تأكيد تسمية «Opus 5.5» من المصدر الرسمي بسبب حجب الوصول؛ اختر النموذج المتاح في حسابك ولا تستخدم model ID مفترضًا.

## إنشاء فيديو بـ Remotion

ابدأ بـ [إخراج المشروع](skills/motion-director/SKILL.md) لاتخاذ قرارات تصميم الحركة، ثم افتح [مهارة إنتاج الفيديو](skills/remotion-production/SKILL.md). ستوجّه Claude إلى [حزمة Remotion الرسمية المحلية](skills/remotion-production/remotion-agent-skills/remotion-best-practices/SKILL.md) لإنشاء المشروع والتحريك والمعاينة في Studio والتصدير عند طلبه. تُقرأ ملفات المهارات من المستودع، ويحتاج التنفيذ إلى حزم Remotion في مشروع الفيديو.

تضم النسخة المحلية مجلدات المهارات الرسمية الثلاثة عشر من [`remotion-dev/skills` عند الالتزام `6f55706`](https://github.com/remotion-dev/skills/tree/6f55706d1069e512430582ad86e4e57dc07afe1b/skills) بما فيها المراجع والأمثلة والأصول المرافقة.

## الفهرس

| المهارة | الاسم |
| --- | --- |
| [إخراج المشروع](skills/motion-director/SKILL.md) | `motion-director` |
| [الهوية والإبداع البصري](skills/visual-direction/SKILL.md) | `visual-direction` |
| [السيناريو واللوحات](skills/storyboard-animatic/SKILL.md) | `storyboard-animatic` |
| [الإيقاع ومنحنيات الحركة](skills/timing-easing/SKILL.md) | `timing-easing` |
| [الطباعة العربية المتحركة](skills/arabic-kinetic-type/SKILL.md) | `arabic-kinetic-type` |
| [الانتقالات والربط](skills/transitions-matchcuts/SKILL.md) | `transitions-matchcuts` |
| [إعلانات المنتجات والتطبيقات](skills/product-promo/SKILL.md) | `product-promo` |
| [تحريك الشعارات والهوية](skills/logo-brand-motion/SKILL.md) | `logo-brand-motion` |
| [البيانات والإنفوجرافيك](skills/data-storytelling/SKILL.md) | `data-storytelling` |
| [مشاهد ثلاثية الأبعاد](skills/three-dimensional/SKILL.md) | `three-dimensional` |
| [الصوت والمزامنة](skills/sound-design/SKILL.md) | `sound-design` |
| [إنتاج الفيديو بـ Remotion](skills/remotion-production/SKILL.md) | `remotion-production` |
| [حركة الويب والتفاعل](skills/web-motion/SKILL.md) | `web-motion` |
| [تسليم SVG وLottie](skills/lottie-delivery/SKILL.md) | `lottie-delivery` |
| [الرندر وفحص الجودة](skills/render-quality/SKILL.md) | `render-quality` |
| [البحث وانتقاء المراجع](skills/reference-curation/SKILL.md) | `reference-curation` |

## ابدأ بمثال

> استخدم motion-director ثم arabic-kinetic-type وremotion-production لإعلان عربي عمودي 15 ثانية عن تطبيق ميزانية. ابدأ بثلاث معالجات، ثم storyboard ومواصفات styleframes وتوقيت 450 إطارًا. نفّذ إذا توافرت الأدوات، وافصل ما رُندر فعلًا عما لم يُرندر.

- [معالجات إبداعية منتقاة](references/creative-recipes.md)
- [المصادر وحالة التحقق](references/sources.md)
- [نموذج التكليف](templates/brief.md)
- [نموذج اللوحات](templates/storyboard.md)
- [تقرير الجودة](templates/qa-report.md)
- [مثال إعلان عربي مكتمل التخطيط](examples/arabic-budget-promo.md)

## الاختيارات التقنية

| المخرج | الأداة المرشحة | سبب الاختيار |
| --- | --- | --- |
| فيديو برمجي | Remotion | React وتوقيت مرتبط بالإطارات |
| تفاعل React | Motion | حالات وgestures وlayout |
| تتابع ويب وSVG | GSAP | timelines وتحكم تفصيلي |
| أيقونات متجهة | Lottie | ملف حركة قابل للتشغيل ضمن دعم المنصة |
| مشاهد 3D برمجية | Three.js | كاميرا وخامات وهندسة |
| فحص وتحويل ملفات | FFmpeg/ffprobe | معالجة وسائط وقراءة metadata |

الاختيار تحريري حسب المهمة، وليس ترتيبًا للأجمل أو الأكثر استخدامًا. راجع ترخيص كل أداة وأصل وقت الاستخدام. تتضمن المكتبة حزمة مهارات Remotion الرسمية ضمن مسار إنتاج الفيديو.

## التحقق والتوسعة

شغّل `python3 scripts/validate_library.py` للتحقق من أسماء المهارات والروابط والقوالب. لا يثبت هذا الفحص جودة فيديو أو نجاح الرندر أو سلوك Claude. أضف المهارات إلى `catalog.json` واربط كل ادعاء خارجي بمصدر وحالة وصول، ثم اختبر المهارة بمهمة فعلية قبل وصفها بأنها مجرّبة إنتاجيًا.
