from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_page_title(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}")

    # We look at the <p> tag
    p_tag = page.locator("a")

    # We assert that it has the text "This is the homepage."
    expect(p_tag).to_have_text("makersbnb")

def test_header_available_homes(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}")

    # We look at the <p> tag
    p_tag = page.locator("h2")

    # We assert that it has the text "This is the homepage."
    expect(p_tag).to_have_text("Available Homes")