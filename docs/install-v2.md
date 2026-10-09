# Установка v2 в проект Claude Design

Правила действуют постоянно, к чатам их прикреплять не нужно.

1. **`readme.md`**: заменить содержимое проекта на `docs/readme-v2.md` (целиком, не дописывать
   в конец: часть старых правил противоречит новым).
2. **`tokens/`**: добавить `tokens/v2.css`; старые `colors.css` и `typography.css` оставить,
   новые правила берут значения из `v2.css`.
3. **`assets/`**: загрузить
   - `logo.png`, `logo-full.png`, `logo-full-white.png`, `logo-mark-white.png`;
   - `pattern-2.png`, `badge-round.png` (`pattern-1.png` только для печати);
   - папку `assets/team/` (36 фото), её описание: `docs/team-photos.md`.
4. **Эталоны**: добавить `specimens/tax.png`, `tax-plain.png`, `law.png`, `law-olive.png`, `digits.png` как референсы
   качества (не как шаблоны для копирования).
5. **Проверка**: попросить Claude Design собрать новый пост по рецепту R1–R6 и прогнать его
   по чек-листу из раздела 14.

Устаревшее (в проекте можно оставить для истории): `design-system-rules.md`, `readme-patch.md`,
`install-pending.md`, `brandbook-1plus1.md`.
