import asyncio
import random
from playwright.async_api import async_playwright

class ScrollAndFollow:
    def __init__(self, page):
        self.page = page

    async def click_follow_buttons(self):
        """Clicks all visible 'Follow' buttons dynamically."""
        try:
            follow_buttons = await self.page.query_selector_all("button:has-text('Follow')")
            for button in follow_buttons:
                if await button.is_visible():
                    await button.click()
                    await asyncio.sleep(random.uniform(1, 3))  # Random delay
        except Exception as e:
            print(f"Error clicking 'Follow' buttons: {e}")

    async def scroll_and_follow(self, max_scrolls=10):
        """Scrolls down the modal and clicks 'Follow' buttons."""
        scroll_count = 0
        modal_selector = "div[role='dialog']"  # Update if necessary
        modal = await self.page.query_selector(modal_selector)

        if not modal:
            print("DEBUG: Modal not found. Check the selector or ensure the modal is loaded.")
            return

        last_height = await self.page.evaluate("(modal) => modal.scrollHeight", modal)

        while scroll_count < max_scrolls:
            await self.click_follow_buttons()
            await self.page.evaluate(
                "(modal) => modal.scrollTo(0, modal.scrollHeight);", modal
            )
            await asyncio.sleep(2)  # Wait for new content to load
            
            new_height = await self.page.evaluate("(modal) => modal.scrollHeight", modal)
            print(f"Last height: {last_height}, New height: {new_height}")

            if new_height == last_height:
                print("No more content to scroll.")
                break
            last_height = new_height
            scroll_count += 1
        
        print(f"Scrolled {scroll_count} times.")

async def main():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)
        
        user_agent_string = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/91.0.4472.124 Safari/537.36"
        )
        
        context = await browser.new_context(
            user_agent=user_agent_string,
            extra_http_headers={"Accept-Language": "en-US,en;q=0.9"}
        )
        
        page = await context.new_page()
        await page.set_viewport_size({"width": 550, "height": 691})

        # Navigate to the profile page and open the followers modal
        await page.goto("https://www.instagram.com/thedesignely/")
        followers_button = await page.wait_for_selector("a[href*='/followers/']", timeout=10000)
        await followers_button.click()

        # Wait for the modal to load
        modal_selector = "div[role='dialog']"  # Update this if necessary
        await page.wait_for_selector(modal_selector, timeout=10000)

        cookies = await context.cookies("https://www.instagram.com/")
        csrf_token = next((cookie["value"] for cookie in cookies if cookie["name"] == "csrftoken"), None)

        if not csrf_token:
            print("CSRF token not found!")
            return

        print(f"Extracted CSRF Token: {csrf_token}")

        await context.add_cookies([
            {'name': 'csrftoken', 'value': csrf_token, 'domain': '.instagram.com', 'path': '/'},
            {'name': 'sessionid', 'value': 'sessionid', 'domain': '.instagram.com', 'path': '/'},
        ])

        scroll_follow = ScrollAndFollow(page)
        await scroll_follow.scroll_and_follow(max_scrolls=20)

        await browser.close()

# Run the asyncio event loop
asyncio.run(main())
