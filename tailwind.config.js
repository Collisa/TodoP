const colors = require('tailwindcss/colors')

module.exports = {
  purge: [
    'app/templates/**/*.html',
    'app/templates/*.html',
    'app/templates/**/**/*.html'
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        fuchsia: colors.fuchsia,
      },
    },
  },
  variants: {
    extend: {
      cursor: ['hover', 'focus'],
    },
  },
  plugins: [],
}
