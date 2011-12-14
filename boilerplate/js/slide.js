
// Credits: 

// Queness, "Create a Vertical, Horizontal and Diagonal Sliding Content Website with jQuery"
// http://www.queness.com/post/356/create-a-vertical-horizontal-and-diagonal-sliding-content-website-with-jquery




$(document).ready(function() {
	
	initializeMap();

	////////////////////////
	// Sliding Navigation //
	////////////////////////

	// Begin at Dashboard
	$('#wrapper').scrollTo('#atAGlanceTile', 0);

	// Add slider click action when 
	$('body').on('click', '.panel', function(event) {
		
		$('.panel').removeClass('selected');
		$(this).addClass('selected');

		var target = $(event.target);

		// Could be done more efficiently, but works
		if( target.is('.eventsLink') || target.is('.eventsLink span') ) {
			$('#wrapper').scrollTo($(this).attr('href'), 1100, { easing: 'easeInOutExpo', offset:{left:$('.item').width()/6} });
		} else if( target.is('.chatterBoxLink') || target.is('.chatterBoxLink span') ) {
			$('#wrapper').scrollTo($(this).attr('href'), 1100, { easing: 'easeInOutExpo', offset:{left:-$('.item').width()/6} });
		} else {
			$('#wrapper').scrollTo($(this).attr('href'), 1100, { easing: 'easeInOutExpo' });
		}
		return false;
	});

	// Call function in a template - doesn't work
	/*$('.jqtest span').click( function() {
		console.log('clicked inside template');
	});*/

	$(window).resize(function() {
		resizePanel();
	});
	
	// End slide nav
	

	// Expand scenes-nav on rollover
	$('.dropdown-title#scenesMenu').toggle(function() {
			$('.scenes-nav').slideDown(300);
			$(this).html('More Scenes &uarr;');
		}, function() {
			$('.scenes-nav').slideUp(300);		
			$(this).html('More Scenes &darr;');
		}
	);


	// Print filter search box value to a list
	$("#add-filter").click(function() {
		var value = $('#search-box').val();
		$("#current-filters").append('<li><span class="remove-filter"></span>' + value + '</li>');
				
		$(".remove-filter").click(function() {
			$(this).parent('li').hide(300, function() {
				$(this).remove();
			});
		});
		
    });


}); // document.ready

function resizePanel() {
	width = $(window).width;
	height = $(window).height();
	mask_width = width + $('.item').length;

	$('#wrapper, .item').css({width: width, height: height});
	$('#mask').css({width: mask_width, height: height});
	$('#wrapper').scrollTo($('a.selected').attr('href'), 0);
}

var map, map2;

function initializeMap() {	

	// Your location would be the center of the map	
	var youLoc = new google.maps.LatLng(40.44201350, -79.96255210);
	var myOptions = {
      zoom: 15,
      center: youLoc,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    };

    map = new google.maps.Map(document.getElementById("map_canvas"),
        myOptions);

    map2 = new google.maps.Map(document.getElementById("map_canvas2"),
        myOptions);    
	
} // initializeMap

function cycleTeasers() {
	var next = $("#chatter-teasers li:last-child");
    $.unique(next).each( function() {
		$(this).hide()
        $(this).prependTo(this.parentNode);
        $(this).slideDown(200);
        // hack to add a more sensible time to the teaser feed
        $(this).find('.timesince').html('1 minute')
    });
}

window.setInterval(cycleTeasers,10000);
