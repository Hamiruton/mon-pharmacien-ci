/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        bgColor: '#eeeeee',
        primary: {
          normal: '#80cbc4',
          shades: {
            100: '#73b7b0',
            200: '#66a29d',
            300: '#5a8e89',
            400: '#4d7a76',
            500: '#406662',
            600: '#33514e',
            700: '#263d3b',
          },
          tints: {
            100: '#8dd0ca',
            200: '#99d5d0',
            300: '#a6dbd6',
            400: '#b3e0dc',
            500: '#c0e5e2',
            600: '#cceae7',
            700: '#d9efed',
          }
        },
        secondary: {
          normal: '#004d40',
          tints: {
            100: '#1a5f53',
            200: '#337166',
            300: '#4d8279',
            400: '#66948c',
          }
        },
        error: '#b00020',
        valid: '#62b965', 
      },
    },
  },
  plugins: [require('rippleui')],
}