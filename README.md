**Modul pribadi iewil** adalah toolkit Python untuk membangun skrip CLI yang rapi dan interaktif, dengan fitur gradient display, banner, captcha helper, HTML scraping, dan cache storage.

<a href="https://youtube.com/c/iewil"><img src="https://img.shields.io/youtube/channel/subscribers/UCvBSqRaT6nsPvtl8m6GaQpg?style=social" alt="Youtube: iewil" /></a>&nbsp;&nbsp;&nbsp;
<a href="https://github.com/iewilmaestro"><img src="https://img.shields.io/github/followers/iewilmaestro?style=social" alt="Github: iewil" /></a>&nbsp;&nbsp;&nbsp;
<a href="https://t.me/fat9ght"><img src="https://img.shields.io/badge/Telegram-Iewil-green?style=social&logo=Telegram" alt="Telegram: iewil" /></a>

> ⚠️ **FREE SCRIPT NOT FOR SALE!**
> Gunakan modul ini untuk keperluan pribadi atau pengembangan, tidak untuk dijual.

---

## Fitur Utama

* **Display & Banner CLI**

  * Gradient teks & background
  * Garis pemisah, peringatan, dan info rata kiri

* **Captcha Helper**

  * Mendukung provider Xevil & Multibot
  * Fungsi solving progress dengan spinner

* **HTML Scraping**

  * Ambil input form, opsi, captcha, dan limit dari halaman HTML
  * Response parsing otomatis (success/warning/locked/cloudflare)

* **Cache Storage**

  * Simpan data seperti cookie, username, password, email, user-agent
  * Bisa otomatis atau manual tanpa mengganggu user

* **ShowError / Debugging**

  * Log error ke file
  * Tampilkan error di terminal dengan format rapi

---

## Instalasi

```bash
pip install iewil==0.0.6
```

---

## Cara Pakai

```python
from iewil.functions.display import Display
from iewil.functions.show_error import ShowError
from iewil.functions.cache_storage import CacheStorage

# Set title & register
Display.TITLE = "MyScript"
Display.REGISTER = "t.me/MyBot"

# Tampilkan banner
Display.banner(author="iewil")

# Menyimpan cache
CacheStorage.simpan("cookie")
CacheStorage.simpan("user")

# Tangani error
error_handler = ShowError("error.log")
error_handler._start()
```
* Display
```python
# test display
from iewil import Display

# Set Banner
Display.TITLE = "MyScript"
Display.REGISTER = "t.me/MyBot"
Display.banner()

Display.title("TEST DISPLAY")
Display.info("Ini info")
Display.debug("Ini debug")
Display.sukses("Berhasil")
Display.error("Error contoh")
Display.timer(10)
```
* DataStore
```python
# test datastore
from iewil import DataStore

# Simpan data
# minta input dari user
cookie = DataStore.simpan("cookie")

# langsung set value
user = DataStore.simpan("user", "admin123")

# Hapus data
DataStore.hapus("cookie")
```
* BP Captcha (xevil & multibot)
```python
# test BP Captcha
from iewil import Captcha

cap = Captcha()
print("Balance:", cap.get_balance())

token = cap.Turnstile("0x4AAAAAAAxL-BbCFZ3EZbE9", "https://clxaward.com/")
print(token)
```
* ShowError
```python
from iewil import ShowError

ShowError().start()

Display.info("Program dimulai")

x = 1 / 0   # error disengaja

```

## Donasi
* ![BTC](https://img.shields.io/badge/BTC-18jswG2t9EZrnHju5dyiYw1yGbkcrTSgJg-blue?style=flat-square\&logo=bitcoin)
* ![Paypal](https://img.shields.io/badge/Paypal-Purna.iera@gmail.com-blue?style=flat-square\&logo=paypal)
* ![Dana](https://img.shields.io/badge/Dana-085819008551-blue?style=flat-square\&logo=idr)
