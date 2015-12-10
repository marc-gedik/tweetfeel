var TWITTER_SEARCH_URL = "https://twitter.com/i/search/timeline";

function search(query, rateDelay) {
    url = constructURL(query, null);
    minTweet = null;
    while ((response = executeSearch(url)) != null && continueSearch && !response.getTweets().isEmpty()) {
        if (minTweet == null) {
            minTweet = response.getTweets().get(0).getId();
        }

        maxTweet = response.getTweets().get(response.getTweets().size() - 1).getId();
        if (!minTweet.equals(maxTweet)) {
            Thread.sleep(rateDelay);

            maxPosition = "TWEET-" + maxTweet + "-" + minTweet;
            url = constructURL(query, maxPosition);
        } else {
            break;
        }
    }
}
function executeSearch(url){
$.getJSON(url,
  function (r) {
    console.log(r);
});

}

function constructURL(query, maxPosition) {

    var params = {
        q: query,
        f: "tweets",
    };
    if (maxPosition)
        params.max_position=  maxPosition

    return TWITTER_SEARCH_URL + '?' + jQuery.param(params);
}

