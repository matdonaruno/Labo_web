(function($){

	$(document).ready(function(){
		
		$('#open-menu').click(function(e){
      console.log('test');
			if(!$('#menu-wrapper').hasClass('opened')){
				$('#menu-wrapper').addClass('opened');
			} 
		});
    
    $('#menu-wrapper').click(function(e){
			if($('#menu-wrapper').hasClass('opened')){
				$('#menu-wrapper').removeClass('opened');
			} 
		});
    
    // disable click on menu-container
    
    //$('#menu').click(function(e){
		//	e.stopPropagation();
		//});
    
	});
		
})(jQuery)