# PRADEEP BHAI SARKARI SERVICE - Ultimate Master Code
from kivy.app import App
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.utils import get_color_from_hex
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import webbrowser

Window.clearcolor = get_color_from_hex("#F5F7FC")

def open_url(url):
    try:
        webbrowser.open(url)
    except Exception:
        Popup(title="Link error",
              content=Label(text="Browser link could not be opened."),
              size_hint=(.8, .3)).open()

MAIN_SERVICES = [
    ("AADHAAR CARD", "Download | Update | Lock/Unlock", "https://uidai.gov.in/", "#F32135"),
    ("PAN CARD", "Apply | Download | e-PAN", "https://www.incometax.gov.in/iec/foportal/", "#1265E8"),
    ("VOTER CARD", "Apply | Download | Check", "https://voters.eci.gov.in/", "#078A38"),
    ("RATION CARD", "Apply | Download | Status", "https://nfsa.gov.in/", "#8515D6"),
    ("e-SHRAM CARD", "Apply | Download | Registration", "https://eshram.gov.in/", "#F28A00"),
    ("AYUSHMAN CARD", "Apply | Download | Check", "https://beneficiary.nha.gov.in/", "#05AFC1"),
    ("NSDL / PROTEAN", "PAN | eSign | Other services", "https://www.protean-tinpan.com/", "#36A400"),
    ("UTI PAN SERVICE", "Apply | Download | Status", "https://www.pan.utiitsl.com/", "#E8178B"),
]

MORE_SERVICES = [
    ("Passport Seva", "https://www.passportindia.gov.in/", "#C8E0FF"),
    ("Income Tax e-Filing", "https://www.incometax.gov.in/iec/foportal/", "#D5F7C9"),
    ("Driving Licence", "https://sarathi.parivahan.gov.in/", "#E6D8FF"),
    ("Vehicle RC / Vahan", "https://vahan.parivahan.gov.in/", "#FFE8A8"),
    ("DigiLocker", "https://www.digilocker.gov.in/", "#C9F6FA"),
    ("PM Kisan Samman Nidhi", "https://pmkisan.gov.in/", "#E8D7FF"),
    ("Scholarship Portal", "https://scholarships.gov.in/", "#D8F7CA"),
    ("Labour Services", "https://labour.gov.in/", "#FFDCE7"),
    ("Pension / NSAP", "https://nsap.nic.in/", "#D8E8FF"),
    ("Jan Aadhaar", "https://janaadhaar.rajasthan.gov.in/", "#D8F7C8"),
    ("Birth / Death Certificate", "https://crsorgi.gov.in/", "#D8F4F8"),
    ("GST Portal", "https://www.gst.gov.in/", "#FFF0C2"),
]

class PradeepBhaiSarkariServiceApp(App):
    def build(self):
        self.title = "Pradeep Bhai Sarkari Service"
        root = BoxLayout(orientation="vertical", padding=dp(6), spacing=dp(5))

        # Header Area
        header = BoxLayout(orientation="vertical", size_hint_y=None, height=dp(80), spacing=dp(0))
        header.add_widget(Label(
            text="[b][color=#142C83]PRADEEP BHAI SARKARI SERVICE[/color][/b]",
            markup=True, font_size="19sp", halign="center"))
        header.add_widget(Label(
            text="[b]Sabka Saath, Sabka Vikas[/b]  |  100% Safe & Secure",
            markup=True, color=get_color_from_hex("#20366E"), font_size="12sp", halign="center"))
        root.add_widget(header)

        # Banner
        banner = Button(
            text="[b]Online Sarkari Seva[/b]  (Verified Portal)\nGhar Baithe Sabhi Kaam Karen",
            markup=True, size_hint_y=None, height=dp(50),
            background_normal="", background_color=get_color_from_hex("#142D8B"),
            color=(1, 1, 1, 1), font_size="13sp")
        root.add_widget(banner)

        scroll = ScrollView(do_scroll_x=False, bar_width=dp(4))
        body = BoxLayout(orientation="vertical", size_hint_y=None, spacing=dp(6))
        body.bind(minimum_height=body.setter("height"))

        # Main Service Rows
        for title, subtitle, url, color in MAIN_SERVICES:
            row_btn = Button(
                text=f"    [b]{title}[/b]\n         [color=#FFF000]{subtitle}[/color]    > ",
                markup=True,
                halign="left",
                valign="middle",
                size_hint_y=None,
                height=dp(68),
                padding=(dp(10), dp(5)),
                background_normal="",
                background_color=get_color_from_hex(color),
                color=(1, 1, 1, 1),
                font_size="14sp"
            )
            row_btn.bind(on_release=lambda _btn, target=url: open_url(target))
            body.add_widget(row_btn)

        # More Services Title
        body.add_widget(Label(
            text="[b][color=#142C83]MORE ONLINE GOVERNMENT SERVICES[/color][/b]",
            markup=True, size_hint_y=None, height=dp(30), font_size="13sp"))

        # Grid Services
        grid = GridLayout(cols=2, spacing=dp(5), size_hint_y=None)
        grid.bind(minimum_height=grid.setter("height"))
        for name, url, color in MORE_SERVICES:
            b = Button(text=f"[b]{name}[/b]", markup=True,
                       size_hint_y=None, height=dp(50),
                       background_normal="", background_color=get_color_from_hex(color),
                       color=get_color_from_hex("#101D4D"), font_size="12sp")
            b.bind(on_release=lambda _btn, target=url: open_url(target))
            grid.add_widget(b)
        body.add_widget(grid)
        scroll.add_widget(body)
        root.add_widget(scroll)

        # Bottom Tab Navigation
        bottom = BoxLayout(size_hint_y=None, height=dp(48), spacing=dp(2))
        for label in ("Home", "Favorites", "History", "Settings"):
            b = Button(text=label, font_size="12sp",
                       background_normal="",
                       background_color=get_color_from_hex("#10277F"),
                       color=(1, 1, 1, 1))
            b.bind(on_release=lambda _btn, tab=label: self.bottom_action(tab))
            bottom.add_widget(b)
        root.add_widget(bottom)
        return root

    def bottom_action(self, tab):
        if "Home" in tab:
            return
        message = {
            "Favorites": "Aapke pasandida sarkari sewayein yahan dikhengi.",
            "History": "Aapke dwara khole gaye portals ka record.",
            "Settings": "Pradeep Bhai Sarkari Service Settings & About."
        }.get(tab, "Pradeep Bhai Sarkari Service")
        Popup(title=tab, content=Label(text=message, halign="center"),
              size_hint=(.8, .25)).open()

if __name__ == "__main__":
    PradeepBhaiSarkariServiceApp().run()
