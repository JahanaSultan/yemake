// PREVIEW IMAGE

let preview_prf = document.getElementById("prf-img")
let preview_cvr = document.getElementById("cvr-img")
let file_input_profile = document.querySelector(".prf-img input[type='file']")
let file_input_cover = document.querySelector(".cvr-img input[type='file']")
let link_prf = document.querySelector(".prf-img .hide a")
let link_cvr = document.querySelector(".cvr-img .hide a")
file_input_profile.addEventListener("change", () => {
  preview_prf.src = window.URL.createObjectURL(file_input_profile.files[0])
})
file_input_cover.addEventListener("change", () => {
  preview_cvr.src = window.URL.createObjectURL(file_input_cover.files[0])
})

if (link_prf) {
  preview_prf.src = link_prf.href
}
if (link_cvr) {
  preview_cvr.src = link_cvr.href
}
let input = [...document.querySelectorAll(".field input")]

input.map(e => e.classList.add("contact-input"))