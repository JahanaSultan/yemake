// const box=document.querySelector(".main")
// const select=document.getElementById('lang')
// const loading=document.querySelector('.loading')

// const displayLoading=()=>{
//     loading.classList.add('display')
// }

// const hideLoading=()=>{
//        setTimeout(()=>{
//         loading.classList.remove('display')
//     },3000)
// }

// *Sil ve ya duzelis et ucun 

let dots=[...document.querySelectorAll(".dots")]

dots.map(e=>{
    e.addEventListener("click",()=>{
        e.nextElementSibling.classList.toggle("display")
    })
})


// *Placeholder typeeffect animasyasi ucun funksiya

function addToPlaceholder(toAdd, el) {
    el.attr('placeholder', el.attr('placeholder') + toAdd);
    return new Promise(resolve => setTimeout(resolve, 100));
}

function clearPlaceholder(el) {
    el.attr("placeholder", "");
}

function printPhrase(phrase, el) {
    return new Promise(resolve => {
        clearPlaceholder(el);
        let letters = phrase.split('');
        letters.reduce(
            (promise, letter, index) => promise.then(_ => {
                if (index === letters.length - 1) {
                    setTimeout(resolve, 2000);
                }
                return addToPlaceholder(letter, el);
            }),
            Promise.resolve()
        );
    });
} 

function printPhrases(phrases, el) {
    phrases.reduce(
        (promise, phrase) => promise.then(_ => printPhrase(phrase, el)), 
        Promise.resolve()
    );
}

function run() {
    let phrases = [
        "Balıq",
        "Şirniyyat",
        "Sərin İçkilər",
        "Plov",
        "Kabab",
        "Toyuq",
        "Mürəbbə",
        "Tərəvəz",
        "Brokolli",
        "Balqabaq",
        'Badımcan',
        'Ayran',
        'Sıyıq',
        "Nə axtarırsan?"
    ];

    printPhrases(phrases, $('#search'));
}

run()



// LOADING GIF HIDE AFTER 1 SECOND

setTimeout(() => {
    document.querySelector(".loader").classList.add("hide")
}, "1000")

