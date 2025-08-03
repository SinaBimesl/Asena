import sys
from PyQt5 import QtWidgets, uic
from dns_manager import show_current_dns  


app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("dns_ui.ui")


def on_show_current_dns():
    current_dns = show_current_dns()
    # اگر لیست بود، به رشته تبدیل می‌کنیم
    if isinstance(current_dns, list):
        current_dns = ", ".join(current_dns)
    window.label_current_dns.setText(current_dns)

# وصل کردن دکمه به تابع
window.btn_show_current_dns.clicked.connect(on_show_current_dns)

# نمایش پنجره
window.show()
sys.exit(app.exec_())
