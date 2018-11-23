$(function(){
});
layui.use(['element','layer','form','laydate'], function(){
    var element = layui.element,
        layer = layui.layer,
        laydate = layui.laydate,
        form = layui.form;
    //表单验证
    $(".layui-form").Validform({
        tiptype:3,
        ajaxPost:true,
        callback:function(data){
            window.location.href = './index.html';
        }
    });
    form.on('checkbox(allChoose)', function(data){
        var child = $(data.elem).parents('table').find('tbody input[type="checkbox"]');
        child.each(function(index, item){
            item.checked = data.elem.checked;
        });
        form.render('checkbox');
    });
});
