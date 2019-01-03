
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

//添加header输入
function add_headers() {
    var html = '<div>key:<input class="header-key"/>value:<input class="header-value"/><input class="del" type="button" value="DEL" style="margin-left: 10px"/></div>';
    $('#add_headers').append(html);
    $('#add_headers').show()
    $('.del').click(del_click)
}

//添加param输入
function add_params() {
    var html = '<div>key:<input class="params-key"/>value:<input class="params-value"/><input class="del" type="button" value="DEL" style="margin-left: 10px"/></div>';
    $('#add_params').append(html);
    $('#add_params').show()
    $('.del').click(del_click)
}

function del_click() {
    $(this).parent().remove()
}
//获取输入的headers数据
function get_headers() {
    var data = {};
    // $.each($('.header-key'), function (index, value) {
    //     var key = $('.header-key').eq(index).val();
    //     var value = $('.header-value').eq(index).val();
    //     data[key] = value
    // });
    $('.header-key').each(function (i, val) {
        var key = $('.header-key').eq(i).val();
        var value = $('.header-value').eq(i).val();
        data[key] = value
    });
    return data

}
//获取输入的params数据
function get_params() {
    var data = {};
    // $.each($('.params-key'), function (index, value) {
    //     var key = $('.params-key').eq(index).val();
    //     var value = $('.params-value').eq(index).val();
    //     data[key] = value
    // });
    $('.params-key').each(function (i, val) {
        var key = $('.params-key').eq(i).val();
        var value = $('.params-value').eq(i).val();
        data[key] = value
    });
    return data
}
function debug_click() {
    var url = "http://127.0.0.1:8888/accept";
    var data = {
        'method': $('#method').val(),
        'url': $('#url').val(),
        'headers': get_headers(),
        'params': get_params()
    };
    var method = "POST";
    http(url, data, method, function (data) {
        console.log(data)
    }, function (data) {
        console.log(data)
    })
    }


$(function () {
        $('#add_headers').hide();
        $('#add_params').hide();
        $('#header').click(add_headers);
        $('#param').click(add_params);
        $('#debug').click(debug_click)
})