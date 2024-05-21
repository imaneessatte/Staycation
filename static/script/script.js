const countryList = document.getElementById('country-list');
const countryFilterBtn = document.getElementById('country-btn');
const cityList = document.getElementById('city-list');
const cityFilterBtn = document.getElementById('city-btn')
const ownerFilterBtn = document.getElementById('owner-btn')
const ownerForm = document.getElementById('owner-form')

let countryBtnActive = false
let cityBtnActive = false
let ownerBtnActive = false

countryFilterBtn.addEventListener('click',function(){
    if (countryBtnActive === false){
        countryList.classList.add('show')
        console.log("show")
        countryBtnActive = true
        cityList.classList.remove('show')
        cityBtnActive = false
    }
    else{
        countryList.classList.remove('show')
        console.log("hide")
        countryBtnActive = false
    }
})

cityFilterBtn.addEventListener('click',function(){
    if (cityBtnActive === false){
        cityList.classList.add('show')
        console.log("show")
        cityBtnActive = true
        countryList.classList.remove('show')
        countryBtnActive = false
    }
    else{
        cityList.classList.remove('show')
        console.log("hide")
        cityBtnActive = false
    }
})

ownerFilterBtn.addEventListener('click',function(){
    if(ownerBtnActive === false){
        ownerForm.classList.add('show')
        console.log('show')
        ownerBtnActive = true
        cityList.classList.remove('show')
        cityBtnActive = false
        countryList.classList.remove('show')
        countryBtnActive = false
    }
    else{
        ownerForm.classList.remove('show')
        console.log('hide')
        ownerBtnActive = false
    }
})