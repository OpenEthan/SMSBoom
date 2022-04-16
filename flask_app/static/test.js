

function getValue() {
    let desc = $("#desc").val();
    let url = $("#url").val();
    let method = $("#method").val();
    let header = $("#header").val();
    let phone = $("#phone").val();
    let data_ = $("#data").val();

    let data = {
        "desc": desc,
        "url": url,
        "method": method,
        "header": header,
        "phone": phone,
        "data": data_
    };

    return data;
};

$(document).ready(function () {



    $("#test").click(function () {

        $.ajax({
            type: "POST",
            url: "/testapi/",
            contentType: "application/json",
            data: JSON.stringify(getValue()),
            dataType: "json",
            success: function (response) {
                if (response.status == 0) {
                    $("#suc").show().text("请求成功!:" + response.resp);
                } else {
                    $("#suc").attr("class", "alert alert-warning").show().text("请求失败!:" + response.resp);
                }
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                $("#error").show().text("发送请求错误请检查后端接口:" + textStatus);
            },
        });

    });

    // console.log(desc, url, method, header);


});