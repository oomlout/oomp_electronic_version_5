import urllib.request, ssl
ssl._create_default_https_context = ssl._create_unverified_context

urls = [
    ("XC6206-octopart", "https://octopart.com/xc6206p332mr-torex-5365305"),
    ("XC6206-mouser-direct", "https://www.mouser.com/ProductDetail/Torex-Semiconductor/XC6206P332MR-G"),
    ("XC6206-digikey", "https://www.digikey.com/en/products/detail/torex-semiconductor-ltd/XC6206P332MR-G/6198310"),
    ("CH340C-pdf-jlc", "https://datasheet.lcsc.com/lcsc/1812281614_WCH-Jiangsu-Qin-Heng-CH340C_C84681.pdf"),
    ("CH340C-wch-direct", "http://www.wch-ic.com/downloads/CH340DS1_PDF.html"),
    ("CH340C-alldatasheet", "https://pdf1.alldatasheet.com/datasheet-pdf/view/1131748/WCH/CH340C.html"),
]

for name, url in urls:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        resp = urllib.request.urlopen(req, timeout=15)
        data = resp.read(100)
        if b"%PDF" in data[:10]:
            print(f"OK  {name}: {url}")
        else:
            print(f"HTML {name}: {url} -> {data[:50]}")
    except Exception as e:
        print(f"FAIL {name}: {url} -> {e}")
