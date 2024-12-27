/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}"
  ],
  theme: {
    extend: {
      colors: {
        'threat-low': '#4CAF50',
        'threat-medium': '#FF9800',
        'threat-high': '#F44336'
      }
    }
  },
  plugins: []
}