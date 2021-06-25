module.exports = {
  mode: 'jit',
  // purgeを指定して、呼び出すクラスを指定する。ビルドサイズを圧縮する。
  purge: ['./pages/**/*.{js,ts,jsx,tsx}', './components/**/*.{js,ts,jsx,tsx}'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
