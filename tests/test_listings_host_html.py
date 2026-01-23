from playwright.sync_api import Page, expect
import re

def test_listings_page_title(logged_in_page, test_web_address):
    logged_in_page.goto(f"http://{test_web_address}/host/listings")
    expect(logged_in_page).to_have_title("My Listings · makersbnb")

def test_listings_page_header(logged_in_page, test_web_address):
    logged_in_page.goto(f"http://{test_web_address}/host/listings")
    header = logged_in_page.locator("h2")
    expect(header).to_have_text("Your Listings")

def test_add_listing_button_present(logged_in_page, test_web_address):
    logged_in_page.goto(f"http://{test_web_address}/host/listings")
    add_button = logged_in_page.locator("a[href='/host/add_listing']")
    expect(add_button).to_be_visible()

def test_navigation_arrows_present(logged_in_page, test_web_address):
    logged_in_page.goto(f"http://{test_web_address}/host/listings")
    arrows = logged_in_page.locator(".btn-outline-secondary.btn-sm")
    expect(arrows).to_have_count(2)

def test_no_listings_message(logged_in_page, test_web_address):
    logged_in_page.goto(f"http://{test_web_address}/host/listings")
    message = logged_in_page.locator("text=You have no properties listed")
    expect(message).to_be_visible()

def test_listing_cards_container(logged_in_page, test_web_address):
    logged_in_page.goto(f"http://{test_web_address}/host/listings")
    container = logged_in_page.locator(".container")
    expect(container.first).to_be_visible()

def test_page_extends_base(logged_in_page, test_web_address):
    logged_in_page.goto(f"http://{test_web_address}/host/listings")
    navbar = logged_in_page.locator(".navbar")
    expect(navbar).to_be_visible()

def test_footer_present(logged_in_page, test_web_address):
    logged_in_page.goto(f"http://{test_web_address}/host/listings")
    footer = logged_in_page.locator("footer")
    expect(footer).to_be_visible()

def test_add_listing_button_styling(logged_in_page, test_web_address):
    logged_in_page.goto(f"http://{test_web_address}/host/listings")
    add_button = logged_in_page.locator("a[href='/host/add_listing']")
    expect(add_button).to_have_class(re.compile("btn-secondary"))

def test_redirect_when_not_logged_in(page, test_web_address):
    page.goto(f"http://{test_web_address}/host/listings")
    expect(page).to_have_url(re.compile("/login"))

def test_add_listing_page_title(logged_in_page, test_web_address):
    logged_in_page.goto(f"http://{test_web_address}/host/add_listing")
    expect(logged_in_page).to_have_title("Add New Listing · makersbnb")

def test_add_listing_page_header(logged_in_page, test_web_address):
    logged_in_page.goto(f"http://{test_web_address}/host/add_listing")
    header = logged_in_page.locator("h2")
    expect(header).to_have_text("Add a New Listing")

def test_add_listing_form_method(logged_in_page, test_web_address):
    logged_in_page.goto(f"http://{test_web_address}/host/add_listing")
    form = logged_in_page.locator("form")
    expect(form).to_have_attribute("method", "POST")

def test_property_name_input(logged_in_page, test_web_address):
    logged_in_page.goto(f"http://{test_web_address}/host/add_listing")
    input_field = logged_in_page.locator("input[name='name']")
    expect(input_field).to_be_visible()

def test_description_textarea(logged_in_page, test_web_address):
    logged_in_page.goto(f"http://{test_web_address}/host/add_listing")
    textarea = logged_in_page.locator("textarea[name='description']")
    expect(textarea).to_be_visible()

def test_price_input(logged_in_page, test_web_address):
    logged_in_page.goto(f"http://{test_web_address}/host/add_listing")
    input_field = logged_in_page.locator("input[name='price_per_night']")
    expect(input_field).to_be_visible()

def test_image_input(logged_in_page, test_web_address):
    logged_in_page.goto(f"http://{test_web_address}/host/add_listing")
    input_field = logged_in_page.locator("input[name='image']")
    expect(input_field).to_be_visible()


def test_submit_button_present(logged_in_page, test_web_address):
    logged_in_page.goto(f"http://{test_web_address}/host/add_listing")
    submit_button = logged_in_page.locator("button[type='submit']")
    expect(submit_button).to_be_visible()

