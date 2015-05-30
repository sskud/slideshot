/*global $, _ */
function csrfSafeMethod(method) {
	    // these HTTP methods do not require CSRF protection
	    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}

$(function() {
    "use strict";
    // make sure AJAX-requests send the CSRF cookie, or the requests will be rejected.
    var csrftoken = $('input[type=hidden][name=csrfmiddlewaretoken]').val();

    $.ajaxSetup({
		    beforeSend: function(xhr, settings) {
		        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		            xhr.setRequestHeader("X-CSRFToken", csrftoken);
		        }
		    }
		});
    
    var indicators = $('.carousel-indicators');
	var inner = $('.carousel-inner');
    var in_unload = false;

    $(window).bind('beforeunload', function() {
        in_unload = true;
    });

    /* The last highest ID of a message, this is to avoid returning the same messages
     * more than once.
     */
    var s_count = indicators.children().length;

    /* Contains the current number of failed requests (for get_new_messages) in a row. */
    var failed_requests_in_a_row = 0;

    
    var get_new_immage = function() {
        if (failed_requests_in_a_row >= 100) {
            return;
        }
        var request = $.ajax({
						url : '/slide_get/',
						data: { bk : 1, pos : s_count},
						type : "POST",
						timeout : 7000,
					});

					request.done(function(result) {
            			failed_requests_in_a_row = 0;
						
			            var data = result;
			            if (data['file']===null) {
			            	return;
			            }
						var div = $('<div/>', { class : 'item'});
						var img = new Image();
						img.src=data['file'];
						div.append(img).appendTo(inner);
						var indicator = $('<li/>').attr("data-target",'#myCarousel').attr("data-slide-to", data['position']);
						indicators.append(indicator);			
						s_count = indicators.children().length;
						
						//append in slider
						console.log(result);
        			});

					request.fail(function(jqXHR, textStatus) {
						console.log(textStatus);
            			/* Seems to happen on hibernate, the request will restart. */
            		
            			/* A fail has happened, increment the counter. */
            			failed_requests_in_a_row += 1;
					});
					
					request.always(function() {
						setTimeout(get_new_immage, 7000);
					});
    };

    setTimeout(get_new_immage, 7000);
});