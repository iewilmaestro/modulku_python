# test cek Dir
import iewil
print(iewil.__all__)

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

# test datastore
from iewil import DataStore

# Simpan data
# minta input dari user
cookie = DataStore.simpan("cookie")

# langsung set value
user = DataStore.simpan("user", "admin123")

# Hapus data
DataStore.hapus("cookie")

# test BP Captcha
from iewil import Captcha

cap = Captcha()
print("Balance:", cap.get_balance())

token = cap.Turnstile("0x4AAAAAAAxL-BbCFZ3EZbE9", "https://clxaward.com/")
print(token)

# test show_error
from iewil import ShowError

ShowError().start()

Display.info("Program dimulai")

x = 1 / 0   # error disengaja
