function http(url, data, method, success, fail) {
    data = method == 'GET' ? data : JSON.stringify(data)
    console.log(data);
    $.ajax({
        url: url,
        type: method,
        dataType: 'json',
        contentType: 'application/json; charset=UTF-8',
        data: data,
        success: success,
        error: fail
    });
}

$(function () {
    var url = 'http://127.0.0.1:8889' + '/api/v1/get_news';
    var data = {
        'page': 0,
    };
    http(url, data, 'GET', function (data) {
        console.log(data);
        $('.news_list').empty();
        var data = data['data'];
        for (var i = 0; i < data.length; i++) {
            var one = "";
            one += '<div>';
            one += '<a href="' + data[i]['url'] + '">';
            one += '<lable>' + data[i]['title'] + '</labal>';
            one += '</a>';
            one += '<p>' + data[i]['authorName'] + '  ' + data[i]['publicTime'] + '</p>';
            if (typeof(data[i]['image']) != "undefined") {
                one += '<img src="' + data[i]['image'] + '" />';
            }
            one += '</div>';
            one += '<hr>';
            $('.news_list').append(one)
        }
    }, function (data) {
        console.log(data)
    })
})