$(document).ready(function(){
	// Top search form toggle
	$(".top-search-form__toggle").click(function(e){
		$(this).closest(".top-search-form").toggleClass("top-search-form_active");
		e.preventDefault();
	});
	
	
	// Mobile menu toggle
	$(".menu__toggle").click(function(e){
		var $menu = $(".menu");
		var $menuContent = $(".menu__content");
		
		if(!$menu.hasClass("menu_active")){
			$("body").addClass("overflow");
		} else {
			$("body").removeClass("overflow");
		}
		
		$menu.toggleClass("menu_active");
		$menuContent.fadeToggle(250);
		e.preventDefault();
	});
	
	
	// Top navigation
	$(".top-nav__list-item-link:has(+ .top-nav__sub)").click(function(e){
		var $parent = $(this).closest(".top-nav__list-item");
		var $sub = $(this).next(".top-nav__sub");
		
		$parent.toggleClass("top-nav__list-item_active");
		$sub.slideToggle(250);
		e.preventDefault();
	});
	
	
	// Catalog last slider
	$(".catalog-slider-last .catalog").slick({
		mobileFirst : true,
		responsive : [
			{
				breakpoint : 992,
				settings : {
					slidesToShow : 3
				}
			}
		]
	});
	
	
	// Catalog similar slider
	$(".catalog-slider_similar .catalog").slick({
		mobileFirst : true,
		responsive : [
			{
				breakpoint : 992,
				settings : "unslick"
			}
		]
	});
	
	
	// Hide current selectmenu item
	function hideSelectItem(buttonId){
		var $button = $("#" + buttonId + "-button");
		var $menu = $("#" + buttonId + "-menu");
		var $menuItems = $menu.find(".ui-menu-item");
		var currentItemId = $button.attr("aria-labelledby");
		
		// Visible all selectmenu items
		$menuItems.show();
		
		// Hide selected menu item
		$menuItems.has("#" + currentItemId).hide();
	}
	
	
	// Create selectmenu

	$(".selectmenu").selectmenu({

		width : false,
		open : function(){
			hideSelectItem($(this).attr("id"));
		},
		select: function (event, ui) {
			$(this).parent('form').submit();
        }
	});
	
	// Popup open
	$("[data-popup]").click(function(e){
		var $popup = $("#" + $(this).data("popup"));
		
		$("body").addClass("overflow");
		$popup.fadeIn(300);
		e.preventDefault();
	});
	
	
	// Popup close
	$(".popup__close").click(function(e){
		var $popup = $(this).closest(".popup");
		
		$("body").removeClass("overflow");
		$popup.fadeOut(300, function(){
			switch($popup.attr("id")){
				case "popup-offer" :
					$popup.removeClass("popup-offer_is-thank");
					$popup.find(".popup-offer__thank").fadeOut(250);
					break;
			}
		});
		e.preventDefault();
	});

	// Validate offer form
	$('form input').keypress(function (e) {
		if (e.which == 13) {
			$(this).parents('form').submit();
			return false;    //<---- Add this line
		}
	});
	$(".offer-form").submit( function (e) {
		e.preventDefault();
		var url = $(this).attr("action");
		var method = $(this).attr("method");
		$(".error").removeClass('error');
		$(this).find("label").remove();
		$.ajax({
			dataType:"json",
			url: url,
			method: method,
			data: $(this).serialize(),
			success: function (data) {
				console.log(data.status);

				if(data.status === "ok"){
					var $popupOffer = $(".popup-offer");
					var $thank = $(".popup-offer__thank");
					$popupOffer.addClass("popup-offer_is-thank");
					$thank.fadeIn(250);
				} else {
					for(var k in data){
						console.log(k, data[k]);
						$el = $("#id_"+k);
						$el.addClass("error");
						$el.parent().append("<label class='error'>"+data[k].join(", ")+"</label>");
					}
				}
            }
		});
    });

	$(".subs-form").submit( function (e) {
		e.preventDefault();
		var url = $(this).attr("action");
		var method = $(this).attr("method");
		$(".error").removeClass('error');
		$(this).find("label").remove();
		$.ajax({
			dataType:"json",
			url: url,
			method: method,
			data: $(this).serialize(),
			success: function (data) {
				console.log(data.status);

				if(data.status === "success"){
					var $sectionSubs = $(".section-subs");
                    $sectionSubs.addClass("section-subs_is-thank");
				} else {
					for(var k in data){
						console.log(k, data[k]);
						$el = $("#id_"+k);
						$el.addClass("error");
						$el.parent().append("<label class='error'>"+data[k].join(", ")+"</label>");
					}
				}
            }
		});
    })

	$("a.topLink").click(function() {
      $("html, body").animate({
         scrollTop: $($(this).attr("href")).offset().top + "px"
      }, {
         duration: 500,
         easing: "swing"
      });
      return false;
   });

});