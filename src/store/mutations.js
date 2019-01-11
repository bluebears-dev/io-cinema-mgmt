const mutations = {
  SET_CURRENT_CINEMA (state, cinema) {
    state.currentCinema = cinema
  },
  SET_CINEMAS (state, cinemas) {
    state.cinemas = cinemas
  },
  SET_MOVIES (state, movies) {
    state.movies = movies
  },
  SET_TICKET_TYPES (state, ticketTypes) {
    state.ticketTypes = ticketTypes
  },
  SET_SELECTED_DATE (state, selectedDate) {
    state.selectedDate = selectedDate
  },
  SET_MOVIE_DETAILS (state, movieDetails) {
    state.movieDetails = movieDetails
  },
  SET_SHOWINGS (state, showings) {
    state.showings = showings
  },
  SET_ROOM (state, room) {
    state.room = room
  }
}

export default mutations
