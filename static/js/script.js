$(function () {
  $(".item col-12 col-lg-4 p-3 mb-4").slice(0, 3).show();
  $("body").on('click touchstart', '.load-more', function (e) {
      e.preventDefault();
      $(".item col-12 col-lg-4 p-3 mb-4:hidden").slice(0, 3).slideDown();
      if ($(".item col-12 col-lg-4 p-3 mb-4:hidden").length == 0) {
          $(".load-more").css('visibility', 'hidden');
      }
      $('html,body').animate({
          scrollTop: $(this).offset().top
      }, 1000);
  });
});