
// *Sil ve ya duzelis et ucun 

let dots=[...document.querySelectorAll(".dots")]

dots.map(e=>{
    e.addEventListener("click",()=>{
        e.nextElementSibling.classList.toggle("display-crud")
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
}, "500")


// Modal Display Function


const modal_func=(deleteButton, deletemodal, deletecontent, link )=>{
    deleteButton.map(e=>{
        e.addEventListener("click",()=>{
        deletemodal.classList.add("display")
        console.log(e.dataset.id)
        deletecontent.setAttribute("action",`/${link}/${e.dataset.id}/`)
        })
    })
    
}

// MODALS CLICK BODY AND HIDE

let mdl=document.querySelector(".modal")
let delete_comment=[...document.querySelectorAll(".delete-comment")]
let delete_recipe=[...document.querySelectorAll(".delete-recipe")]
let delete_blog=[...document.querySelectorAll(".delete-blog")]
let mdl_content=document.querySelector(".modal-content")

mdl.addEventListener("click",()=>{
    mdl.classList.remove("display")
})


modal_func(delete_recipe,mdl,mdl_content,"delete-recipe")
modal_func(delete_blog,mdl,mdl_content,"delete-blog")
modal_func(delete_comment,mdl,mdl_content,"delete-comment")



const nav = document.querySelector('nav');
const navlinks=document.querySelector(".nav-links")

window.addEventListener("scroll",()=>{
    
    if (window.scrollY >= 60) {  
        nav.classList.add('sticky-nav');
        navlinks.getElementsByClassName.top="50px"
      } else {
        nav.classList.remove('sticky-nav');    
        navlinks.getElementsByClassName.top="60px"
      }
})

let hamburger=document.querySelector(".hamburger")
hamburger.addEventListener("click",()=>{
hamburger.classList.toggle("toggle")
navlinks.classList.toggle("open")
})

let profile=document.querySelector(".profile-nav")
let dropdown=document.querySelector(".dropdown")
profile.addEventListener("click",()=>{
    dropdown.classList.toggle("display")
})

let bottom_profile=document.querySelector(".bottom-profile")

bottom_profile.addEventListener("click",()=>{
    dropdown.classList.toggle("transform")
})


console.log(window.innerWidth)

if(window.innerWidth > 1026){
    $('.notifications').click(function(){
        document.querySelector(".dropdown-notification").classList.toggle("show-dropdown") 
    })

    if(Number($('.notification-count').html())>0){

        const ajaxfunc=(url)=>{
        $('.notification-bell').click(function(){
            $.ajax(
            {
                type:"GET",
                url: url,
                url:url,
                success: function( data ) 
                {
                   $('.notification-count').html(0)
                }
             })
        })}

        ajaxfunc("/notification/isseen/")
        ajaxfunc("/notification/isactiverecipeseen/")
        ajaxfunc("/notification/isactiveblogseen/")
    }
}
else{
    $('.noti').click(function(){
        document.querySelector(".dropdown-notification").classList.toggle("transform") 
    })

    if(Number($('.notification-count').html())>0){

        $('.noti').click(function(){
            $.ajax(
            {
                type:"GET",
                url: "/notification/isseen/",
                success: function( data ) 
                {
                   $('.notification-count').html(0)
                }
             })
        })}
}