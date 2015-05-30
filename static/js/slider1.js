/*global $, _ */
function csrfSafeMethod(method) {
	    // these HTTP methods do not require CSRF protection
	    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}

$(function() {
    "use strict";
    /////////////////////////////////// SLIDER MANAGER //////////////////////////////////////////
/*    var thumbs = $('.thumbs');

	document.onkeydown = keyHit;
	var thisPic = 0;
	var myPix = new Array();
	
	//add references to myPix
	var imgs = thumbs.find("a").attr("href");
	for(var i = 0, len = imgs.length;i < len; ++i){
		myPix.push(imgs[i]);
	}
	*/
/*	
	function keyHit(evt) {

 		var imgCt = myPix.length-1;
 		var ltArrow = 37;
 		var rtArrow = 39;
 		var thisKey = (evt) ? evt.which : window.event.keyCode;
 		if (thisKey == ltArrow) {
 			chgSlide(-1);
 		}
 		else if (thisKey == rtArrow) {
 			chgSlide(1);
 		}
 		return false;
 		function chgSlide(direction) {
 			thisPic = thisPic + direction;
 			if (thisPic > imgCt) {
 				thisPic = 0;
 			}
 				if (thisPic < 0) {
 				thisPic = imgCt;
 			}
 			document.getElementById("largeImg").src = myPix[thisPic];
 		}
	}
    */
    ////////////////////////////////SLIDE DOWNLOAD BLOCK////////////////////////////////////////////
    
    var csrftoken = $('input[type=hidden][name=csrfmiddlewaretoken]').val();
    $.ajaxSetup({
		    beforeSend: function(xhr, settings) {
		        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		            xhr.setRequestHeader("X-CSRFToken", csrftoken);
		        }
		    }
		});

    /* The last highest ID of a message, this is to avoid returning the same messages
     * more than once.
     */

    /* Contains the current number of failed requests (for get_new_messages) in a row. */
    var failed_requests_in_a_row = 0;

/*    function addToSlider(result) {
            			failed_requests_in_a_row = 0;
						
			            var data = result;
			            if (data['file']===null) {
			            	return;
			            }
			            
			            var src=data['file'];
			            
			            var thumb = $('<a/>').attr("href",data['file']).attr("title", 'Slide #'+data['position']);
						myPix.push(data['file']);
						
						var img = new Image();
						img.src=data['file'];
						thumb.append(img);						
						thumbs.append(thumb);			

						
        			}
*/



    var get_new_immage = function() {
				        if (failed_requests_in_a_row >= 100) {
				            return;
				        }
				        var request = $.ajax({
										url : '/api/slide/'+SLIDER.broadcasting+'/'+SLIDER.slides.length+'/',
				        				//url : '/api/slide/'+SLIDER.slides.length+'/',
				        				type : "GET",
										timeout : 7000,
									});
	
						//request.done(addToSlider);
				        request.done(function(result) {
	            			failed_requests_in_a_row = 0;
							
				            var data = result;
				            if (data['file'] == null) {
				            	return;
				            }
							//var div = $('<div/>', { class : 'item'});
							var img = new Image();
							img.src=data['file'];
							//div.append(img).appendTo(inner);
							var count = SLIDER.slides.length
							SLIDER.slides[SLIDER.slides.length] = img.src;
							//var indicator = $('<li/>').attr("data-target",'#myCarousel').attr("data-slide-to", data['position']);
							//indicators.append(indicator);			
							//s_count = indicators.children().length;

				            SLIDER.setImage(SLIDER.slides[count]);
				        });
				        
	
						request.fail(function(jqXHR, textStatus) {
							//console.log(textStatus);
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

