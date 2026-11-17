# v12 (1.5.5): lists inside panels scroll on the phone again.
# The game blocked every touchmove on the page (so the 3D view never rubber-bands), which also froze
# the shop grid (FLIX / Iz / Insan / Hayvan / Tuy), and any other scrolling list. Now a touch that starts
# inside an element that can actually scroll is let through; everything else is still blocked.
# Applies to ../index.html in place and to game10.js (source); running twice changes nothing.
import os
D = os.path.dirname(os.path.abspath(__file__))
OLD = "document.addEventListener('touchmove', (e) => e.preventDefault(), {passive: false});"
NEW = ("document.addEventListener('touchmove', (e) => { for (let el = e.target; el && el !== document.body && el.nodeType === 1; el = el.parentElement) { "
       "const cs = getComputedStyle(el); if ((/(auto|scroll)/.test(cs.overflowY) && el.scrollHeight > el.clientHeight + 1) || (/(auto|scroll)/.test(cs.overflowX) && el.scrollWidth > el.clientWidth + 1)) return; } "
       "e.preventDefault(); }, {passive: false});")
for f in [os.path.join(D, '..', 'index.html'), os.path.join(D, 'game10.js')]:
    s = open(f, encoding='utf-8').read()
    if NEW in s: print('already', f); continue
    assert s.count(OLD) == 1, f
    open(f, 'w', encoding='utf-8').write(s.replace(OLD, NEW)); print('patched', f)
