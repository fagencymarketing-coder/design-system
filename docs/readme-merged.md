# 1+1 Design System

**1+1** (1-plus-1.ru) — аутсорсинг бухгалтерии для малого и среднего бизнеса (outsourced accounting for small and medium businesses), based in Russia. Services include: accounting outsourcing, financial & tax consulting, legal support, management accounting, and a free tax calculator tool. The company positions itself around peace of mind, reliability, and expertise — "Ваше спокойствие" (Your peace of mind).

**Website:** https://1-plus-1.ru/  
**Phone:** 8 (800) 600-56-86  
**Email:** info@1-plus-1.ru

---

## Sources

This design system was built from the following provided materials:

- **Figma file:** "1+1 финал.fig" — mounted as virtual filesystem; contains the hero landing page design, color swatches, icon components (Call, Chart, Mail, Secure, Verified), and typography specimens
- **Figma file:** "Дизайн 1+1.fig" — extended design context
- **Figma file:** "Дизайн 1+11.fig" — additional design variants
- **Figma file:** "Фир стиль 1+1.fig" — brand/visual style reference
- **Branding folder:** `Брендбук/` — CorelDRAW source files + PDF exports of logo, blank, pattern, and icon sets
- **Design system folder:** `Дизайн система/` — screenshots of key pages, slides, and design references
- **Brand style folder:** `Фирменный стиль/` — logo PNG exports
- **Font files:** Gilroy family (all weights: Thin–Black + Italic variants), uploaded directly

---

## CONTENT FUNDAMENTALS

### Voice & Tone
- **Direct and confident.** The brand speaks plainly — no jargon, no fluff. Sentences are short.
- **Client-first.** Always framed around benefit to the client: "ваше спокойствие", "ваша уверенность". The company is the means, the client's peace of mind is the end.
- **We ("мы"), not "I".** The brand speaks as a team: "мы работаем", "наши клиенты".
- **Warm professionalism.** Not dry/corporate, not casual/friendly — a trusted expert friend tone.
- **Factual proof points.** Claims are always backed by numbers: "15 лет без штрафов", "страхование на 10 млн руб", "более 450 компаний".

**Правило генерации текста (строгое)**
Используй в макете только тот текст, который явно предоставлен пользователем в запросе. Это касается ВСЕХ текстовых элементов без исключения: заголовков, подзаголовков, бейджей, тегов, лейблов, категорий, подписей к фото, кнопок, футера — не только основного текста.

- Не добавляй бейджи/теги/категории (например, "Наши эксперты", "Команда", "Новость"), если пользователь их не указал явно.
- Если по смыслу макета такой элемент кажется уместным (например, бейдж-категория для карточки блога) — не добавляй его сам, а спроси пользователя, нужен ли он и что в нём написать.
- Разрешено использовать без явного запроса пользователя только: элементы из брендбука, которые являются частью фирменного стиля и повторяются на всех макетах без исключения (логотип, слоган компании) — потому что это не контент, а фиксированный брендинг.
- Контакты и домен сайта фиксированным брендингом не являются — это контент. Они добавляются только в макетах, где форматом предусмотрен футер или контактный блок: лендинг, презентация, бланк, визитка, коммерческое предложение. В постах для соцсетей, обложках и отдельных карточках домен и контакты без явного запроса не добавляются.
- Всё остальное — включая декоративные короткие лейблы — требует явного текста от пользователя или явного вопроса перед добавлением.
- **Про компонент Badge**: наличие компонента Badge в библиотеке — не разрешение использовать его по умолчанию. Badge применим только если у него есть явный текст от пользователя. Не добавляй Badge с придуманным текстом категории (например, "Команда 1+1", "Наши эксперты", "Новость", "Кейс") просто потому, что он есть в дизайн-системе и "обычно так делают" на карточках такого типа.
- **Самопроверка перед выдачей результата**: перед тем как показать финальный макет, сверь список всех текстовых элементов на нём со списком того, что явно предоставил пользователь. Если на макете есть текстовый элемент (включая бейдж/тег/лейбл), которого нет в исходном запросе и который не является фиксированным элементом брендинга (логотип, слоган компании) — удали его перед выдачей результата, а не оставляй как "полезное дополнение".
- Если нужного текста нет и пользователь ещё не ответил на вопрос — используй короткий нейтральный плейсхолдер в квадратных скобках, например `[Заголовок]`, `[Описание услуги]`, а не сочиняй правдоподобный текст.
- Никогда не выдумывай факты, цифры, статистику или условия (сроки, суммы страхования, количество клиентов и т.п.) — используй только те, что явно даны.
- При редактировании существующего компонента/страницы не меняй и не "улучшай" копирайтинг, если это не было запрошено — трогай только layout, стили и структуру, если не указано иное.

### Casing
- **Russian standard sentence case** for all headings and body. No ALL CAPS except in the logo mark.
- Highlighted words (inside a crimson pill/badge) may have emphasis but still use sentence case.

### Punctuation
- Em-dashes (—) used for emphasis mid-sentence: "Основа компании — наши ценности"
- No serial commas (Russian punctuation rules)
- Exclamation marks used sparingly — only for emotional payoff lines

**Правила переноса строк**

Следующие сочетания связываются неразрывным пробелом и никогда не разделяются
переносом строки:

- односложные предлоги и союзы — в, с, к, о, у, на, по, из, за, до, и, а, но —
  не остаются в конце строки, а переносятся вместе со следующим словом
- число и его единица измерения: «500 тысяч», «10 млн рублей», «15 лет», «40 px»
- число и следующее за ним слово в датах: «1 октября», «2026 года»
- инициалы и фамилия, сокращения вида «г. Барнаул», «ул. Пролетарская»

Акцентное выделение цветом не разрывается переносом: фраза под акцентом либо
умещается в строку целиком, либо сокращается, либо перестраивается вёрстка.

### Emoji
- **Never used.** The brand is professional and minimal. No emoji anywhere.

### Copy examples
- "Бухгалтерский аутсорсинг с 1+1" — hero headline
- "Это время, деньги и уверенность наших клиентов — а не просто бухгалтерия" — subheadline
- "Бесплатный экспресс-аудит при заключении договора" — offer callout

---

## VISUAL FOUNDATIONS

### Colors
Five-color palette, used with intention:

| Token | Hex | Role |
|---|---|---|
| `--color-crimson` | `#D73A61` | Primary CTA, active labels, highlights |
| `--color-olive` | `#ABAD58` | Secondary brand, slide bg, decorative |
| `--color-ink` | `#1B1B1B` | Primary text, dark buttons, nav bg |
| `--color-cream` | `#F2F3ED` | Main panel/section bg |
| `--color-cloud` | `#F9F9F9` | Page bg |
| White | `#FFFFFF` | Cards, overlays |

### Typography
- **Gilroy** is the sole typeface, all weights available (Thin 100 → Black 950).
- Display text (desktop): 120px, Semibold (600), letter-spacing -0.05em, line-height 0.9 — extremely tight and editorial.
- Subheadings (desktop): 28px, Medium (500), letter-spacing -0.03em.
- Body: 18px, Regular (400), line-height 1.4.
- UI labels/buttons: 16–20px, Semibold, letter-spacing -0.02em.
- No serif, no mono, no system font fallback intentionally used in brand contexts.

**Responsive type scale** — the desktop sizes above are not fixed; scale them down at narrower breakpoints rather than guessing:

| Role | Desktop (≥1200px) | Tablet (768–1199px) | Mobile (<768px) |
|---|---|---|---|
| Display | 120px | 72–88px | 40–56px |
| H1 | 72px | 48–56px | 32–36px |
| Subheading | 28px | 22–24px | 18–20px |
| Body | 18px | 17px | 16px |

Keep letter-spacing and line-height ratios the same across breakpoints; only the size scales down.

**Contrast rule** — crimson (`#D73A61`) on cream (`#F2F3ED`) and olive (`#ABAD58`) on white do not reliably pass WCAG AA for body text. Reserve these combinations for large display type (≥24px bold or ≥32px regular), decorative accents, and non-text elements (badges, dots, rules). For body copy and small UI text, always use `--color-text-primary` (ink) on light surfaces, or white on ink/olive-dark surfaces.

### Backgrounds
- **Cream panels** (`#F2F3ED`) are the primary content containers — large, card-like rounded panels (radius 20–26px) on a lighter cloud grey page.
- **Olive green slides** (`#ABAD58`) used for full-bleed presentation/service slides — strong, editorial.
- **Dark ink** (`#1B1B1B`) used for the nav bar button and footer — minimal dark presence.
- **Gradients are restricted to one place**: the decorative circular gradient (white → olive) in the hero background only. Do not reuse a gradient treatment in any other section (cards, banners, buttons, footers) — those stay flat.
- No textures or noise effects.

### Pattern
A distinctive **repeating pattern** made from tiled "1+1" logo marks in alternating crimson and olive, used on branded materials (envelopes, backgrounds, brand stationery). Never used as a UI element directly — reserved for brand/print contexts.

### Cards
- White (`#FFFFFF`) background, radius 10px for small/inline cards, 20px for section panels.
- No drop shadow on large panels; subtle shadow (`--shadow-md`) on floating cards — see Shadows below for the token scale.
- No colored left-border accent (this is an anti-pattern for this brand).

### Corner Radii
- Buttons: 6–8px (compact, not pill-shaped)
- Cards/panels: 10–20px
- Large sections: 20–26px
- Decorative circles: 50% (full)

### Borders
- Very minimal use. Thin `1px` separators in olive/grey as dividers between list items.
- No heavy card outlines or box borders.

### Shadows
- Used sparingly, on floating cards only — large panels stay flat (no shadow).
- Scale: `--shadow-sm` (small inline cards or none), `--shadow-md` (floating cards, default), `--shadow-lg`/`--shadow-xl` (modals, popovers). The brand prefers clean flat surfaces over heavy elevation.

### Hover / Press states
- **Buttons**: darken background color (crimson → `#C42E53`, ink → `#2E2E2E`). No opacity tricks.
- **Links/nav items**: opacity reduction to ~0.6 or color shift.
- **Cards**: subtle shadow increase on hover.

### Animations
- Minimal. No bounces, no elaborate transitions.
- Simple `opacity` + slight `translateY` fades for content appearing.
- Transition speed: 120–200ms ease. Nothing flashy.

### Imagery
- Professional photography — team photos, people at work. Warm, approachable.
- Images are always cropped generously, usually right-aligned in hero sections.
- No illustrations or hand-drawn elements.
- Color treatment: natural, warm.

Это описание относится к фотографиям самой компании. Требования к тематическим
фотографиям — см. Photo source rule.

**Photo source rule**
Фотографии берутся из двух источников, выбор зависит от того, о чём блок.

**Реальные фото компании** — `assets/photos/`. Обязательны везде, где макет
говорит о самой компании: команда, эксперты, офис, отзывы, кейсы конкретных
клиентов, контакты, hero-секция сайта. Подставлять сток в такие блоки запрещено —
это вводит аудиторию в заблуждение относительно реальной команды.

**Тематические фотографии** — разрешены в блоках, иллюстрирующих тему,
а не компанию: посты о налогах, проверках, сроках, изменениях в законодательстве,
обложки статей, тематические карточки.

Тематическое фото допускается только при выполнении всех условий:

- **По смыслу.** Показывает рабочую ситуацию: документы, расчёты, встреча, офис,
  разговор с клиентом. Запрещены клише: рукопожатия на фоне небоскрёбов, люди
  в костюмах с папками, растущие столбики монет, песочные часы, лупа над бумагами.
- **По цвету.** Допустимые доминирующие цвета: кремовый, белый, бежевый, серый,
  тёплое дерево, живая зелень, приглушённый оливковый. Запрещены как доминанта:
  синий, голубой, бирюзовый, фиолетовый, неоновые и кислотные цвета. Осторожно
  с чистым красным и оранжевым: спорят с crimson `#D73A61`.
- **По обработке.** Насыщенность приглушена, баланс белого сдвинут в тёплую
  сторону — в тон существующим фото бренда. Фотография без приведения к общему
  виду не используется.
- **По качеству.** См. Photo quality rule.

Если по смыслу блока фотография не требуется — не добавляй её принудительно.

Если подходящего кадра нет — оставь плейсхолдер `[Фото: описание, что должно быть
на фото]` и сообщи, что нужно добавить фотографию.

**Photo quality rule**
Требования к качеству распространяются на все фотографии в макете — и на реальные
фото компании из `assets/photos/`, и на тематические.

Если единственное подходящее по смыслу фото — низкого качества (маленькое разрешение, размытое, сильно сжатое) — не используй его через силу. Вместо этого либо выбери другое фото того же смысла из `assets/photos/` или `assets/stock/`, либо, если альтернативы нет, оставь плейсхолдер `[Фото: описание]` и сообщи пользователю, что нужно фото лучшего качества для этого места.

**AI-generated imagery rule**
AI-генерируемые изображения разрешены только если они фотореалистичны и стилистически неотличимы от настоящей профессиональной фотографии бренда: естественное освещение, реалистичные материалы и текстуры, нейтральный/светлый фон (как в существующих brand-фото), тёплая, естественная цветокоррекция — без художественной стилизации.

Разрешено: предметная/натюрмортная съёмка объектов, иллюстрирующих тему поста (например: молоток судьи и книга законов — тема права; тарелка с чеком — тема НДС/чеков). Такие изображения должны выглядеть как реальная студийная/предметная фотосъёмка.

Запрещено:
- Стилизованные иллюстрации, 3D-рендеры, "художественные" или фэнтезийные образы (пример: золотая статуя Фемиды с нереалистичным освещением и стилизацией) — это остаётся нарушением правила "No illustrations or hand-drawn elements".
- Изображения людей, сгенерированные AI, допустимы, если они фотореалистичны и генеричны (иллюстрируют абстрактную ситуацию или роль — например, "предприниматель за столом с документами", "клиент общепита"), но не представлены как реальные сотрудники или клиенты компании 1+1.
- Если контекст макета подразумевает именно команду/сотрудников/клиентов 1+1 (например, "наши эксперты", "команда 1+1", отзывы, кейсы конкретных клиентов) — используются только настоящие фото из assets/photos/ (см. Photo source rule), AI-люди в таком контексте не допускаются, так как это ввело бы аудиторию в заблуждение относительно реальной команды.
- Любые изображения, где стиль, освещение или композиция визуально выделяются на фоне остального макета как "AI-картинка" — если результат выглядит неестественно, нужно перегенерировать. Если и после этого результат неудовлетворителен — поставить плейсхолдер `[Фото: описание]` и сообщить об этом; молча переходить к типографической композиции нельзя (см. «Когда макет с изображением, когда без»).

Перед тем как генерировать изображение с нуля, всё равно сначала проверь Reuse existing graphic elements rule — возможно, подходящий предметный элемент уже есть в загруженных материалах.

**Reuse existing graphic elements rule**
Перед тем как оставлять пустое пространство в макете или генерировать новый
визуальный элемент, проверь, есть ли подходящий по смыслу графический элемент
среди исходников дизайн-системы.

Исходники делятся на две группы, смешивать их нельзя:

- **Можно вставлять в макет:** элементы брендбука и фирменного стиля —
  декоративные фигуры, паттерны, иконки, графические формы из Figma-файлов
  и брендбука. Это подготовленная графика.
- **Только для понимания стиля, вставлять запрещено:** скриншоты в папке
  «Дизайн система», готовые макеты и их фрагменты, презентационные слайды,
  референсы. Из них берутся приёмы композиции, но не пиксели.

Элемент из первой группы вставляется, только если выполнены оба условия:

- он вырезан — прозрачный фон, без прямоугольной подложки
- он выдержан в фирменной палитре: crimson, olive, ink, cream, cloud, белый

Если элемент подходит по смыслу, но не проходит по этим условиям — он
не используется. Не подкладывай под него плашку, чтобы скрыть фон.

Если непонятно, к какой группе относится файл, — считай его референсом
и не вставляй.

**Image cutout rule**
Изображение — фотография, графический элемент, иллюстрация — вставляется так,
чтобы оно не приносило с собой собственный фон.

Запрещено:

- белая или цветная плашка, карточка, рамка, подложенная под изображение, чтобы
  скрыть его фон
- изображение с собственным прямоугольным фоном, отличающимся от фона макета
- тени и скругления, имитирующие карточку под картинкой

Фотографии кадрируются в предусмотренную макетом форму — скруглённый прямоугольник,
круг или фигуру — и ложатся на фон макета либо на фирменную подложку по правилам
layout. Графические элементы и иконки вставляются только с прозрачным фоном.

Если изображение нельзя вставить без собственного фона — оно не используется.

Правило не отменяет компонент Card. Карточка со скруглением и тенью — легитимный
элемент макета, если она содержит текст или несколько элементов. Запрещена именно
подложка, добавленная под изображение с единственной целью скрыть его собственный
фон.

**Logo version rule**
Файлы логотипа в `assets/`:

- `logo.png` — только знак «1+1», цветной
- `logo-alt.png` — знак на кремовой плашке
- `logo-full.png` — знак и дескриптор «АУТСОРСИНГ БУХГАЛТЕРИИ», цветной
- `logo-full-white.png` — знак и дескриптор, белый
- `logo-mark-white.png` — только знак, белый

**Выбор по фону:**

- Светлый фон — cloud `#F9F9F9`, cream `#F2F3ED`, белый, светлая фотография →
  цветная версия
- Тёмный и насыщенный фон — ink `#1B1B1B`, olive `#ABAD58`, crimson `#D73A61`,
  тёмная фотография → белая версия
- Цветной логотип на оливковом и малиновом запрещён: знак состоит из этих же
  цветов и сливается с фоном

`logo-alt.png` используется только на фоне cream `#F2F3ED`, где плашка совпадает
с фоном. На любом другом фоне запрещён: подложка станет видимой и нарушит
Image cutout rule.

**Выбор полной версии или знака:**

В постах для соцсетей, обложках, рекламных макетах и любых самостоятельных
материалах используется полная версия с дескриптором. Только знак допускается
в двух случаях: на внутренних слайдах презентации или карусели, где полная версия
уже стоит на первом слайде, и когда высота логотипа меньше 40 px.

Логотип вставляется файлом. Запрещено воспроизводить его шрифтом, набирать «1+1»
текстом или воссоздавать фигуры кодом.

Вокруг логотипа свободное поле не меньше ширины цифры «1» из знака.

### Icons
- 5 brand icons: **Call, Chart, Mail, Secure, Verified** — solid fill, monochromatic (painted with `currentColor`).
- Used at 18–24px in nav/inline contexts. Tinted crimson for emphasis.
- No icon font; SVG-based. See `components/icons/`.
- **Closed set.** This is the complete icon list — do not invent new icons and do not pull in third-party icon libraries (Lucide, Heroicons, emoji, etc.). If a design calls for an icon outside this set, ask the user, or pick the closest match from the existing five instead of improvising one.

### Layout
- Max container: 1856px, padding: 32px per side (from Figma).
- Nav height: 72px. Nav uses cream background, same as panels.
- Generous vertical spacing — 80px+ between sections.
- 3-column grid for feature lists (values, services) on desktop.

**Breakpoints**
- Desktop: ≥1200px — full max-width container, 32px side padding, 3-column grids.
- Tablet: 768–1199px — side padding 24px, 3-column grids collapse to 2 columns.
- Mobile: <768px — side padding 16–20px, all grids collapse to 1 column, nav height 56–64px.

**Typography-only card rule**

**Когда макет с изображением, когда без**

По умолчанию макет собирается с изображением. Типографическая композиция без
изображения — осознанный приём для случаев, когда сила в самой формулировке
или цифре: короткая цитата, крупное число, анонс из одной фразы.

Отсутствие подходящего изображения не является основанием для типографического
макета. Если изображение по смыслу уместно, но подходящего нет — оставь
плейсхолдер `[Фото: описание]` и сообщи об этом. Молча переключаться на текстовую
композицию нельзя.

Источники изображения по приоритету: реальные фото компании из `assets/photos/` →
библиотека тематических фотографий → фотореалистичная предметная съёмка
по AI-generated imagery rule → плейсхолдер.

**Композиция типографического макета**

Заголовок и остальные уровни вертикально центрируются по всей высоте холста.

Размер текста увеличивается так, чтобы текстовый блок занимал не менее 45% высоты
холста. Это обязательное требование, а не возможность.

Текстовый блок занимает не менее 80% ширины холста. Строки заполняются по ширине
блока: перенос делается только тогда, когда следующее слово не помещается,
а не для того, чтобы придать тексту форму столбика.

Каждая строка заголовка, кроме последней, содержит не менее 15 знаков. Строка
короче означает, что кегль завышен относительно ширины блока: расширь блок
до 80–90% ширины холста, а если этого мало — уменьши кегль. Требование относится
ко всем уровням иерархии: подзаголовок и обычный текст не разбиваются на несколько
строк, если умещаются в одну.

Заголовок длиной до 60 знаков не занимает больше трёх строк, но и три строки
по 9–10 знаков считаются нарушением — решает заполненность строки, а не их число.

**Проверка перед выдачей** ведётся по обеим осям сразу: высота текстового блока
45–60% холста, ширина не менее 80%. Выполнение одного требования за счёт другого
считается невыполнением правила.

Логотип остаётся в фиксированной позиции согласно общим правилам layout.

**Типографическая иерархия**

Предоставленный текст может набираться несколькими кеглями, если это улучшает
композицию. Слова при этом не добавляются, не удаляются и не переписываются —
меняется только размер и расположение.

Уровни, из типографической шкалы системы:

- **Заголовок** — главное утверждение, самый крупный кегль
- **Подзаголовок** — уточнение: условие, срок, сумма, оговорка. 40–60% кегля
  заголовка
- **Обычный текст** — пояснение
- **Мелкий текст** — сноска, источник, дисклеймер

**Как разбивать.** Если предоставленная фраза содержит главное утверждение
и уточнение к нему, уточнение набирается меньшим кеглем отдельной строкой.

Если пользователь передал текст уже размеченным по ролям — использовать его
разметку и не переопределять её.

**Акцент цветом** ставится только на одном уровне иерархии, обычно на ключевой
цифре или на подзаголовке. Не выделять цветом одновременно заголовок
и подзаголовок.

**Пунктуация на стыке уровней.** Если фраза разбивается на уровни по знаку-
разделителю — двоеточие, тире, точка с запятой, — сам разделитель убирается: его
роль выполняет вёрстка. Это единственное допустимое изменение предоставленного
текста. Всё остальное неприкосновенно: слова, числа, падежи, знаки внутри уровней.

**Связность блока.** Уровни иерархии образуют единый текстовый блок. Расстояние
между соседними уровнями не превышает полутора межстрочных расстояний заголовка.
Разносить уровни по разным зонам холста с крупными пустотами между ними запрещено.
Свободное пространство собирается по краям композиции, а не между её частями.

**Схемы макетов с изображением**

Размеры даны для квадрата 1080×1080 и пересчитываются пропорционально для других
форматов. Схема выбирается по типу изображения, а не по вкусу.

**Схема A — объект без фона.** Для вырезанной предметной съёмки и графических
элементов. Объект занимает 40–55% площади холста, обычно правую часть или нижний
правый угол. Текст — в свободной зоне слева или сверху. Фон холста: cream
`#F2F3ED` или olive `#ABAD58`. Подложек под объект нет.

**Схема B — изображение верхней частью.** Для сцен, рабочих ситуаций, интерьеров.
Изображение занимает верхние 50–60% холста на всю ширину, нижние углы скруглены
на 24px либо край прямой. Текст — в нижней части на фоне холста, поля 90px.
Логотип ставится в текстовой зоне в цветной версии.

**Схема C — изображение фоном.** Для атмосферных кадров, когда текста мало.
Изображение на весь холст, поверх — затемнение: заливка ink `#1B1B1B`
с прозрачностью 40–55% либо градиент от низа. Текст и логотип белые. Белый текст
на неприкрытом светлом участке фотографии запрещён.

**Схема D — изображение в круге.** Для портретов и фото сотрудников. Круг
диаметром 55–65% ширины холста, на фирменной подложке — оливковой или кремовой.
Текст рядом или под кругом. Фирменный приём, используется на сайте.

**Общие требования ко всем схемам:**

- Текстовый блок сохраняет иерархию, заполненность строк и связность. Требование
  высоты 45–60% относится только к типографическим макетам без изображения —
  в макетах с картинкой текст занимает столько, сколько отводит схема
- Поля холста не меньше 90px со всех сторон
- Изображение и текст не накладываются друг на друга, кроме схемы C, где наложение
  предусмотрено и компенсировано затемнением
- Логотип не заходит на изображение, если под ним нет затемнения или ровной
  однотонной области

**Aspect ratio rule**
Если пользователь явно указывает формат макета (квадрат, сторис, альбомная ориентация, конкретные размеры в px), итоговый холст должен точно соответствовать этому соотношению сторон:
- Квадрат — 1:1 (например, 1080×1080px)
- Сторис/reels — 9:16 (1080×1920px)
- Пост в ленту (портрет) — 4:5 (1080×1350px)

Если формат не указан явно — по умолчанию использовать 1:1 для постов в соцсети, если из контекста не следует другое. Не подгонять контент под "удобную" высоту без учёта заданного соотношения сторон.

---

## ICONOGRAPHY

### Approach
1+1 uses a small, custom SVG icon set (5 icons) materialized from the Figma file. Icons are solid/filled, single-color, rendered with `currentColor`.

### Icon set (`components/icons/icon-data.js`)
- **Call** — phone handset
- **Chart** — bar chart / analytics
- **Mail** — envelope
- **Secure** — shield / lock
- **Verified** — checkmark / verified badge

### Usage
```jsx
import { Icon } from "./components/icons/Icon.jsx";

<Icon name="Call" size={18} style={{ color: "var(--color-crimson)" }} />
<Icon name="Verified" size={24} />
```

No emoji used as icons. No third-party icon font. CDN icon libraries (Lucide, etc.) are not part of the brand.

---

## FILE INDEX

```
styles.css                    ← Global CSS entry point (@import list)
readme.md                     ← This file

tokens/
  fonts.css                   ← @font-face rules for Gilroy (all weights)
  colors.css                  ← Color custom properties
  typography.css              ← Type scale, weights, roles
  spacing.css                 ← Spacing, radius, shadow, layout tokens

assets/
  fonts/                      ← Gilroy TTF files (Regular–Black + Italics)
  logo.png                    ← Знак «1+1», цветной, прозрачный фон
  logo-alt.png                ← Знак на кремовой плашке (только для фона cream)
  logo-full.png               ← Знак и дескриптор, цветной, прозрачный фон
  logo-full-white.png         ← Знак и дескриптор, белый, прозрачный фон
  logo-mark-white.png         ← Знак без дескриптора, белый, прозрачный фон
  pattern1.jpg                ← Repeating 1+1 logo pattern (crimson rows)
  pattern2.jpg                ← Repeating 1+1 logo pattern (mixed)
  hero-person.png             ← Hero section photo
  brand-group.png             ← Brand group reference
  slide1.png … slide5.png     ← Reference slides
  frame-26.png etc.           ← Design reference frames
  photos/                     ← Реальные фото сотрудников и офиса
  stock/                      ← Тематические фотографии, отдельно от photos/

components/
  icons/
    icon-data.js              ← SVG path data for all 5 brand icons
    Icon.jsx                  ← <Icon name="…" size={…} /> component
    Icon.d.ts                 ← TypeScript types
  core/
    Button.jsx + .d.ts        ← Primary, secondary, ghost, sizes
    Card.jsx + .d.ts          ← Content card
    Badge.jsx + .d.ts         ← Status badge / tag
    Input.jsx + .d.ts         ← Text input
    Divider.jsx + .d.ts       ← Section divider

guidelines/
  colors.card.html            ← Color swatches specimen
  type-display.card.html      ← Display / heading type
  type-body.card.html         ← Body / UI type
  type-weights.card.html      ← Weight specimen
  spacing.card.html           ← Spacing scale
  brand.card.html             ← Logo + pattern
  icons.card.html             ← Icon set

ui_kits/
  website/
    index.html                ← Website UI kit (hero, nav, services, CTA)

templates/
  pitch-deck/
    PitchDeck.dc.html         ← Presentation slide template
```

---

## COMPONENTS

### Button
Primary (crimson), secondary (ink dark), ghost (outline). Sizes: sm / md / lg.  
See `components/core/Button.jsx`.

### Card
White content card with optional header and footer.  
See `components/core/Card.jsx`.

### Badge
Small label/tag in brand colors — crimson, olive, ink, muted.  
See `components/core/Badge.jsx`.

### Input
Text input with label and optional helper text.  
See `components/core/Input.jsx`.

---

## UI KITS

- **Website** (`ui_kits/website/index.html`) — Hero landing page with nav, hero section, values grid, service CTA banner, and footer. Interactive.

---

## TEMPLATES

- **Pitch Deck** (`templates/pitch-deck/PitchDeck.dc.html`) — Presentation slide template in 1+1 brand style.

