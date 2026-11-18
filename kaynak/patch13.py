# v13 (1.5.6): QA fixes.
# 1. Settings showed the old version "Flix Atış 1.2": now 1.5.6 (also in the Legal/About panel footer).
# 2. Settings fits small phones (320x568, 375x667, 390x844 with notch): title no longer cut at the top,
#    TAMAM no longer covers the last rows / version; rows get compact on short screens and the list
#    scrolls (never under TAMAM) if it still does not fit. BÖLÜMLER title smaller on 320 px wide screens.
# 3. Interstitial: first one after the 3rd finished level, then every 3rd (it used to be the level
#    index cur < 3 AND adN % 3, so the first one only came after level 6). 90 s after a rewarded ad,
#    No Ads and ?bot=1 still block it.
# 4. window.__A (test/cheat hooks: win, lose, addFe, grant...) only on the web build or with ?bot=1,
#    never in the iOS app. window.__atisGrant stays: native-bridge.js delivers App Store purchases through it.
# Applies to ../index.html, game10.js (JS) and shell7.html (HTML/CSS) in place; running twice changes nothing.
# Then: cd ../app && python3 tools/build_www.py
import os
D = os.path.dirname(os.path.abspath(__file__))
VER = '1.5.6'
CSS = ('#setClose{right:18px;bottom:calc(var(--sab) + 26px);width:112px;height:112px}'
       '#setS{justify-content:flex-start;overflow-y:auto;-webkit-overflow-scrolling:touch;padding:calc(var(--sat) + 14px) 14px calc(var(--sab) + 150px)}'
       '#setS>:first-child{margin-top:auto}#setS>:last-child{margin-bottom:auto}'
       '#setS .srow{width:100%;max-width:280px;gap:12px;flex:none;text-align:left}#setS .srow span:last-child{flex:none;white-space:nowrap}'
       '@media (max-height:860px){#setS{padding-bottom:calc(var(--sab) + 124px)}#setS h2{font-size:48px;margin-bottom:10px}'
       '#setS .srow{padding:9px 14px;margin-bottom:7px;font-size:16px}#setS .srow small{font-size:11px}#setClose{width:96px;height:96px;bottom:calc(var(--sab) + 16px)}}'
       '@media (max-height:600px){#setS{padding-top:calc(var(--sat) + 8px);padding-bottom:calc(var(--sab) + 108px)}#setS h2{font-size:40px;margin-bottom:6px}'
       '#setS .srow{padding:7px 12px;margin-bottom:6px;border-radius:14px}#setS .srow small{line-height:1.15}#setS .ver{margin-top:2px}'
       '#setClose{width:88px;height:88px;bottom:calc(var(--sab) + 12px)}#setClose b{font-size:20px}}'
       '@media (max-width:359px){#levels h2{font-size:38px}}')
ANCHOR = '.srow.off span:last-child{background:#9aa3b2}'
HTML = [  # (old, new, required in index.html)
    ('Flix Atış 1.2 · FLIX TOYS', 'Flix Atış ' + VER + ' · FLIX TOYS', True),
    ('<button class="btn" id="setClose" style="right:18px;bottom:calc(var(--sab) + 26px);width:112px;height:112px">', '<button class="btn" id="setClose">', True),
    (ANCHOR + '\n', ANCHOR + '\n' + CSS + '\n', True),
    ('FlixLegal.init({"game": "atis", "name": "Flix Atış", ', 'FlixLegal.init({"game": "atis", "name": "Flix Atış", "version": "' + VER + '", ', True),
]
JS = [
    ('if (SAVE.noads || BOT || cur < AD_CFG.interFromLevel) return Promise.resolve(false); if (SAVE.adN % AD_CFG.interEvery) return Promise.resolve(false); return adInterstitial(); }',
     'if (SAVE.noads || BOT || SAVE.adN < AD_CFG.interFromLevel || SAVE.adN % AD_CFG.interEvery) return Promise.resolve(false); return adInterstitial(); } // adN = finished levels: 3, 6, 9...', True),
    ('\nwindow.__A = {', '\nif (!NATIVE || BOT) window.__A = {', True),  # test hooks: web / ?bot=1 only, never in the app
]
def apply(f, reps):
    s = open(f, encoding='utf-8').read(); o = s
    for old, new, req in reps:
        if new in s: continue
        n = s.count(old)
        if n == 0 and not req: continue
        assert n == 1, (f, old[:60], n)
        s = s.replace(old, new)
    if s != o: open(f, 'w', encoding='utf-8').write(s); print('patched', f)
    else: print('already', f)
apply(os.path.join(D, '..', 'index.html'), HTML + JS)
apply(os.path.join(D, 'game10.js'), JS)
apply(os.path.join(D, 'shell7.html'), [(a, b, False) for a, b, _ in HTML])
