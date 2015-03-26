$(document).ready(function() 
{
    $('#showmenu').click(function() 
    {
        $('.menuListe').slideToggle("medium");
        $('.showMenuArrow').toggleClass("hide");
    });
});