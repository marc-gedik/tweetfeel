var words = [];

setInterval(function () {
    $("#cloud").empty()
    $('#cloud').jQCloud(words.slice(0, 100), {delayedMode: false});
}, 1000 * 10)

var pieChartData

function resetPieChartData() {
    pieChartData = [
        ['Sentiment', 'Analyze'],
        ['Positive', 0],
        ['Negative', 0],
        ['Neutre', 0]
    ]
}

function drawPie() {
    var data = google.visualization.arrayToDataTable(pieChartData);
    var options = {
        slices: {
            0: {color: '#9DD5C0'},
            1: {color: '#F1646C'},
            2: {color: '#F4F4F4'}
        }
    };
    var chart = new google.visualization.PieChart(document.getElementById('piechart'));
    chart.draw(data, options);
}

var positivesChart
function resetPositivesChart() {
    positivesChart = [
        ["Degree", "Number", {role: "style"}],
        ["=D", 0, "color: #4caf50"],
        [":D", 0, "color: #66bb6a"],
        [":)", 0, "color: #81c784"],
        [".", 0, "color: #a5d6a7"],
        [".", 0, "color: #c8e6c9"],
        [".", 0, "color: #e8f5e9"]
    ]
}
function drawPositives() {
    drawChart(positivesChart, 'positives')
}

var negativesChart
function resetNegativesChart() {
    negativesChart = [
        ["Degree", "Number", {role: "style"}],
        ["è_é", 0, "color: #f44336"],
        ["..", 0, "color: #ef5350"],
        ["..", 0, "color: #e57373"],
        ["..", 0, "color: #ef9a9a"],
        ["..", 0, "color: #ffcdd2"],
        [":(", 0, "color: #ffebee"]
    ]
}
function drawChart(data, div) {
    var data = google.visualization.arrayToDataTable(data);
    var options = {legend: {position: 'none'}};
    var chart = new google.visualization.ColumnChart(
        document.getElementById(div));
    chart.draw(data, options);
}


function addTweet(text, sentiment, degree) {
    if (sentiment > 0) {
        div = '<div class= "card-content green lighten-' + degree + '">';
        positivesChart[degree + 1][1] += 1
    }
    else if (sentiment < 0) {
        div = '<div class= "card-content red lighten-' + degree + '">';
        negativesChart[degree + 1][1] += 1
    }
    else
        div = '<div class= "card-content"> '
    $("#tweets").append('<div class="card"> ' + div + text + '</div></div>')
}

function addTweets(tweets) {
    tweets.forEach(function (tweet) {
        addTweet(tweet.tweet, tweet.sentiment, tweet.degree)
    });
}

var intervalId
var minTweet = 0
var maxTweet = 0
var success = true
$(document).ready(function () {
    $("form").submit(function (event) {
        $("#fetch").show()

        resetPieChartData();
        resetNegativesChart();
        resetPositivesChart();
        words = [];
        $("#tweets").empty();
        var $this = $(this);
        event.preventDefault();
        stop()
        success = true
        intervalId = setInterval(function () {

            if (success) {
                success = false
                $.ajax({
                    url: $this.attr('action'),
                    type: $this.attr('method'),
                    data: 'search=' + $('#search').val()
                    + '&min=' + minTweet
                    + '&max=' + maxTweet
                    + "&lang=" + lang,
                    success: function (data) {
                        $("#fetch").hide()

                        success = true
                        if (data.search == $("#search").val()) {

                            pieChartData[1][1] += data.pos;
                            pieChartData[2][1] += data.neg;
                            pieChartData[3][1] += data.neutre;

                            minTweet = data.min;
                            maxTweet = data.max;

                            addTweets(data.tweets);

                            drawPie();
                            drawChart(positivesChart, 'positivesChart');
                            drawChart(negativesChart, 'negativesChart');

                            merge(data.wordFrequencies);

                        }
                    },
                    error: function () {
                        $("#fetch").hide()
                        stop()
                    }
                });
            }
        }, 1000 * .5);
    })
});

function merge(array) {
    for (i = 0; i < words.length; i++)
        for (j = 0; j < array.length; j++)
            if (words[i].text == array[j].text) {
                words[i].weight += array[j].weight;
                array.splice(j, 1);
            }
    array.forEach(function (freq) {
        words.push(freq)
    })
    words.sort(function (a, b) {
        return b.weight - a.weight
    })
}

function stop() {
    clearInterval(intervalId)
}

