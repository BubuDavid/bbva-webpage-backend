/*================ CARDS ================*/
const cardSection = document.getElementById('cards')

async function getCountries(apiURL) {
	const response = await fetch(apiURL)
	const country_list = await response.json()
	return country_list
}

async function createCards(apiURL) {
	countriesInfo = await getCountries(apiURL)
	
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

createCards('http://localhost:3000/countries')