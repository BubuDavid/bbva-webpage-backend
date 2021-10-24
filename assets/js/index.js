/*================ CARDS ================*/
const cardSection = document.getElementById('cards')

async function getCountries(apiURL) {
	const response = await fetch(apiURL, {
    method: 'GET', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
	})
	return response.json()
}

async function createCards(apiURL) {
	responseJson = await getCountries(apiURL)
	countriesInfo = responseJson.countries
	countriesInfo.forEach(country => {
		card = document.createElement('div')
		card.className = "card"
		card.innerHTML = `
			<div class="card-header">
				<img src="${country.flag}" alt="${country.name} Flag" class="card-icon">
				<p class="card-title">${country.name}</p>
			</div>
			<p class="card-summary">Lorem ipsum dolor sit amet consectetur adipisicing elit. </p>
		`
		cardSection.appendChild(card)
	});
}

createCards('http://18.116.247.11:5000/')