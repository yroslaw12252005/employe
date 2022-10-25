const view = document.querySelector('.red')
view.addEventListener('clic', function(){
  console.log("clic")
})


$('.view img').click(function() {
  let src = $(this).attr('src');
  $('.popup img').attr('src',src);
  $('.popup').fadeIn(); 
  $('.fonClos').fadeIn(); 
});

$(' .view1 img').click(function() {
  let src = $(this).attr('src');
  $('.view2 img').attr('src',src);
  $('.view2').fadeIn();
  $('.fonClos').fadeIn(); 
});

$('.clous').click(function() {
  $('.popup').fadeOut();
  $('.view2').fadeOut();
  $('.fonClos').fadeOut();
});

$('.fonClos').click(function() {
  $('.popup').fadeOut();
  $('.fonClos').fadeOut();
  $('.view2').fadeOut();
});
