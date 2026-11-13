#!/usr/bin/env python3
"""v11 (1.5.1 TestFlight): "Gizlilik Seçenekleri" row in Settings.
Google requires a way to change or withdraw ad consent (UMP privacy options entry point) for players in the EEA / UK / Switzerland.
The row only appears inside the iOS app when Google says it is required (FlixAds.privacyOptionsRequired(), app/www/ads.js);
tapping it reopens Google's consent form (FlixAds.showPrivacyOptions()). Nothing changes on the web build.

Patches the built game in place (default ../index.html). Safe to run twice.
Usage: python3 patch11.py [path/to/index.html]"""
import pathlib, sys

path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parent.parent / 'index.html'
s = path.read_text(encoding='utf-8')
if 'id="privRow"' in s:
    sys.exit('already patched: ' + str(path))

ROW_AFTER = '<span id="restT">Geri yükle</span></button>'
ROW = ('\n    <button class="srow link" id="privRow" hidden><span>Gizlilik Seçenekleri<small>Privacy Options · reklam izinleri</small></span>'
       '<span id="privT">Aç</span></button>')
assert s.count(ROW_AFTER) == 1, 'restore row not found'
s = s.replace(ROW_AFTER, ROW_AFTER + ROW, 1)

SCRIPT = r'''<script>/* FLIX privacy options (v11): Google UMP entry point, app only */
(function () {
  var row = document.getElementById('privRow'), lab = document.getElementById('privT');
  if (!row) return;
  function sync() { var A = window.FlixAds; row.hidden = !(A && A.privacyOptionsRequired && A.privacyOptionsRequired()); }
  window.addEventListener('flixprivacy', sync);
  sync();
  row.addEventListener('click', function () {
    var A = window.FlixAds; if (!A || !A.showPrivacyOptions || lab.textContent === '...') return;
    lab.textContent = '...';
    A.showPrivacyOptions().then(function () { lab.textContent = 'Aç'; sync(); }, function () { lab.textContent = 'Aç'; });
  });
})();
</script>
'''
assert s.count('</body>') == 1, '</body> not found'
s = s.replace('</body>', SCRIPT + '</body>', 1)
path.write_text(s, encoding='utf-8')
print('patched', path)
