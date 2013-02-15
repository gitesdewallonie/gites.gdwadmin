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

    addData : function(event) {
        dataToAdd = {dataId: jQuery(event.target).attr('dataId'),
                     name: jQuery(event.target).attr('dataName'),
                     description: jQuery(event.target).attr('dataDescription'),
                     provider: jQuery(event.target).attr('dataProvider')}
        // Insert data in database
        jQuery.ajax({
            type: "POST",
            url: 'mapBlacklistAddData',
            data: dataToAdd ,
            success: function(data) {
                // Remove row in html searchResult table
                jQuery(event.target).closest('tr').fadeOut(300,
                    function(){
                        jQuery(this).remove();
                    });

                rowData = JSON.parse(data)
                // Add row in html blacklist table
                jQuery.ajax({
                    type: "POST",
                    url: 'mapBlacklistRowData',
                    data: rowData,
                    success: function(data) {
                        data = jQuery(data);
                        jQuery("table#blacklist_table tr:last").after(data);
                        jQuery("table#blacklist_table tr:last").hide().fadeIn(300,
                            function(){
                                dataSelector = '[id="' + rowData.dataId + '_' + rowData.provider + '_remove_button' + '"]' + '[name="blacklist_remove_button"]';
                                jQuery(dataSelector).bind({'click': mapBlackList.removeData});
                            });
                    }
                });

            }
        });
    },

    removeData : function(event) {
        dataToAdd = {dataId: jQuery(event.target).attr('dataId'),
                     provider: jQuery(event.target).attr('dataProvider')}
        jQuery.ajax({
            type: "POST",
            url: 'mapBlacklistRemoveData',
            data: dataToAdd,
            success: function(data) {
                jQuery('[id="' + event.target.id + '"]').closest('tr').fadeOut(300,
                    function(){
                        jQuery(this).remove();
                    });
            }
        });
    },
}
