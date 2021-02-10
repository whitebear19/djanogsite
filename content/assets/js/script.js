function readURL(input, target) {
  if (input.files && input.files[0]) {
    var fileType = input.files[0].type;
    if (
      fileType == 'image/jpg' ||
      fileType == 'image/jpeg' ||
      fileType == 'image/png'
    ) {
      var reader = new FileReader();
      reader.onload = function (e) {
        $(target).attr('src', e.target.result);
        var removeBtn = $('.btn-file-remove');
        var imagePreview = $('.image-preview');
        if (removeBtn.length > 0) {
          removeBtn.show();
        }
        if (imagePreview.length > 0) {
          imagePreview.show();
        }
      };
      reader.readAsDataURL(input.files[0]);
    } else {
      alert('Only jpg/jpeg and png files are allowed!');
    }
  }
}
$(window).on('load', function () {
  'use strict';

  $(
    '.chat-list,.messages-line, .suggestions-inner, .nott-list .nott-inner, .pf-gallery, .custom-invite-list, .jobs-list-inner, .messages-list'
  ).mCustomScrollbar({
    axis: 'y',
    theme: 'dark',
    integer: 100,
    setLeft: 0,
    scrollbarPosition: 'inside',
  });

  $('.skill-tags').mCustomScrollbar({
    axis: 'x',
    theme: 'dark',
    integer: 100,
    setLeft: 0,
    scrollbarPosition: 'outside',
  });

  
  
  var windowWidth = $(window).width();
  
    $(window).scroll(function () {
      
      windowWidth = $(window).width();
      if (windowWidth > 1200) {
        if ($(window).scrollTop() >= 86){
          $('.left-sidebar-fixed').css({
            'width': Math.round($('.col-lg-3.col-md-4.pd-left-none').width()) + 'px',
            'position': 'fixed',
            'top': '60px',
          });
          $('.right-sidebar-fixed').css({
            'width': Math.round($('.col-lg-3.col-md-4.pd-left-none').width()) + 'px',
            'position': 'fixed',
            'top': '60px',
          });
        } else{
            $('.left-sidebar-fixed, .right-sidebar-fixed').css({
                'position': '',
                'width': '',
                'top': '',
            });
        }
      }
      else
      {
        $('.left-sidebar-fixed, .right-sidebar-fixed').css({
          'position': '',
          'width': '',
          'top': '',
        });
      }
    });
  
  
  // custom area
  $(
    '.left-sidebar-fixed,.right-sidebar-fixed'
  ).mCustomScrollbar({
    axis: 'y',
    theme: 'dark',
    integer: 100,
    setLeft: 0,
    scrollbarPosition: 'inside',
  });
  
  // end custom area
  //  ============= SIGNIN SWITCH TAB FUNCTIONALITY =========

  $('.tab-feed ul li').on('click', function () {
    var tab_id = $(this).attr('data-tab');
    $('.tab-feed ul li').removeClass('active');
    $('.product-feed-tab').removeClass('current');
    $(this).addClass('active animated fadeIn');
    $('#' + tab_id).addClass('current animated fadeIn');
    return false;
  });

  //  ============= OVERVIEW EDIT FUNCTION =========

  // $('.overview-open').on('click', function () {
  //   $('#overview-box').addClass('open');
  //   $('.wrapper').addClass('overlay');
  //   return false;
  // });
  // $('.close-box').on('click', function () {
  //   $('#overview-box').removeClass('open');
  //   $('.wrapper').removeClass('overlay');
  //   return false;
  // });

  //  ============= EXPERIENCE EDIT FUNCTION =========

  $('.exp-bx-open').on('click', function () {
    $('#experience-box').addClass('open');
    $('.wrapper').addClass('overlay');
    return false;
  });
  $('.close-box').on('click', function () {
    $('#experience-box').removeClass('open');
    $('.wrapper').removeClass('overlay');
    return false;
  });

  //  ============= EDUCATION EDIT FUNCTION =========

  $('.ed-box-open').on('click', function () {
    $('#education-box').addClass('open');
    $('.wrapper').addClass('overlay');
    return false;
  });
  $('.close-box').on('click', function () {
    $('#education-box').removeClass('open');
    $('.wrapper').removeClass('overlay');
    return false;
  });

  //  ============= LOCATION EDIT FUNCTION =========

  $('.lct-box-open').on('click', function () {
    $('#location-box').addClass('open');
    $('.wrapper').addClass('overlay');
    return false;
  });
  $('.close-box').on('click', function () {
    $('#location-box').removeClass('open');
    $('.wrapper').removeClass('overlay');
    return false;
  });

  //  ============= SKILLS EDIT FUNCTION =========

  $('.skills-open').on('click', function () {
    $('#skills-box').addClass('open');
    $('.wrapper').addClass('overlay');
    return false;
  });
  $('.close-box').on('click', function () {
    $('#skills-box').removeClass('open');
    $('.wrapper').removeClass('overlay');
    return false;
  });

  //  ============= Post Image Sider =========

  $('.post-slider').owlCarousel({
    items: 1,
    nav: true,
    dots: false,
    loop: false,
    margin: 50,
    smartSpeed: 1200,
    touchDrag: false,
    mouseDrag : false,
    navText : ["<i class='fas fa-chevron-left'></i>","<i class='fas fa-chevron-right'></i>"]
  });

  //  ============= ESTABLISH EDIT FUNCTION =========

  $('.esp-bx-open').on('click', function () {
    $('#establish-box').addClass('open');
    $('.wrapper').addClass('overlay');
    return false;
  });
  $('.close-box').on('click', function () {
    $('#establish-box').removeClass('open');
    $('.wrapper').removeClass('overlay');
    return false;
  });

  //  ============= CREATE PORTFOLIO FUNCTION =========

  $('.portfolio-btn > a').on('click', function () {
    $('#create-portfolio').addClass('open');
    $('.wrapper').addClass('overlay');
    return false;
  });
  $('.close-box').on('click', function () {
    $('#create-portfolio').removeClass('open');
    $('.wrapper').removeClass('overlay');
    return false;
  });

  //  ============= EMPLOYEE EDIT FUNCTION =========

  $('.emp-open').on('click', function () {
    $('#total-employes').addClass('open');
    $('.wrapper').addClass('overlay');
    return false;
  });
  $('.close-box').on('click', function () {
    $('#total-employes').removeClass('open');
    $('.wrapper').removeClass('overlay');
    return false;
  });

  //  =============== Ask a Question Popup ============

  $('.ask-question').on('click', function () {
    $('#question-box').addClass('open');
    $('.wrapper').addClass('overlay');
    return false;
  });
  $('.close-box').on('click', function () {
    $('#question-box').removeClass('open');
    $('.wrapper').removeClass('overlay');
    return false;
  });

  //  ============== ChatBox ==============

  $('.chat-mg').on('click', function () {
    $(this).next('.conversation-box').toggleClass('active');
    return false;
  });
  $('.close-chat').on('click', function () {
    $('.conversation-box').removeClass('active');
    return false;
  });

  //  ================== Edit Options Function =================

  $('.ed-opts-open').on('click', function () {
    $(this).next('.ed-options').toggleClass('active');
    return false;
  });

  // ============== Menu Script =============

  $('.menu-btn > a').on('click', function () {
    $('nav').toggleClass('active');
    return false;
  });

  //  ============ Notifications Open =============

  $('.not-box-open').on('click', function () {
    $('#message').hide();
    $('.user-account-settingss').hide();
    $(this).next('#notification').toggle();
  });

  //  ============ Messages Open =============

  $('.not-box-openm').on('click', function () {
    $('#notification').hide();
    $('.user-account-settingss').hide();
    $(this).next('#message').toggle();
  });

  // ============= User Account Setting Open ===========

  $('.user-info').click(function () {
    $('.user-account-settingss').slideToggle('fast');
    $('#message').not($(this).next('#message')).slideUp();
    $('#notification').not($(this).next('#notification')).slideUp();
    // Animation complete.
  });

  //  ============= FORUM LINKS MOBILE MENU FUNCTION =========

  $('.forum-links-btn > a').on('click', function () {
    $('.forum-links').toggleClass('active');
    return false;
  });
  $('html').on('click', function () {
    $('.forum-links').removeClass('active');
  });
  $('.forum-links-btn > a, .forum-links').on('click', function () {
    e.stopPropagation();
  });
  //  ============= Group Image Picker and Remove  =========
  $('.image-picker input[type="file"]').change(function () {
    readURL(this, '.image-picker img');
  });

  $('.image-picker .btn-file-remove').click(function () {
    $('.image-picker img').attr('src', '').hide();
    $(this).hide();
    $('.image-picker input[type="file"]').val('');
  });
  //  ============= Invite People custom to open modal popup  =========
  $('input[type=radio][name=invite]').change(function () {
    if (this.value == 'custom') {
      $('.btn-custom-invite').trigger('click');
    }
  });
  //  ============= Invite People custom to open modal popup  =========
  $('.jobs-view .btn').click(function () {
    $('.jobs-view .btn').removeClass('active');
    $(this).addClass('active');
    var view = $(this).data('value');
    if(view === 'list'){
      $('#jobs-listing').removeClass('show-grid').addClass('show-list');
    }else if(view === 'grid'){
      $('#jobs-listing').removeClass('show-list').addClass('show-grid');
    }else{
      $('#jobs-listing').removeClass('show-grid show-list');
    }
  });
  //  ============= post image and video modal popup  =========
  $('.post-slider .embed-responsive-item').click(function(e){
    e.preventDefault();
    var url = $(this).data('url');
    console.log(url);
    if(url){
      var arr = [ "jpeg", "jpg", "gif", "png" ];
      var ext = url.substring(url.lastIndexOf(".")+1);
      if(arr.some(e => e === ext)){
        $('#post-image-media').attr('src', url).show();
        $('#post-video-media').attr('src', '').hide();
      }else{
        $('#post-video-media').attr('src', url).show();
        $('#post-image-media').attr('src', '').hide();
      }
      $('.btn-post-media-modal').trigger('click');
    }
  });
  $('.post-media-modal').on('hide.bs.modal', function(e) {
    var $v = $(e.delegateTarget).find('video');
    $v[0].pause();
  });
  //  ============= Gallery image modal popup  =========
  $('.btn-gallery-view').click(function(e){
    e.preventDefault();
    var url = $(this).data('url');
    var id = $(this).data('id');
    
    if(url){
      $('#post-image-media').attr('src', url).show();
      $('.btn-gallery-modal').trigger('click');
      $('.btn_modal_attach_delete').attr('data-id',id);
    }
  });
});
