const API_KEY = process.env.API_KEY;

// APIエンドポイント
export default {
  fetchTrending: {
    title: "栃木",
    url: `/trending/all/week?api_key=${API_KEY}&language=en-US`,
  },
  fetchTopRated: {
    title: "群馬",
    url: `/movie/top_rated?api_key=${API_KEY}&language=en-US`,
  },
  fetchActionMovies: {
    title: "山梨",
    url: `/discover/movie?api_key=${API_KEY}&with_genres=28`,
  },
  fetchComedyMovies: {
    title: "長野",
    url: `/discover/movie?api_key=${API_KEY}&with_genres=35`,
  },
  fetchHorrorMovies: {
    title: "新潟",
    url: `/discover/movie?api_key=${API_KEY}&with_genres=27`,
  },
  fetchRomanceMovies: {
    title: "福島",
    url: `/discover/movie?api_key=${API_KEY}&with_genres=10749`,
  },
  fetchMystery: {
    title: "山形",
    url: `/discover/movie?api_key=${API_KEY}&with_genres=9648`,
  },
  // fetchSciFi: {
  //   title: "Sci-Fi",
  //   url: `/discover/movie?api_key=${API_KEY}&with_genres=878`,
  // },
  // fetchWestern: {
  //   title: "Western",
  //   url: `/discover/movie?api_key=${API_KEY}&with_genres=37`,
  // },
  // fetchAnimation: {
  //   title: "Animation",
  //   url: `/discover/movie?api_key=${API_KEY}&with_genres=16`,
  // },
  // fetchTV: {
  //   title: "TV Movie",
  //   url: `/discover/movie?api_key=${API_KEY}&with_genres=10770`,
  // },
};
