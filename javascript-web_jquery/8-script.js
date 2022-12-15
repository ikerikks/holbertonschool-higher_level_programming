const movieList = $('#list_movies');

$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data)=> {
    data = data.results    
    // console.log(data);
    for (let i in data) {
        movieList.append('<li>' + data[i].title + '</li')
    }
})