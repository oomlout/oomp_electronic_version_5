import urllib.request, ssl
ssl._create_default_https_context = ssl._create_unverified_context

urls = [
    ("AMS1117-http", "http://www.advanced-monolithic.com/pdf/ds1117.pdf"),
    ("AMS1117-alt", "https://www.datasheets360.com/pdf/1012931451313483747"),
    ("XC6206-mouser", "https://www.mouser.com/datasheet/2/760/TOSL_S_A0007229533_1-2575067.pdf"),
    ("XC6206-everythingpe", "https://www.torexsemi.com/file/xc6206/pdf"),
    ("CH340C-wch", "http://www.wch.cn/downloads/CH340DS1_PDF.html"),
    ("CH340C-pdf", "http://www.wch-ic.com/downloads/CH340DS1_PDF.html"),
    ("CP2102N-silabs", "https://www.silabs.com/documents/public/data-sheets/CP2102N.pdf"),
    ("CP2102N-silabs2", "https://www.silabs.com/documents/public/data-sheets/cp2102n-datasheet.pdf"),
    ("CP2102N-mouser", "https://www.mouser.com/datasheet/2/368/CP2102N-2706508.pdf"),
]

for name, url in urls:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        resp = urllib.request.urlopen(req, timeout=15)
        data = resp.read(8)
        if data[:4] == b"%PDF":
            print(f"OK  {name}: {url}")
        else:
            print(f"HTML {name}: {url} -> {data[:20]}")
    except Exception as e:
        print(f"FAIL {name}: {url} -> {e}")
