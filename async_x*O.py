import json
from playwright.async_api import async_playwright
import asyncio
from bs4 import BeautifulSoup
from urllib.parse import urlparse, quote_plus

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"

HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
    "Upgrade-Insecure-Requests": "1",
}

async def fetch_all_posts(url):
    statuses = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent=USER_AGENT, extra_http_headers=HEADERS)
        page = await context.new_page()

        # Navigate to the profile page
        await page.goto(url)
        print("Page loaded. Starting to scroll...")

        previous_height = 0
        retries = 0

        while True:
            # Scroll the page using JavaScript
            await page.evaluate("window.scrollBy(0, document.body.scrollHeight);")
            await asyncio.sleep(5)  # Allow time for content to load

            # Check the new scroll height /// EDITS HERE /// 
            new_height = await page.evaluate("document.body.scrollHeight")
            if new_height == previous_height:
                retries += 1
                if retries > 5:  # Stop after 5 retries if no new content is loaded
                    print("No more posts to fetch.")
                    break
            else:
                retries = 0  # Reset retries if new content is loaded

            previous_height = new_height

            # Extract the HTML content
            content = await page.content()

            # Parse the HTML with BeautifulSoup
            soup = BeautifulSoup(content, 'html.parser')
            post_containers = soup.find_all('div', class_='tweet-container')

            # Process and print new posts
            for post_div in post_containers[len(statuses):]:  # Only process new posts
                try:
                    # Extract post details
                    profile_name = post_div.find('h6', class_='mb-0').text.strip()
                    profile_handle = post_div.find('span').text.strip()
                    timestamp = post_div.find('span', class_='time-stamp').text.strip()
                    tweet_body = post_div.find('div', class_='tweet-body').find('p').text.strip()

                    # Extract tweet statistics
                    footer_div = post_div.find('div', class_='tweet-footer')
                    comments = footer_div.find('i', class_='fa-comment').find_next_sibling('span').text.strip()
                    retweets = footer_div.find('i', class_='fa-retweet').find_next_sibling('span').text.strip()
                    likes = footer_div.find('i', class_='fa-heart').find_next_sibling('span').text.strip()
                    bookmarks = footer_div.find('i', class_='fa-bookmark').find_next_sibling('span').text.strip()
                    views = footer_div.find('i', class_='fa-chart-simple').find_next_sibling('span').text.strip()

                    # Add the post to the list
                    post_data = {
                        "Profile Name": profile_name,
                        "Profile Handle": profile_handle,
                        "Timestamp": timestamp,
                        "Post": tweet_body,
                        "Comments": comments,
                        "Retweets": retweets,
                        "Likes": likes,
                        "Bookmarks": bookmarks,
                        "Views": views,
                    }
                    statuses.append(post_data)

                    # Print the post
                    print(f"New Post Collected:")
                    for key, value in post_data.items():
                        print(f"  {key}: {value}")
                    print()

                except AttributeError as e:
                    print(f"Error parsing a post: {e}")
                    continue

        await browser.close()

    return statuses

def generate_file_name(url):
    """Generate a safe file name based on the URL."""
    parsed_url = urlparse(url)
    path = parsed_url.path.replace("/", "_").strip("_")
    query = quote_plus(parsed_url.query)
    file_name = f"{path}_{query}" if query else path
    return f"{file_name}.json"

async def main():
    url = "https://xstalk.com/search/%F0%9F%87%B3%F0%9F%87%BF"
    posts = await fetch_all_posts(url)
    print(f"\nTotal posts collected: {len(posts)}")

    # Generate a dynamic file name based on the URL
    output_file = generate_file_name(url)

    # Save to JSON file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=4, ensure_ascii=False)
    print(f"Posts saved to {output_file}")

if __name__ == "__main__":
    asyncio.run(main())
