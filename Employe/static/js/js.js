const view = document.querySelector('.red')

function redMore(){
    var dots = document.getElementByid("dots");
    var more = document.getElementByid("more");
    var btn = document.getElementByid("btn");

    if(dots.style.display === "none"){
      dots.style.display="inline";
      morestyle.display="none";
      btn.innerHTML="Подробнее";
    }else(dots.style.display === "none"){
      dots.style.display="none";
      morestyle.display="inline";
      btn.innerHTML="Скрыть";
    }
}
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

