from playwright.sync_api import Page, expect

def test_get_page_title(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    brand = page.locator("a.navbar-brand")
    expect(brand).to_contain_text("makersbnb")

def test_header_available_homes(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text("Available Homes")

def test_navbar_logo_present(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    logo = page.locator("img[alt='Logo']")
    expect(logo).to_be_visible()

def test_navbar_brand_text(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    brand = page.locator(".navbar-brand span")
    expect(brand).to_have_text("makersbnb")

def test_navbar_brand_is_link(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    brand_link = page.locator("a.navbar-brand")
    expect(brand_link).to_have_attribute("href", "/")

def test_navbar_profile_image_present(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    profile = page.locator("img[alt='Profile']")
    expect(profile).to_be_visible()

def test_navbar_profile_dropdown_toggle(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    dropdown_toggle = page.locator("#profileDropdown")
    expect(dropdown_toggle).to_be_visible()

def test_navbar_dropdown_menu_present(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    dropdown_menu = page.locator(".dropdown-menu")
    expect(dropdown_menu).to_be_attached()

def test_navbar_dropdown_feedback_link(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    dropdown_toggle = page.locator("#profileDropdown")
    dropdown_toggle.click()
    feedback_link = page.locator("text=Feedback")
    expect(feedback_link).to_be_visible()

def test_navbar_dropdown_privacy_link(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    dropdown_toggle = page.locator("#profileDropdown")
    dropdown_toggle.click()
    privacy_link = page.locator("text=Privacy Statement")
    expect(privacy_link).to_be_visible()

def test_navbar_dropdown_terms_link(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    dropdown_toggle = page.locator("#profileDropdown")
    dropdown_toggle.click()
    terms_link = page.locator("text=Terms & Conditions")
    expect(terms_link).to_be_visible()

def test_navbar_dropdown_contact_link(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    dropdown_toggle = page.locator("#profileDropdown")
    dropdown_toggle.click()
    contact_link = page.locator("text=Contact us")
    expect(contact_link).to_be_visible()

def test_search_bar_where_input(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    where_input = page.locator("input[placeholder='Where']")
    expect(where_input).to_be_visible()
    expect(where_input).to_have_attribute("name", "location")

def test_search_bar_when_input(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    when_input = page.locator("input[placeholder='When']")
    expect(when_input).to_be_visible()
    expect(when_input).to_have_attribute("name", "date")

def test_search_bar_who_input(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    who_input = page.locator("input[placeholder='Who']")
    expect(who_input).to_be_visible()
    expect(who_input).to_have_attribute("name", "guests")

def test_search_bar_submit_button(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    submit_button = page.locator("button[type='submit']")
    expect(submit_button).to_be_visible()

def test_search_bar_form_present(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    search_form = page.locator("form")
    expect(search_form).to_be_visible()
    expect(search_form).to_have_attribute("method", "GET")
    expect(search_form).to_have_attribute("action", "/")

def test_navigation_arrows_present(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    arrows = page.locator(".btn-outline-secondary.btn-sm")
    expect(arrows).to_have_count(2)

def test_property_cards_container_present(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    cards_container = page.locator(".row.g-4")
    expect(cards_container).to_be_visible()

def test_property_card_structure(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    card = page.locator(".card").first
    expect(card).to_be_visible()

def test_property_card_has_image(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    card_image = page.locator(".card-img-top").first
    expect(card_image).to_be_visible()

def test_property_card_image_has_alt_text(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    card_image = page.locator(".card-img-top").first
    alt_text = card_image.get_attribute("alt")
    assert "Photo of" in alt_text

def test_property_card_has_title(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    card_title = page.locator(".card-title").first
    expect(card_title).to_be_visible()

def test_property_card_has_description(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    card_text = page.locator(".card-text").first
    expect(card_text).to_be_visible()

def test_property_card_has_price(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    card_footer = page.locator(".card-footer").first
    expect(card_footer).to_be_visible()
    expect(card_footer).to_contain_text("night")

def test_footer_present(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    footer = page.locator("footer")
    expect(footer).to_be_visible()

def test_footer_copyright(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    footer = page.locator("footer")
    expect(footer).to_contain_text("©2026 All Rights Reserved")

def test_footer_links(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    footer = page.locator("footer")
    expect(footer).to_contain_text("Privacy")
    expect(footer).to_contain_text("Terms")
    expect(footer).to_contain_text("Contact")

def test_page_title(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    expect(page).to_have_title("Available Homes · makersbnb")

def test_bootstrap_loaded(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    container = page.locator(".container").first
    expect(container).to_be_visible()

def test_custom_font_applied(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    body = page.locator("body")
    expect(body).to_be_visible()