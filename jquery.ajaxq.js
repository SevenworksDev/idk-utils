/*
 * jQuery AjaxQ - AJAX request queueing for jQuery
 *
 * Version: 0.0.1
 * Date: July 22, 2008
 *
 * Copyright (c) 2008 Oleg Podolsky (oleg.podolsky@gmail.com)
 * Licensed under the MIT (MIT-LICENSE.txt) license.
 *
 * http://plugins.jquery.com/project/ajaxq
 * http://code.google.com/p/jquery-ajaxq/
 */

jQuery.ajaxq = function (queue, options)
{
	// Initialize storage for request queues if it's not initialized yet
	if (typeof document.ajaxq == "undefined") document.ajaxq = {q:{}, r:null};

	// Initialize current queue if it's not initialized yet
	if (typeof document.ajaxq.q[queue] == "undefined") document.ajaxq.q[queue] = [];
	
	if (typeof options != "undefined") // Request settings are given, enqueue the new request
	{
		// Copy the original options, because options.complete is going to be overridden

		var optionsCopy = {};
		for (var o in options) optionsCopy[o] = options[o];
		options = optionsCopy;
		
		// Override the original callback

		var originalCompleteCallback = options.complete;

		options.error = function(e){
			//console.log(e);
		};
		
		options.complete = function (request, status)
		{
			// Dequeue the current request
			document.ajaxq.q[queue].shift();
			document.ajaxq.r = null;
			
			// Run the original callback
			if (originalCompleteCallback) originalCompleteCallback (request, status);

			// Run the next request from the queue
			if (document.ajaxq.q[queue].length > 0) {
				//console.log('sending: ' + document.ajaxq.q[queue][0].url);
				document.ajaxq.r = jQuery.ajax (document.ajaxq.q[queue][0]);
			}
		};
		
		
		//si la peticion es de mouse move
		if(options.url.indexOf('action=move') != -1){
			var found = false;
			//si hay elementos en la cola
			if(document.ajaxq.q[queue].length){
				//recorro la cola
				//si ninguna de las peticiones en move la agrego
				for(p in document.ajaxq.q[queue]){
					if(p.url){
						if(p.url.indexOf('action=move') >= 0){
							//piso la anterior
							document.ajaxq.q[queue][p] = options;
							found = true;
							break;
						}
					}
				}
			}
			if (!found)
				document.ajaxq.q[queue].push (options);
		}


		// Enqueue the request if not action move
		if(options.url.indexOf('action=move') == -1) {
			document.ajaxq.q[queue].push (options);
		}
		
		// Also, if no request is currently running, start it
        if (document.ajaxq.q[queue].length == 1) {
          //console.log('sending: ' + document.ajaxq.q[queue][0].url);
          document.ajaxq.r = jQuery.ajax (document.ajaxq.q[queue][0]);
        }
	}
	else // No request settings are given, stop current request and clear the queue
	{
		if (document.ajaxq.r)
		{
			document.ajaxq.r.abort ();
			document.ajaxq.r = null;
		}

		document.ajaxq.q[queue] = [];
	}
}
