(function($)
{
    $(document).ready(function() {
        mapBlackList.initialize();
    });
})(jQuery);


var mapBlackList = {

    initialize : function()
    {
        mapBlackList.initHandlers();
    },

    initHandlers : function()
    {
        jQuery("input#blacklist_search_value").autocomplete(mapBlackList.liveSearchOptions);
        jQuery("input#blacklist_search_value").bind({'keypress': mapBlackList.liveSearchKeyPress});
    },

    liveSearchOptions : {
        source: function(request, response) {
            jQuery.ajax({
                url: "mapBlacklistLiveSearch",
                dataType: "json",
                data: {
                    featureClass: "P",
                    style: "full",
                    maxRows: 10,
                    client_contains: request.term
                },
                success: function(data) {
                    response(jQuery.map(data, function(item) {
                        return {
                            label: item,
                            value: item
                        };
                    }));
                }
            });
        },
        minLength: 4
    },

    liveSearchKeyPress : function(event) {
        if(event.which == 13) {
            alert('You pressed enter!');
        }
    },
}
