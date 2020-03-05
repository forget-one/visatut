$(document).ready(function() {



  $('.form_consultation').fancybox({
    touch: false,
    scrolling: 'hidden',
   
});


var inputHasFocus = $('.input_focus');
inputHasFocus.on('focus', function() {
  let focusFinder = $(this).parents('.inp-vak-wrap').find('.label__style');
  focusFinder.addClass('label__style_active');
});

inputHasFocus.on('blur', function() {
  if ($(this).val().length < 1 || $(this).val() == '+38(___) __ __ ___') {
      let blurFinder =$(this).parents('.inp-vak-wrap').find('.label__style');
      blurFinder.removeClass('label__style_active');
  }
  
});



if (window.matchMedia("(max-width: 996px)").matches) {
  $('.hidden_name').addClass('hidden_mob');
      var hidden_name = $('.hidden_name a');
    for (var testz = 1; testz <= hidden_name.length; ++testz) {
      var tehas = hidden_name[testz];
     
      add_number = 1 + testz;
      var dinamic_id = '#sect' + add_number;
      $(tehas).attr('href', dinamic_id);
    }

}




$('.one-time').slick({
  dots: true,
  infinite: false,
  speed: 300,
  slidesToShow: 1,
  adaptiveHeight: true,
  // autoplay: true,
  lazyLoad: "string",
});



var doFullpage = document.documentElement.clientWidth;
if (doFullpage > 996) {
  $('#fullpage').fullpage({
    //options here
    autoScrolling: true,
    scrollHorizontally: true,
      // scrollOverflow: true,
    navigation: true,
    normalScrollElements: '.normalScroll',
    slidesNavigation: false,
    anchors: ['firstPage', 'secondPage', '3thPage', '4thpage', '5thpage', '6thpage', '7thpage'],
  
  });
}

// psevdo ====================================================>


console.log(localStorage.psevdo_link);
if (window.location.pathname == "/C:/Users/odmin/Desktop/visaTUT/index.html") {
  if (localStorage.psevdo_link != 0) {
    if (window.matchMedia("(max-width: 996px)").matches) {
    function linkTime() {
      let destination = $('#sect' + localStorage.psevdo_link).offset().top;
      $('html, body').animate({ scrollTop: destination }, 600);
      return false;
    }
    setTimeout(linkTime, 500);
    } else {
      fullpage_api . moveTo (localStorage.psevdo_link);
    }
  
  }
}

$('.psevdo_link').on("click", function() {
  localStorage.setItem('psevdo_link', '0');
  let psevdo_class = $(this).data('index');
 
  localStorage.psevdo_link = psevdo_class;
  window.location.pathname = '/C:/Users/odmin/Desktop/visaTUT/index.html';
});


// psevdo ====================================================>







$('.nav_name_link').on('click', function() {
    let data_scheme = $(this).data('scheme');
  
    if (data_scheme == 1) {
      window.location.pathname = '/C:/Users/odmin/Desktop/visaTUT/index.html';
      localStorage.scheme = 1;
    } else if (data_scheme > 10 && data_scheme < 100) {
      localStorage.scheme = data_scheme;
      console.log('localStorage.scheme: ', localStorage.scheme);
      window.location.pathname = '/C:/Users/odmin/Desktop/visaTUT/index.html';
    }
});

if (window.location.pathname == "/C:/Users/odmin/Desktop/visaTUT/index.html" && localStorage.scheme != 0 && localStorage.scheme != 1) {
  

  if (window.matchMedia("(max-width: 996px)").matches) {
    function linkTime() {
      let destination = $('#sect2').offset().top;
      $('html, body').animate({ scrollTop: destination }, 600);
      return false;
    }
    setTimeout(linkTime, 500);
    } else {
      fullpage_api.moveSectionDown();
    }

  add_visible_content();
 
}
if (window.location.pathname == "/C:/Users/odmin/Desktop/visaTUT/index.html" && localStorage.scheme == 1) {
  if (window.matchMedia("(max-width: 996px)").matches) {
    function linkTime() {
      let destination = $('#sect2').offset().top;
      $('html, body').animate({ scrollTop: destination }, 600);
      return false;
    }
    setTimeout(linkTime, 500);
    } else {
      fullpage_api.moveSectionDown();
    }
}

function add_visible_content () {
  let find_content = $('.hidden_tab_content').find('.content' + localStorage.scheme);
  

  let default_content = $('.sect2 .default-block .default-content');
  let default_image = $('.sect2 .default-block .default-image');
  let hidden_tab_content = $('.hidden_tab_content');
  let services_block = $('.services-block');
  default_content.addClass('default-content_active');
  default_image.addClass('default-image_active');
  hidden_tab_content.addClass('hidden_tab_content_active');
  services_block.addClass('services-block_active');

  find_content.addClass('info-content_active');

  localStorage.setItem('scheme', '0');
}


$('.header-button').on('click', function() {




  let data_btn = $(this).data('btn');
  console.log('data_btn: ', data_btn);
  localStorage.scheme = data_btn;
  
  if (window.matchMedia("(max-width: 996px)").matches) {
    function linkTime() {
      let destination = $('#sect' + 2).offset().top;
      $('html, body').animate({ scrollTop: destination }, 600);
      return false;
    }
    setTimeout(linkTime, 500);
    } else {
      fullpage_api . moveTo (2);
    }

    add_visible_content();
});







localStorage.setItem('scheme', '0');
localStorage.setItem('psevdo_link', '0');






























$.extend($.lazyLoadXT, {
    edgeY:  250,
    srcAttr: 'data-src'
  });


  // if (window.matchMedia("(min-width: 996px)").matches) {
  
  // } else {
  //   $('.hidden_name').addClass('scroll_all');
  // }

 




  $(".services-prof").click(function (){
    let page_info = $(this).data("info");
    let content_info = $("#"+page_info);
    let default_content = $('.sect2 .default-block .default-content');
    let default_image = $('.sect2 .default-block .default-image');
    let hidden_tab_content = $('.hidden_tab_content');
    let services_block = $('.services-block');
    default_content.addClass('default-content_active')
    default_image.addClass('default-image_active')
    hidden_tab_content.addClass('hidden_tab_content_active')
    content_info.addClass('info-content_active')
    services_block.addClass('services-block_active')
  });

  $(".close-btn").click(function (){
    let default_content = $('.sect2 .default-block .default-content');
    let default_image = $('.sect2 .default-block .default-image');
    let hidden_tab_content = $('.hidden_tab_content');
    let services_block = $('.services-block');
    default_content.removeClass('default-content_active');
    default_image.removeClass('default-image_active');
    hidden_tab_content.removeClass('hidden_tab_content_active');
    $('.info-content').removeClass('info-content_active');
    services_block.removeClass('services-block_active');
  });

  function removeModalServices() {
    let default_content = $('.sect2 .default-block .default-content');
    let default_image = $('.sect2 .default-block .default-image');
    let hidden_tab_content = $('.hidden_tab_content');
    let services_block = $('.services-block');
    default_content.removeClass('default-content_active');
    default_image.removeClass('default-image_active');
    hidden_tab_content.removeClass('hidden_tab_content_active');
    $('.info-content').removeClass('info-content_active');
    services_block.removeClass('services-block_active');
  }

  $(".ham").click(function (){
      $('.nav-bar').toggleClass('nav-bar_active');
      $('.onepage-pagination').toggleClass('onepage-pagination_active');
      $('.hidden_nav-bar').toggleClass('hidden_nav-bar_active');
      $('.sociate-block').toggleClass('sociate-block_active');
      $('.info_top-block_desktopNone').toggleClass('info_top-block_desktopNone_active');
      $('.main_nav_bar_for_mobile').toggleClass('main_nav_bar_for_mobile_active');
 
      if ($(this).hasClass('active')) {
        $("html,body").css("overflow", "hidden");
      } else {
          $("html,body").css("overflow", "visible");
    
      }
 
    

    });

    $(".hidden_name").click(function (){
      $('.nav-bar').removeClass('nav-bar_active');
      $('.onepage-pagination').removeClass('onepage-pagination_active');
      $('.hidden_nav-bar').removeClass('hidden_nav-bar_active');
      $('.sociate-block').removeClass('sociate-block_active');
      $('.info_top-block_desktopNone').removeClass('info_top-block_desktopNone_active');
      $('.main_nav_bar_for_mobile').removeClass('main_nav_bar_for_mobile_active');
      $('.ham').removeClass('active');

      if (window.matchMedia("(max-width: 996px)").matches) {
        if ($('.hidden_mob').hasClass('active')) {
          $("html,body").css("overflow", "hidden");
        } else {
            $("html,body").css("overflow", "visible");
      
        }
      }
 
    });
    

    $(".nav_name").click(function (){
      let page_info = $(this).data("nav");
     
        if (page_info == "nav1") {
            removeModalServices();
        }
    });



    $(".scroll_all").on('click', function () {
      event.preventDefault();

      var elementClick = $(this).attr("href");
      // console.log(elementClick);
    
      var destination = $(elementClick).offset().top;
      var destContacts = (destination - 600)
      $('html, body').animate({ scrollTop: destination }, 600);
      console.log(destContacts);
      return false;
      

  });




  $('.select__input').on('click', function(){
   
    let fieldt = $(this).parents('.select').find(".select__wrap");
    $('.select__wrap').removeClass('select__wrap_active');
    //   $('.field').removeClass('field-active');
    $('.field__icon').removeClass('field__icon_active');
    
    fieldt.toggleClass('select__wrap_active');
    $('.field__icon', this).toggleClass('field__icon_active');


    if ($(this).hasClass('select__input_active')) {
        
        $('.select__wrap').removeClass('select__wrap_active');
        $('.field__icon').removeClass('field__icon_active');
          $(this).removeClass('select__input_active');
    } else {
        $('.select__input').removeClass('select__input_active');
        $(this).addClass('select__input_active');
    }


   
});

$(document).mouseup(function(e) {
    var select = $(e.target).parents('.select'); // тут указываем класс элемента
    let finder_visual = select.find('.select__input').find('.visual_label');
    let finder_select = select.find('.select__input');
   

    if (select.length > 0) {} else {
        $('.select__wrap').removeClass('select__wrap_active');
        //   $('.field').removeClass('field-active');
        $('.field__icon').removeClass('field__icon_active');
        $('.select__input').removeClass('select__input_active');
        
    
     
    
        // if ($(finder_field)[0].outerText == "") {
        //   finder_visual.removeClass('visual_label_active');
        //   finder_select.removeClass('select__input_activate');
        // }
        //  } else if ($(finder_field)[0].outerText != "") {
        //   finder_visual.addClass('visual_label_active');
        //   finder_select.addClass('select__input_activate');
        //  }
      }

      var form_input1 = $('.services_form').find('.select__input1').find('.field_text1');
      var form_input2 = $('.services_form').find('.select__input2').find('.field_text2');
      var form_input3 = $('.services_form').find('.select__input3').find('.field_text3');
      var form_input4 = $('.services_form').find('.select__input4').find('.field_text4');

      
        if (form_input1[0].outerText == '') {
          console.log(form_input1[0].outerText);
          $('.services_form').find('.select__input1').removeClass('visual_label_active');
          $('.select__input1').removeClass('select__input_activate');
          } else if (form_input1[0].outerText != '') {
            $('.services_form').find('.select__input1').addClass('visual_label_active');
            $('.select__input1').addClass('select__input_activate');
          }
        if (form_input2[0].outerText == '') {
          $('.services_form').find('.select__input2').removeClass('visual_label_active');
          $('.select__input2').removeClass('select__input_activate');
          } else if (form_input2[0].outerText != '') {
            $('.services_form').find('.select__input2').addClass('visual_label_active');
            $('.select__input2').addClass('select__input_activate');
          }
        if (form_input3[0].outerText == '') {
          $('.services_form').find('.select__input3').removeClass('visual_label_active');
          $('.select__input3').removeClass('select__input_activate');
          } else if (form_input3[0].outerText != '') {
            $('.services_form').find('.select__input3').addClass('visual_label_active');
            $('.select__input3').addClass('select__input_activate');
          }
        if (form_input4[0].outerText == '') {
          $('.services_form').find('.select__input4').removeClass('visual_label_active');
          $('.select__input4').removeClass('select__input_activate');
          } else if (form_input4[0].outerText != '') {
            $('.services_form').find('.select__input4').addClass('visual_label_active');
            $('.select__input4').addClass('select__input_activate');
          }
         

      
        
        
      
 
   
    });




$('.select__wrap_item').on('click', function() {
    var text = $(this).text();
    var id = $(this).data('id');
    
    let field = $(this).parents('.select__wrap').parents('.select').find(".field_text");
    let input_select = $(this).parents('.select').find("input");
    $(field).text(text);
    $(input_select).val(id);
    
    field.attr('data-countries', id)
   
    let engineType = $(this).parents('.select__wrap').parents('.select').find(".field_text");
    engineType.attr('data-engineType', id);

    let engineYear = $(this).parents('.select__wrap').parents('.select').find(".field_text");
    engineYear.attr('data-year', id)
    
    $('.select__wrap').removeClass('select__wrap_active');
    $('.select__input').removeClass('select__input_active');
    $('.field__icon').removeClass('field__icon_active');
    // $('.select__input').removeClass('select__input-active');

    let field_label = $(this).parents('.select__wrap').parents('.select').find('.visual_label');
    let field_input = $(this).parents('.select__wrap').parents('.select').find('.select__input');

    field_label.addClass('visual_label_active');
    field_input.addClass('select__input_activate');
    
  })
  



  $('.select__input').on('click', function() {

    let visual_label = $(this).find('.visual_label');


      $(this).addClass('select__input_activate');
      visual_label.addClass('visual_label_active');

     
     
  });










});