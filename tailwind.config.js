/** @type {import('tailwindcss').Config} */
module.exports = {
  mode:"jit",
  purge:[
'./templates/**/*.html'
  ],
  content: [],
  theme: {
    extend: {},
  },
  plugins: [require('@tailwindcss/forms'),],
}
