// // var data=3.1415926
// var data={
//     'name':'jason',
//     'age':18,
// }
// console.log(data)
// console.log(JSON.parse('{"key1":3.1415926,"key2":"key1的值是π！"}'))
// console.log(JSON.stringify(data))
// console.log('Python测试开发')

// 条件语句
data = 0
if (data > 0) {
    console.log('正数')
}
else if (data == 0) {
    console.log('0')
}
else {
    console.log('负数')
}
// 循环语句
for (i = 0; i < 10; i++) {
    console.log(i)
}

// 排序
data = [2, 4, 1, 8, 5, 3, 6, 9, 7]
// data.sort()
// console.log(data)
function sort() {
    len = data.length
    for (i = 0; i < len; i++) {
        for (j = 0; j < len - 1 - i; j++) {
            if (data[j] > data[j + 1]) {
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp
            }
        }
    }
    return data
}

console.log(sort(data))

// 裴波那切
function fibonacci(n) {
    if (n == 0 || n == 1) {
        return n
    }
    return fibonacci(n - 1) + fibonacci(n - 2)
}

//  阶乘  n！
function jiecheng(n) {
    if (n == 0 || n == 1) {
        return 1
    }
    return n * jiecheng(n - 1)
}

console.log(jiecheng(3));
// jQuery应用
function http(url, data, method, success, fail) {
    data = method == 'GET' ? data : JSON.stringify(data);
    console.log(data);
    $.ajax({
    url: url,
    type: method,
    dataType: 'json',
    contentType: 'application/json; charset=UTF-8', data: data,
    success: success,
    error: fail
    }); }


var expression = '';
$(function () {
    $('.control').click(function () {
            value = $(this).text();
            expression += value;
            $('label').text(expression)
        }
    );
    $('.number').click(function () {
        value = $(this).text();
        expression += value;
        $('label').text(expression)
    });
    $('#clear').click(function () {
        expression = '';
        $('label').text('0')
    });
    $('#eval').click(function () {
        var url = "http://127.0.0.1:8889/evaluation";
        var data ={
            'expression':expression
        };
        http(url,data,'GET',function (data) {
            console.log(data);
            expression = data['data'];
            $('label').text(data['data'])
        },function (data) {
            console.log(data)

        })
    });

    console.log('这是js程序入口')
});