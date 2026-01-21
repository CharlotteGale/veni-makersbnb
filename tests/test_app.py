from playwright.sync_api import Page, expect

def test_get_page_title(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    p_tag = page.locator("p.navbar-brand")
    expect(p_tag).to_contain_text("makersbnb")

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

def test_navbar_become_host_link(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    become_host = page.locator("text=Become a Host")
    expect(become_host).to_be_visible()

def test_navbar_profile_image_present(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    profile = page.locator("img[alt='Profile']")
    expect(profile).to_be_visible()

def test_search_bar_where_input(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    where_input = page.locator("input[placeholder='Where']")
    expect(where_input).to_be_visible()

def test_search_bar_when_input(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    when_input = page.locator("input[placeholder='When']")
    expect(when_input).to_be_visible()

def test_search_bar_who_input(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    who_input = page.locator("input[placeholder='Who']")
    expect(who_input).to_be_visible()

def test_search_bar_submit_button(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    submit_button = page.locator("button[type='submit']")
    expect(submit_button).to_be_visible()

def test_search_bar_form_present(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    search_form = page.locator("form")
    expect(search_form).to_be_visible()

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

def test_property_card_has_image_placeholder(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    image_placeholder = page.locator(".card-img-top").first
    expect(image_placeholder).to_be_visible()

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