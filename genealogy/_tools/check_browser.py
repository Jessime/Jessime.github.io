"""Exercise the static site in Chromium, including mobile and file:// mode."""
import functools
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import threading
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
SITE = HERE.parent.parent if HERE.name == '_tools' else Path('/Users/jessime/Code/me/Jessime.github.io')
OUT = HERE/'browser-checks'
OUT.mkdir(exist_ok=True)

class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_):
        pass

server = ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(QuietHandler, directory=str(SITE)))
threading.Thread(target=server.serve_forever, daemon=True).start()
url = f'http://127.0.0.1:{server.server_port}/genealogy/'
try:
    with sync_playwright() as pw:
        browser = pw.chromium.launch(channel='chrome', headless=True)
        context = browser.new_context(viewport={'width':1440,'height':1100}, device_scale_factor=1)
        page = context.new_page()
        errors, failures = [], []
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.on('response', lambda response: failures.append(response.url) if response.status >= 400 else None)
        page.goto(url)
        page.wait_for_selector('.profile h2')
        assert page.locator('#people-count').inner_text() == '2,144'
        assert 'Johann (Jean)' in page.locator('.profile h2').inner_text()
        assert page.locator('#result-count').inner_text() == '2,144 people in the archive'
        response = context.request.get(url + 'source.pdf')
        assert response.status == 200 and response.body().startswith(b'%PDF')
        assert context.request.get(url + 'data.json').json()['meta']['people'] == 2144
        page.screenshot(path=str(OUT/'desktop.png'), full_page=True)
        page.locator('#search').fill('jessime')
        assert page.locator('.result').count() == 1
        page.locator('.result').click()
        assert page.locator('.profile h2').inner_text() == 'Jessime Murray Kirk'
        assert page.locator('#profile a[data-person]').filter(has_text='Jilani E. Trabelsi').count() == 1
        person_hash = page.evaluate('location.hash')
        page.locator('#original-entry summary').click()
        assert '10 Nov 1991' in page.locator('#original-entry pre').inner_text()
        assert page.locator('.source-head a').get_attribute('href') == 'source.pdf#page=20'
        page.screenshot(path=str(OUT/'jessime.png'), full_page=True)
        page.locator('#profile').get_by_role('link', name='Linda Kay Murray-Kirk', exact=True).first.click()
        assert page.locator('.profile h2').inner_text() == 'Linda Kay Murray-Kirk'
        page.go_back()
        assert page.locator('.profile h2').inner_text() == 'Jessime Murray Kirk'
        page.reload()
        assert page.locator('.profile h2').inner_text() == 'Jessime Murray Kirk'
        page.locator('#copy-link').click()
        page.wait_for_function("document.getElementById('copy-link').textContent === 'Link copied ✓' || document.getElementById('copy-fallback') !== null")
        page.locator('[data-view=outline]').click()
        assert page.locator('#outline-panel').is_visible()
        assert page.locator('.tree-node.is-selected').get_attribute('data-tree-id') == person_hash[1:]
        assert page.locator('.tree-node[open]').count() >= 7
        page.locator('#collapse-tree').click()
        assert page.locator('.tree-node[open]').count() == 0
        page.locator('#show-lineage').click()
        assert page.locator('.tree-node[open]').count() >= 7
        page.screenshot(path=str(OUT/'outline.png'), full_page=True)
        page.locator('[data-view=directory]').click()
        page.locator('#reset').click()
        page.locator('#search').fill('luxembourg 1780')
        assert page.locator('.result').count() == 1
        page.locator('#search').fill('zzzznonexistent')
        assert page.locator('.empty').is_visible()
        page.locator('#reset').click()
        page.locator('#generation').select_option('9')
        assert '44 people' in page.locator('#result-count').inner_text()
        page.locator('#reset').click()
        page.locator('#review-only').check()
        assert page.locator('.result').count() == 35
        page.locator('#search').fill('rebekah avery')
        page.locator('.result').click()
        assert page.locator('.review-notes').is_visible()
        assert 'No partner link has been asserted' in page.locator('.review-notes').inner_text()
        page.locator('[data-view=about]').click()
        assert page.locator('#about-panel').is_visible()
        assert '35 records' in page.locator('#review-explanation').inner_text()
        page.locator('.wordmark').click()
        assert page.locator('#directory').is_visible()
        assert 'Johann (Jean)' in page.locator('.profile h2').inner_text()
        page.locator('#reset').click()
        page.locator('#load-more').click()
        assert page.locator('.result').count() == 120
        page.locator('#sort').select_option('birth')
        assert 'Johann (Jean)' in page.locator('.result').first.inner_text()
        assert not errors, errors
        assert not failures, failures
        # Real mobile layout and keyboard search/navigation.
        mobile = context.new_page()
        mobile.set_viewport_size({'width':390,'height':844})
        mobile.on('pageerror', lambda error: errors.append(str(error)))
        mobile.goto(url + person_hash)
        assert mobile.locator('.profile h2').inner_text() == 'Jessime Murray Kirk'
        assert mobile.evaluate('document.documentElement.scrollWidth <= innerWidth')
        mobile.locator('#search').fill('ginsbach')
        mobile.locator('.result').first.focus()
        mobile.keyboard.press('Enter')
        assert 'Ginsbach' in mobile.locator('.profile h2').inner_text()
        assert mobile.evaluate('document.documentElement.scrollWidth <= innerWidth')
        mobile.screenshot(path=str(OUT/'mobile.png'), full_page=True)
        mobile.locator('[data-view=outline]').click()
        mobile.locator('#show-lineage').click()
        assert mobile.evaluate('document.documentElement.scrollWidth <= innerWidth')
        # Direct local files require neither a server nor fetch/CORS exceptions.
        local = context.new_page()
        local.on('pageerror', lambda error: errors.append(str(error)))
        local.goto((SITE/'genealogy/index.html').as_uri() + person_hash)
        assert local.locator('.profile h2').inner_text() == 'Jessime Murray Kirk'
        local.locator('#search').fill('agnes thi huong')
        assert local.locator('.result').count() == 1
        assert not errors, errors
        print('PASS: desktop, mobile, search, generation/review filters, sorting, pagination, relatives, outline, original entry, deep links, browser history, reload, keyboard, file://, no JS errors or HTTP failures.')
        browser.close()
finally:
    server.shutdown()
