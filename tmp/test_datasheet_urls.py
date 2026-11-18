import urllib.request, ssl
ssl._create_default_https_context = ssl._create_unverified_context

urls = [
    ("AMS1117-5.0", "https://www.advanced-monolithic.com/pdf/ds1117.pdf"),
    ("AMS1117-5.0-alt", "https://pdf1.alldatasheet.com/datasheet-pdf/view/17123441/AMS/AMS1117-5.0.html"),
    ("XC6206", "https://www.torexsemi.com/file/xc6206/pdf/xc6206.pdf"),
    ("XC6206-alt", "https://pdf1.alldatasheet.com/datasheet-pdf/view/243854/TOREX/XC6206P332MR.html"),
    ("ATmega328P", "https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7810-Automotive-Microcontrollers-ATmega328P_Datasheet.pdf"),
    ("CH340C", "http://www.wch-ic.com/downloads/CH340DS1_PDF.html"),
    ("CP2102N", "https://www.silabs.com/documents/public/data-sheets/cp2102n-data-sheet.pdf"),
    ("ESP32-S3", "https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf"),
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
