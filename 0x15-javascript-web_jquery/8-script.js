$.get(
  'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  function (data) {
    $('UL#list_movies').append(
      ...data.results.map((movie) => $('<LI></LI>').text(movie.title))
    );
  }
);
