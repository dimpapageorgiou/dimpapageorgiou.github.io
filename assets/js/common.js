$(document).ready(function() {

    $('a.abstract').click(function() {

        var entry = $(this).parent().parent();

        entry.find(".abstract.hidden").toggleClass('open');
        entry.find(".bibtex.hidden.open").removeClass('open');

        // Close citation box
        entry.find(".citation-box").hide();

    });

    $('a.bibtex').click(function() {

        var entry = $(this).parent().parent();

        entry.find(".bibtex.hidden").toggleClass('open');
        entry.find(".abstract.hidden.open").removeClass('open');

        // Close citation box
        entry.find(".citation-box").hide();

    });

    $('a').removeClass('waves-effect waves-light');

});