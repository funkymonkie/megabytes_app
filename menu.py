import sys
import time


class MegaBytesMenu:

    def display_menu(self):
        menu_html = "<div>"
        menu_html += "<h2>Drinks:</h2><ul>"
        self.get_animated_banner_html()
        for item_number in range(1, 7):
            drinks_name, drinks_price, drinks_emoji = self.get_item_details(item_number)
            menu_html += f"<li>{item_number}. {drinks_emoji} {drinks_name}: £{float(drinks_price):.2f}</li>"

        menu_html += "</ul><h2>Food:</h2><ul>"

        for item_number in range(7, 13):
            food_name, food_price, food_emoji = self.get_item_details(item_number)
            menu_html += f"<li>{item_number}. {food_emoji} {food_name}: £{float(food_price):.2f}</li>"

        menu_html += "</ul></div>"

        return menu_html

    def get_animated_banner_html(self):
        banner_frames = [
            "      ☕🥐🧁 Welcome to MegaBytes Menu! 🧁🥐☕",
            "      🥐🧁☕ Welcome to MegaBytes Menu! ☕🧁🥐",
            "      🧁☕🥐 Welcome to MegaBytes Menu! 🥐☕🧁",
        ]

        banner_html = "<div class='animated-banner'>"
        for frame in banner_frames:
            banner_html += f"<p>{frame}</p>"
        banner_html += "</div>"

        return banner_html

    def get_item_details(self, item_number):
        menu_items = {
            1: ("Tea", 1.00, "☕"),
            2: ("Americano", 1.70, "☕"),
            3: ("Latte", 1.90, "☕"),
            4: ("Cappuccino", 1.90, "☕"),
            5: ("Mocha", 2.00, "☕"),
            6: ("Hot Chocolate", 2.20, "☕"),
            7: ("Croissant", 1.50, "🥐"),
            8: ("Muffin", 2.10, "🧁"),
            9: ("Toast", 1.00, "🍞"),
            10: ("Panini", 2.90, "🥪"),
            11: ("Buttered Roll", 0.70, "🍞"),
            12: ("Stroopwafel", 0.50, "🍪"),
        }
        return menu_items[int(item_number)]
