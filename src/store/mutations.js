const mutations = {
  SET_CURRENT_CINEMA (state, cinema) {
    state.currentCinema = cinema
  },
  SET_CINEMAS (state, cinemas) {
    state.cinemas = cinemas
  },
  SET_MOVIES (state, movies) {
    state.movies = movies
  }
}

export default mutations
