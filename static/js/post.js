$(function(){
  $('a.at').click(
    function(){
      var parent = $(this).parents('.infos').children('.info');
      var name = parent.children('.name').html();
      var floor = parent.children('.floor').html();
      var replyContent = $('#editor-input');
      var oldContent = replyContent.val();
      var prefix = "#" + floor + "楼" + " " + "@" + name + " ";
      var newContent = '';
      if (oldContent.length > 0) {
        if (oldContent != prefix) {
          newContent = oldContent + " " + prefix;
        }
      } else {
        newContent = prefix;
      }
      replyContent.focus();
      replyContent.val(newContent);
    });
  $('ul.nav li.active').removeClass();
  $('a.toreply').mouseover(
    function(e) {
    var floor = $(this).children('span').html();
    var parent = $('#' + floor);
    var avatar = parent.children('.avatar').html();
    var name = parent.children('.infos').children('.info').children('.name').html();
    var content = parent.children('.reply_content').html();
    var floater = "<div id='floater'>" + "<div class='avatar'>" + avatar + "<\/div>" + "<span class='float_name'>" + name + ":<\/span>" + "<div class='float_content'>" + content + "<\/div><\/div>";
    $('body').append(floater);
    $('#floater').css({
      "position":"absolute",
      "background-color":"rgba(255,255,255,0.8)",
      "padding":"12px 15px",
      "border-radius":"3px",
      "box-shadow": "0px 0px 10px rgba(0, 0, 0, 0.8)",
      "max-width":"550px",
      "max-height":"500px",
      "top":(e.pageY + 20) + "px",
      "left":(e.pageX + 10) + "px"
      }).show("fast");
    }).mouseout(
      function(){
      $('#floater').remove();
      });
  $('a.toreply').click(function(){
      var floor = $(this).children('span').html();
      $('.isit').removeClass('isit');
      $('#' + floor).addClass('isit');
      $.scrollTo('#' + floor,500);
      });
  $('form :input').blur(function(){
      if($(this).is('#reply_name')){
        if(this.value == ''){
          $('span.reply_name').css({"color":"#C01F2F"}).html("请输入正确的名字");
        } else {
          $('span.reply_name').css({"color":"#468847"}).html("√ 输入正确");
        }
      }
      if($(this).is('#reply_email')){
        if(this.value == '' || (this.value != "" && !/.+@.+\.[a-zA-Z]{2,4}$/.test(this.value))){
          $('span.reply_email').css({"color":"#C01F2F"}).html("请输入正确的 E-Mail 地址");
        } else {
          $('span.reply_email').css({"color":"#468847"}).html("√ 输入正确");
        }
      }
      }).keyup(function(){
        $(this).triggerHandler('blur');
      }).focus(function(){
        $(this).triggerHandler('blur');
      });
  $('.btn').click(function(){
      $('span.reply_name').css({"color":"#ccc"}).html("必填");
      $('span.reply_email').css({"color":"#ccc"}).html("必填 不会公开");
      var $name = $('input#reply_name');
      var $email = $('input#reply_email');
      var $editor = $('#editor-input');
      $editor.css({"border-color":"#DADADA"});
      var error = 0;
      if($name.val() == ''){
        $('span.reply_name').css({"color":"#C01F2F"}).html("请输入正确的名字");
        error = 1;
      } else {
        $('span.reply_name').css({"color":"#468847"}).html("√ 输入正确");
      }
      if($email.val() == '' || ($email.val() != "" && !/.+@.+\.[a-zA-Z]{2,4}$/.test($email.val()))){
        $('span.reply_email').css({"color":"#C01F2F"}).html("请输入正确的 E-Mail 地址");
        error = 1;
      } else {
        $('span.reply_email').css({"color":"#468847"}).html("√ 输入正确");
      }
      if($editor.val() == ''){
        $editor.css({"border-color":"#C01F2F"});
        error = 1;
      }
      if(error===1){
      return false;
      }
      });
    var website = $('#reply_website');
    var url = website.val();
    if (url.indexOf("http://") != 0) {
      var newurl = "http://" + url; 
      website.val(newurl);
    }
    if (website.val() == "http://") {
      website.css({"color":"#ddd"});
    }
    website.focus(function(){
      website.css({"color":"#555"});
    }).blur(function(){
      if (website.val() == "http://") {
        website.css({"color":"#ddd"});
      }
    });
  })
