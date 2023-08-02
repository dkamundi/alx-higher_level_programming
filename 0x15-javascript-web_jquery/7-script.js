ler skywarsData = []
var skywars = async function(){
	await fetch("https://swapi-api.alx-tools.com/api/people/5/?format=json")
	.then((response) => response.json())
	.then((data) => (skywarsData = data))

	$("#character").text(skywarsData.name);
}

skywars()
