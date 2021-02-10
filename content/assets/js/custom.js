jQuery(function ($) {

    'use strict';
   
    var fileExtension = ['jpeg', 'jpg', 'png', 'gif', 'bmp','avi','mp4'];
    var imgExtension = ['jpeg', 'jpg', 'png', 'gif', 'bmp'];
    var videoExtension = ['avi','mp4'];
    
    var token = $("#meta_csrf input[name='csrfmiddlewaretoken']").val();
    
// ----------------------------------------------------------------
   
    function init_menu()
    {
        var cur_url = window.location.href;      
        console.log(cur_url);
        if (cur_url.indexOf("contract") >= 0)
        {   
            $(".sub_menu_item_contract").addClass("selected_sub_menu");
        }
        else if(cur_url.indexOf("data") >= 0)
        {
            $(".sub_menu_item_data").addClass("selected_sub_menu");
        }
        else if(cur_url.indexOf("ticket") >= 0)
        {
            $(".sub_menu_item_ticket").addClass("selected_sub_menu");
        }
        else if(cur_url.indexOf("payment") >= 0)
        {
            $(".sub_menu_item_checkout").addClass("selected_sub_menu");
            console.log("here");
        }  
        else
        {
            $(".sub_menu_item").removeClass("selected_sub_menu");
        }
    }


    $(document).ready(function(){
    
        init_menu();
    
    });

    // -----------------------Post part-------------------------------
    $(window).scroll(function() {            
    
    });
    $(document).on('click','.alertborder',function(){                
        $(this).removeClass('alertborder');
    });

    $(document).on('click','#btn_store_basic_profile',function(){
        var is_checked = true;
        $('#form_basicinfo .required_form_basicinfo').each(function(){
            if($(this).val()=="")
            {
                $(this).addClass('alert-border');
                is_checked = false;
            }
        });     
       
        if(is_checked)
        {
            var data = $('#form_basicinfo').serialize();
            $("#loading").css("display","block");
            $.ajax({                
                url:"/store_basicinfo",
                type: 'post',
                dataType: 'json',
                data: data,

                success: function(result){                    
                    $("#loading").css("display","none");
                    var data = result.response;
                    if(data.emailcount == '0')
                    {                            
                        swal({
                            title: "Successfully stored!",                     
                            type: "success"
                        }).then(function() {
                            location.reload();
                        });
                    }
                    
                    else if(data.emailcount == '1')
                    {
                        Swal.fire('The email already exsist.Please try another.');
                    }
                    
                
                }
            });
        }            
    });
        
    // ---------------------------Data Part---------------------------------
    
    $(document).on('click','.btn_store_data',function(){
        var is_checked = true;
        $('.new_data_form .required').each(function(){
            if($(this).val()=="")
            {
                $(this).addClass('alert-border');
                is_checked = false;
            }
        });     
       
        if(is_checked)
        {
            var data = $('.new_data_form').serialize();
            $("#loading").css("display","block");
            $.ajax({                
                url:"/data/store",
                type: 'post',
                dataType: 'json',
                data: data,

                success: function(result){                    
                    $("#loading").css("display","none");
                    var data = result.response;
                    if(data)
                    {                            
                        swal({
                            title: "Successfully stored!",                     
                            type: "success"
                        }).then(function() {
                            location.reload();
                        });
                    }
                    else
                    {
                        swal({
                            title: "Something wrong!",                     
                            text: "Please try again",
                            type: "error"
                        }).then(function() {
                            location.reload();
                        });
                    }
                    
                
                }
            });
        }            
    });
});


    
