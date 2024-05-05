// fetches and lists the title for all movies by using a URL
$(function () {
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
        $.each(data.results, function(index, movie) {
            var newList = $('<li>').text(movie.title);
            $('UL#list_movies').append(newList);
        });
    });
});