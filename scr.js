(function() {
    let extractedPosts = [];

    function extractContent() {
        const posts = document.querySelectorAll('article');

        posts.forEach(post => {
            // Extract the tweet's text content
            const tweetContentElement = post.querySelector('div[data-testid="tweetText"]');
            const tweetText = tweetContentElement ? tweetContentElement.innerText.trim() : null;

            // Extract the user's name
            const userNameElement = post.querySelector('div[data-testid="User-Name"] span.css-1jxf684');
            const userName = userNameElement ? userNameElement.innerText.trim() : null;

            // Extract the user's handle (username)
            const userHandleElement = post.querySelector('div[data-testid="User-Name"] span.css-1jxf684.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3');
            let userHandle = userHandleElement ? userHandleElement.innerText.trim() : null;
            if (userHandle && !userHandle.startsWith('@')) {
                userHandle = `@${userHandle}`; // Add "@" to the user handle if missing
            }

            // Extract the timestamp of the tweet
            const timeElement = post.querySelector('time');
            const time = timeElement ? timeElement.getAttribute('datetime') : null;

            // Extract the href from the <a> tag containing the status (tweet) link
            const linkElement = post.querySelector('a[href*="/status/"]');
            const tweetHref = linkElement ? linkElement.getAttribute('href') : null;

            // Extract tweet ID from the href (assuming the ID is the last part of the href)
            const tweetId = tweetHref ? tweetHref.split('/').pop() : null;

            // Extract the number of likes, reposts, bookmarks, and views from the aria-label
            const ariaLabel = post.querySelector('div[aria-label*="likes"]');
            let likes = 0, reposts = 0, bookmarks = 0, views = 0;

            if (ariaLabel) {
                const ariaText = ariaLabel.getAttribute('aria-label');
                const matches = ariaText.match(/(\d+) reposts.*?(\d+) likes.*?(\d+) bookmarks.*?(\d+) views/);

                if (matches) {
                    reposts = parseInt(matches[1], 10);
                    likes = parseInt(matches[2], 10);
                    bookmarks = parseInt(matches[3], 10);
                    views = parseInt(matches[4], 10);
                }
            }

            // If all necessary data is available, store it in the extractedPosts array
            if (tweetText && userName && time && tweetId && userHandle) {
                extractedPosts.push({
                    tweet_id: tweetId,
                    user_name: userName,
                    user_handle: userHandle,
                    tweet: tweetText,
                    time: time,
                    tweet_link: tweetHref,
                    likes: likes,
                    reposts: reposts,
                    bookmarks: bookmarks,
                    views: views
                });
                console.log('Extracted Post:', tweetText);
            }
        });
    }

    // Set up a MutationObserver to monitor changes in the timeline and run extractContent whenever new content is loaded
    const observer = new MutationObserver(extractContent);
    observer.observe(document.body, { childList: true, subtree: true });

    // Function to stop the MutationObserver, halting the collection of new posts
    function stopCollectingPosts() {
        observer.disconnect();
        console.log('Stopped collecting posts.');
    }

    // Function to export the collected posts as a JSON file
    window.exportPostsAsJSON = function() {
        const dataStr = JSON.stringify(extractedPosts, null, 2);
        const dataUri = 'data:application/json;charset=utf-8,' + encodeURIComponent(dataStr);

        const exportFileDefaultName = 'extracted_posts.json';

        const linkElement = document.createElement('a');
        linkElement.setAttribute('href', dataUri);
        linkElement.setAttribute('download', exportFileDefaultName);
        document.body.appendChild(linkElement);
        linkElement.click();
        document.body.removeChild(linkElement);

        console.log("Autosaved JSON at:", new Date().toISOString());
    };

    // Autosave JSON every 2 minutes
    const autosaveInterval = setInterval(window.exportPostsAsJSON, 2 * 60 * 1000);

    // Function to stop the autosave interval
    function stopAutosave() {
        clearInterval(autosaveInterval);
        console.log("Autosave stopped.");
    }

    // Log a message to the console to inform the user that the script is running
    console.log("Monitoring timeline for new posts with structured data extraction. Autosave enabled. To stop collecting, run 'stopCollectingPosts()' in the console. To stop autosave, run 'stopAutosave()'.");

    // Expose the stopCollectingPosts and stopAutosave functions to the global scope
    window.stopCollectingPosts = stopCollectingPosts;
    window.stopAutosave = stopAutosave;
})();
