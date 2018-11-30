const getters = {
  getCurrentCinema (state) {
    return state.currentCinema
  },
  getCinemas (state) {
    return state.cinemas
  },
  getMovies (state) {
    return state.movies
  }
}

export default getters
