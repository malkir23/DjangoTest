$(function() {
    $('.list-group-sortable-connected').sortable({
        placeholderClass: 'list-group-item',
        connectWith: '.connected'
    });

    $('.list-group-item').mousedown(function () {
        var id = $(this).attr('id');
        var name = $(this).text();
        var text = $(this).attr('title');
        var token = $("input[name=csrfmiddlewaretoken]").val();
        var parent = $(this).parent().attr('id');
        $('.list-group').mouseenter(function () {
            var category = $(this).attr('id');
            if(parent !== category){
                var result = name.replace(/\s+/g,' ' ).replace(/^\s/,'').replace(/\s$/,'').replace(' Edit Delete','');
                $.ajax({
                    type: "POST",
                    url: "work_update/"+id,
                    async:  false,
                    data:{
                        name: result,
                        text: text,
                        category: category.replace('_',' '),
                        csrfmiddlewaretoken: token
                    },
                    success: function() {
                        id = '';
                        name = '';
                        text = '';
                        category = '';
                        parent = '';
                       location.reload();
                    }
                });
            }
        });
    });

/*-----Modal ---------*/
    // function css_modal (){

    //     $('label').addClass('col-form-label');
    //     $('input').addClass('form-control col-sm-4');
    //     $('textarea').addClass('form-control');
    //     $('select').addClass('custom-select col-sm-3');
    //     $('button').addClass('btn btn-primary');
    // }

    $('#add_work').on("click",function (event) {
        var val = "/add_work/";
        $('.modal-body').load(val);
    });

    $('.work_update').on("click",function (event) {
        var val = "work_update/"+ $(this).attr("nomer");
        $('.modal-body').load(val);
    });

    $('.work_delete').on("click",function (event) {
        var val = "work_delete/"+ $(this).attr("nomer");
        $('.modal-body').load(val);
    });

    $('#submit').on('click',function() {
        var urls = $(this).attr("url");
        $.ajax({
            type: "POST",
            url: urls,
            async:  false,
            data: $("form").serialize()
        });
    });
/*----------------------------------------------------------------------------*/
    $('label').addClass('col-form-label');
    $('input').addClass('form-control col-sm-4');
    $('textarea').addClass('form-control');
    $('select').addClass('custom-select col-sm-3');
    $('#submit').addClass('btn btn-primary');
});