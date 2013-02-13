jQuery(function($){
    $("input[id='blacklist_search_value']").autocomplete({
        source: function(request, response) {
            $.ajax({
                url: "mapBlacklistLiveSearch",
                dataType: "json",
                data: {
                    featureClass: "P",
                    style: "full",
                    maxRows: 10,
                    client_contains: request.term
                },
                success: function(data) {
                    response($.map(data, function(item) {
                        return {
                            label: item,
                            value: item
                        };
                    }));
                }
            });
        },
        minLength: 4
    });

});
