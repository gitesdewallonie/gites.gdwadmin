jQuery(document).ready(function( $) {

    var addLine;
    addLine = function(){

        var newLine = $("#metadata tr:last").clone();
        newLine.attr('class', 'new-line');   // XXX : add CSS .new-line class

        newLine.find('input[type="text"]').each(function() {
            $(this).val('');
        });

        // By default, new metadata should not be filterable
        newLine.find('input[type="checkbox"]').remove();

        // Remove pk field because we create a new metadata !
        newLine.find('input[type="hidden"]').remove();

        newLine.appendTo($("#metadata table"));

    };

    $("#add-metadata").click(addLine);

});
