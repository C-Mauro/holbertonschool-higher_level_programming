$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  let films = data.results;
  for (let i = 0; i < films.length; i++) {
    let title = films[i].title;
    $('#list_movies').append('<li>' + title + '</li>');
  }
});
