from flask import Blueprint, render_template, request
from customers_reviews import customer_review_data
from menu import MegaBytesMenu

my_view = Blueprint("my_view", __name__)


@my_view.route("/")
def index():
    return render_template("/index.html")


@my_view.route("/menu")
def menu():
    menu_instance = MegaBytesMenu()
    menu_html = menu_instance.display_menu()
    return render_template("/menu.html", menu_html=menu_html)


@my_view.route("/leave_a_review", methods=["GET", "POST"])
def get_review():
    if request.method == "POST":
        customer_name = request.form.get("customer_name")
        rating = request.form.get("rating")
        comment = request.form.get("comment")

        # Create a dictionary to store the review details
        review = {"customer_name": customer_name, "rating": rating, "comment": comment}

        # Append the review dictionary to the customer_review_data list
        customer_review_data.append(review)

    return render_template("reviews.html", customer_review_data=customer_review_data)
