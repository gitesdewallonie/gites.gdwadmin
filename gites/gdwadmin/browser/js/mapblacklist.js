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
        jQuery("input#blacklist_search_button").bind({'click': mapBlackList.searchResult});
        jQuery("[name='blacklist_remove_button']").bind({'click': mapBlackList.removeData});
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
            mapBlackList.searchResult();
        }
    },

    searchResult : function() {
            jQuery.ajax({

                    type: "POST",
                    url: 'mapBlacklistSearchResult',
                    data: "searchValue=" + jQuery("input#blacklist_search_value").val(),
                    success: function(data) {
                                             jQuery("div#blacklist_search_result").html(data);
                                             jQuery("[name='blacklist_add_button']").bind({'click': mapBlackList.addData});
                                            }

                    });
    },

    removeData : function(event) {
            jQuery.ajax({

                    type: "POST",
                    url: 'mapBlacklistRemoveData',
                    data: "dataId=" + event.target.id,
                    success: function(data) {
                                                jQuery("#"+event.target.id).parent().parent().fadeOut();
                                            }

                    });
    },

    addData : function(event) {
            jQuery.ajax({

                    type: "POST",
                    url: 'mapBlacklistAddData',
                    data: "dataId=" + event.target.id,
                    success: function(data) {
                                                jQuery("#"+event.target.id).parent().parent().fadeOut();

                                            }

                    });
    }
}
