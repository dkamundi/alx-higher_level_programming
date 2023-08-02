let skywarsData = []
var skywars = async function(){
    await fetch("https://swapi-api.hbtn.io/api/films/?format=json")
    .then((response) => response.json())
    .then((data) => (skywarsData = data.results))

    for (let i = 0; i < skywarsData.length; i++) {
        $("#list_movies").append(
            skywarsData.map(film => `<li>${film.title}</li>`)
        );
    }
}

skywars()
