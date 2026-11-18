import urllib.request, ssl
ssl._create_default_https_context = ssl._create_unverified_context

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

urls = [
    ("XC6206-torex2", "https://www.torexsemi.com/file/xc6206/pdf/"),
    ("XC6206-torex3", "https://www.torexsemi.com/file/xc6206/pdf/xc6206_series.pdf"),
    ("XC6206-torex4", "https://www.torexsemi.com/file/xc6206/pdf/xc6206p.pdf"),
    ("CH340C-wch2", "http://www.wch.cn/downloads/CH340DS1_PDF.html"),
    ("CH340C-github", "https://raw.githubusercontent.com/search?q=CH340C+datasheet+pdf"),
    ("CH340C-jlc", "https://datasheet.lcsc.com/lcsc/1812281614_WCH-Jiangsu-Qin-Heng-CH340C_C84681.pdf"),
]

for name, url in urls:
    try:
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req, timeout=15)
        data = resp.read(8)
        if data[:4] == b"%PDF":
            print(f"OK  {name}: {url}")
        else:
            print(f"HTML {name}: {url} -> {data[:20]}")
    except Exception as e:
        print(f"FAIL {name}: {url} -> {e}")
