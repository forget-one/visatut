$(document).ready(function() {

    $('.mobile_mask').mask("+38(999) 99 99 999");
    $('.form_consultation').fancybox({
      touch: false,
      scrolling: 'hidden',
  });
  
  
  if ($('.main_blog-block').length >= 1) {
    let length_prof = $('.main_blog-block .blog-prof').length;
    if (length_prof > 3) {
      $('.main_blog-block').addClass('normalScroll');
    }
  }
  
  
  
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
    lazyLoad: "ondemand",
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
  
  
  console.log('window.location.pathname: ', window.location.pathname);
  if (window.location.pathname == "/") {
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
    window.location.pathname = '/';
  });
  
  
  // psevdo ====================================================>
  
  
  
  
  
  
  
  $('.nav_name_link').on('click', function() {
      localStorage.setItem('finder_page', '1');
      let data_scheme = $(this).data('scheme');
      console.log('data_scheme: ', data_scheme);
      let nav_name_first = $('.nav_name_first').data('scheme');
     
      if (data_scheme == nav_name_first) {
       
        console.log('nav_name_first: ', nav_name_first);
        window.location.pathname = '/';
        localStorage.scheme = nav_name_first;
      } else if (data_scheme >= 1 && data_scheme <= 100) {
        localStorage.scheme = data_scheme;
        
        console.log('localStorage.scheme: ', localStorage.scheme);
        window.location.pathname = '/';
      }
  });
  
  $('.nav_name_blog').on('click', function(){
    let data_scheme = $(this).data('scheme');
    let nav_name_blog = $('.nav_name_blog').data('scheme');
      if (data_scheme == nav_name_blog) {
        
        window.location.pathname = '/';
        localStorage.scheme = nav_name_blog;
        
      }
  });
  
  if (window.location.pathname == "/" && localStorage.scheme != 0 && localStorage.scheme != 101 && localStorage.scheme != 102 && localStorage.finder_page == 1) {
    localStorage.finder_page = 0;
  
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
  if (window.location.pathname == "/" && localStorage.scheme == 101 && localStorage.finder_page == 1 && localStorage.scheme != 102) {
   
    localStorage.finder_page = 0;
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
  if (window.location.pathname == "/" && localStorage.scheme == 102) {
    console.log("tuta");
    
    localStorage.finder_page = 0;
    if (window.matchMedia("(max-width: 996px)").matches) {
      function linkTime() {
        let destination = $('#sect6').offset().top;
        $('html, body').animate({ scrollTop: destination }, 600);
        return false;
      }
      setTimeout(linkTime, 500);
      } else {
        fullpage_api . moveTo (6);
      }
      localStorage.scheme = 0;
  }
  
  if (window.location.pathname == "/" && localStorage.scheme == 103) {
    console.log("tuta");
    
    localStorage.finder_page = 0;
    if (window.matchMedia("(max-width: 996px)").matches) {
      function linkTime() {
        let destination = $('#sect5').offset().top;
        $('html, body').animate({ scrollTop: destination }, 600);
        return false;
      }
      setTimeout(linkTime, 500);
      } else {
        fullpage_api . moveTo (5);
      }
      localStorage.scheme = 0;
  }
  
  function add_visible_content () {
    let find_content = $('.hidden_tab_content').find('.content' + localStorage.scheme);
    console.log('localStorage.scheme: ', '.content' + localStorage.scheme);
    
  
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
  

  if (localStorage.vakancy == true) {
    
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
    localStorage.vakancy = false;

  }
  localStorage.setItem('vakancy', false);
  
  
  
  
  
  
  
  localStorage.setItem('psevdo_link', '0');
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  $.extend($.lazyLoadXT, {
      edgeY:  250,
      srcAttr: 'data-src'
    });
  
  
    // if (window.matchMedia("(min-width: 996px)").matches) {
    
    // } else {
    //   $('.hidden_name').addClass('scroll_all');
    // }
  
    if ($(".all_bottom_nav").hasClass("all_bottom_nav_inactive")) {
        $('.all_bottom_nav_inactive').attr("href", "#")
    }
  
  
  
  
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
          
            $('.services_form').find('.select__input1').find('.visual_label').removeClass('visual_label_active');
            $('.select__input1').removeClass('select__input_activate');
            } else if (form_input1[0].outerText != '') {
              $('.services_form').find('.select__input1').find('.visual_label').addClass('visual_label_active');
              $('.select__input1').addClass('select__input_activate');
            }
          if (form_input2[0].outerText == '') {
            $('.services_form').find('.select__input2').find('.visual_label').removeClass('visual_label_active');
            $('.select__input2').removeClass('select__input_activate');
            } else if (form_input2[0].outerText != '') {
              $('.services_form').find('.select__input2').find('.visual_label').addClass('visual_label_active');
              $('.select__input2').addClass('select__input_activate');
            }
          if (form_input3[0].outerText == '') {
            $('.services_form').find('.select__input3').find('.visual_label').removeClass('visual_label_active');
            $('.select__input3').removeClass('select__input_activate');
            } else if (form_input3[0].outerText != '') {
              $('.services_form').find('.select__input3').find('.visual_label').addClass('visual_label_active');
              $('.select__input3').addClass('select__input_activate');
            }
          if (form_input4[0].outerText == '') {
            $('.services_form').find('.select__input4').find('.visual_label').removeClass('visual_label_active');
            $('.select__input4').removeClass('select__input_activate');
            } else if (form_input4[0].outerText != '') {
              $('.services_form').find('.select__input4').find('.visual_label').addClass('visual_label_active');
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
      
      // if ($(input_select).val() != "") {
      //   $(this).parents('.select').find('.add_error').remove();
      // }
  
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
  
  
     
            $('.services_form').on("submit", function(event) {
              
                  // event.preventDefault();
                  //     showValues();
          });
  
                // var serviceFinder = $('.services_form').attr('action');
                // console.log('serviceFinder: ', serviceFinder);
  
                // function showValues(){
                //   let vallue_vant5 = true;
                  // $('#rd1').val();
                  // if ($("#rd1").is(":checked")) {
                  //   vallue_vant5 = true;
                  // } else {
                  //   vallue_vant5 = false;
                  // }
                  // console.log('$(', $('#rd1').val());
                  // let data = $(".services_form").serializeArray();
                // console.log('data: ', data);
                  // let form_input = {
                  //   vant1: $('.form_select_1').val(),
                  //   vant2: $('.form_select_2').val(),
                  //   vant3: $('.form_select_3').val(),
                  //   vant4: $('.form_select_4').val(),
                  //   vant5: vallue_vant5,
                  // }

                // var obj = {};
                // $.each(x, function(i, field){
                //   if(field.value.trim() != ""){
                //     if(obj[field.name] != undefined){
                //       var val = obj[field.name];
                //       if(!Array.isArray(val)){
                //          arr = [val];
                //       }
                //       arr.push(field.value.trim());
                //       obj[field.name] = arr;
                //     }else{
                //       obj[field.name] = field.value;
                //     }
                //     }
                // });
                //       fetch(serviceFinder, {
                //         method: 'POST',
                //         body: JSON.stringify(form_input)
                //       })
                //       .then(data => {
                //         return data.json();
                //       })
  
  
                // }
  
  
  
  
  
  
  
  });