
  let preview = document.getElementById("preview")
  let file_input = document.querySelector("input[type='file']")
  let link = document.querySelector("form p a")

  file_input.addEventListener("change", () => {
    preview.style.display = "inline-block"
    preview.src = window.URL.createObjectURL(file_input.files[0])
  })

  if (link.href) {
    preview.style.display = "block"
    preview.src = link.href
  }

  