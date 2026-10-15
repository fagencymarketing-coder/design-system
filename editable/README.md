# Редактируемые макеты (PPTX)

`1plus1-layouts-editable.pptx` — 17 слайдов 1080×1080 (квадрат). Порядок: V1, V13, V2, V14, V3, V5, V6, V8, V9, V11, V12,
затем срочные новости U1–U6.

Как устроен слайд (слои снизу вверх): «Фон (картинка, без текста)» — фото, паттерн, водяной знак, плашка рубрики;
«Логотип» и «Фото / вырезка» (в V9 портрет) — отдельные картинки; «Малиновая черта» — фигура; тексты — обычные
текстовые поля Gilroy, перенос строк заданный вручную.

Шрифт: имена `Gilroy`, `Gilroy Medium`, `Gilroy SemiBold`, `Gilroy ExtraBold` (жирный `Gilroy` Bold). Должны быть
установлены на компьютере. Файлы шрифта лежат на Drive (папка fonts), в репозиторий не входят из-за лицензии.

Пересборка: `node tools/pptx/extract.js && python3 tools/pptx/build.py editable/1plus1-layouts-editable.pptx`
(нужны Playwright и python-pptx; список макетов — `tools/pptx/layouts.json`).
